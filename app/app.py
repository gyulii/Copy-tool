import sys
import time

import logging
import pyperclip


logging.basicConfig(format="%(levelname)s-%(asctime)s - %(message)s", datefmt="%H:%M:%S", level=logging.DEBUG)
from datetime import datetime

from key_register import KeyRegister
from MainWindow import Ui_MainWindow
from mouse_handler import MouseHandler
from ocr import OCR_engine_interface
from pynput import keyboard
from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

# import PySide6 before matplotlib
from PySide6.QtCore import (
    QAbstractListModel,
    QMutex,
    QObject,
    QRunnable,
    Qt,
    QThreadPool,
    QTimer,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QSizeGrip,
    QVBoxLayout,
    QWidget,
)


from writer import Writer


import ctypes

myappid = "mycompany.myproduct.subproduct.version"  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class WritingThreadSignals(QObject):
    signal_writing_done = Signal(bool)


MutexWritingController = QMutex()


class WritingThread(QRunnable):
    def __init__(self, Writer: Writer, input_text: str) -> None:
        super().__init__()

        self.WritingController = Writer
        self.WritingController.load_text(input_text)
        self.signals = WritingThreadSignals()

    @Slot()
    def run(self):
        self.WritingController.run()  # TODO: If disabled, prompt enable
        self.signals.signal_writing_done.emit(True)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Frameless window

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.topMiddle.mouseMoveEvent = self.move_window
        QSizeGrip(self.grip_bottom_right)  # Invisible Frame widget used as a corner grip
        app.setWindowIcon(QtGui.QIcon("./icon.ico"))

        # Button mapping

        self.ButtonCopyPageSelect.clicked.connect(self.select_copy_page)
        self.ButtonSecondPage.clicked.connect(self.select_second_page)
        self.ButtonThirdPage.clicked.connect(self.select_third_page)
        self.ButtonExit.clicked.connect(self.close_app)
        self.ButtonEnableCopy.clicked.connect(self.enable_or_disable_writer)

        self.ButtonMinimalize.clicked.connect(lambda: self.showMinimized())
        self.ButtonExitTop.clicked.connect(self.close_app)

        self.ButtonChangeWindowSize.clicked.connect(self.toogle_size)
        self.window_size = False  # For the statmachine

        # Writer mapping and creation

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.controller_writing = Writer(input_text="Hi this is the default text")  # TODO: Copy from Clipboard
        self.writing_thread_counter = 0

        self.LineStartDelay.setText(f"{str(self.controller_writing.start_delay)} s")
        self.LineStartDelay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.SliderStartDelay.setValue(int(self.controller_writing.start_delay * 2))
        self.SliderStartDelay.sliderReleased.connect(self.delay_slider_released)
        self.ButtonRunOnClick.clicked.connect(self.enable_or_disable_writer_execution_after_click)

        # Start key detection thread

        self.controller_key_monitoring = KeyRegister(on_press_fn=self.detect_on_press, on_release_fn=self.detect_on_release)

        # Fill key list for auto typing

        self.hotkey_start_writer_list_copy = [keyboard.Key.caps_lock, keyboard.Key.caps_lock]

        ky_str = [
            i.name for i in self.hotkey_start_writer_list_copy
        ]  # Weird naming + 2 steps, but otherwise WinDefender starts to cry, intersing defense policy by windows
        self.LineCurrentInputKey.setText(str(ky_str))

        self.ButtonRecordNewKey.toggled.connect(self.reset_hotkeys)

        # OCR setup

        self.OCR_handler = OCR_engine_interface(auto_copy_to_clipboard=True)
        self.Button_OCR_start.clicked.connect(self.manual_start_ocr)

        self.ButtonEnable_OCR.clicked.connect(self.toggle_OCR_module)
        self.Button_OCR_AutoCopy.clicked.connect(self.toggle_OCR_module_auto_copy_to_clipboard)

        # Fill key list for OCR
        self.hotkey_start_ocr_list = [keyboard.Key.shift_l, keyboard.Key.ctrl_l]

        ky_str_for_OCR = [
            i.name for i in self.hotkey_start_ocr_list
        ]  # Weird naming + 2 steps, but otherwise WinDefender starts to cry, intersing defense policy by windows
        self.LineCurrentInputKey_OCR.setText(str(ky_str_for_OCR))

        self.ButtonRecordNewKey_OCR.toggled.connect(self.reset_hotkeys_OCR)

        # Record new hotkey for auto typing

        # Mouse handling

        self.mouse_handler = MouseHandler(on_click_fn=self.detect_mouse_click)

    # KeyPress detection

    def detect_on_press(self, key):  # TODO Seperate thread to counteract freezing!
        self.controller_key_monitoring.add_new_input_key_to_queue(key)
        logging.debug(f"{key} pressed")
        self.textEdit_PageCopy_response.append(f"The following key was pressed: {key}")
        self.textEdit_PageCopy_response.ensureCursorVisible()  # Scroll to last line

        if key == keyboard.Key.esc:
            self.controller_writing.interrupt_execution()

        # Check for autotyping input key

        if (
            self.controller_key_monitoring.check_queue_to_keycombination(self.hotkey_start_writer_list_copy) is True
            and self.ButtonRecordNewKey.isChecked() is False
        ):
            print("Starting task")
            if self.controller_writing.is_running_allowed is False:
                self.textEdit_PageCopy_response.append(">>Typing process not started, if you wish to start it please enable the module!")
            else:
                self.textEdit_PageCopy_response.append(">> Typing process started...")
            self.textEdit_PageCopy_response.ensureCursorVisible()  # Scroll to last line

            self.start_writing()
            self.controller_key_monitoring.reset_queue()  # Reset input sequence

        if (
            self.controller_key_monitoring.check_queue_to_keycombination(self.hotkey_start_ocr_list) is True
            and self.ButtonRecordNewKey_OCR.isChecked() is False
        ):
            print("Starting OCR task")
            result = self.OCR_handler.image_to_text()
            self.TextEdit_detected_OCR_text.append(">>Output:\n")
            self.TextEdit_detected_OCR_text.append(result)
            self.TextEdit_detected_OCR_text.ensureCursorVisible()  # Scroll to last line
            self.controller_key_monitoring.reset_queue()

        # Auto typingrecord new button display, Convert keycode to readable format considering the enum type keys
        if self.ButtonRecordNewKey.isChecked():
            self.hotkey_start_writer_list_copy.append(key)
            ky_str = []
            for key in self.hotkey_start_writer_list_copy:
                try:
                    ky_str.append(key.name)
                except AttributeError:
                    ky_str.append(key)
            self.LineCurrentInputKey.setText(str(ky_str))
            self.controller_key_monitoring.reset_queue()

        # OCR record new button display

        if self.ButtonRecordNewKey_OCR.isChecked():
            self.hotkey_start_ocr_list.append(key)
            ky_str = []
            for key in self.hotkey_start_ocr_list:
                try:
                    ky_str.append(key.name)
                except AttributeError:
                    ky_str.append(key)
            self.LineCurrentInputKey_OCR.setText(str(ky_str))
            self.controller_key_monitoring.reset_queue()

    def detect_on_release(self, key):  # TODO Seperate thread to counteract freezing!
        pass

    def detect_mouse_click(self, x, y, button, pressed):
        if pressed:
            self.controller_writing.click_detected()
            logging.debug("Mouse clicked")
        elif not pressed:
            pass

    def reset_hotkeys(self):
        if self.ButtonRecordNewKey.isChecked():  # Only on down press
            self.hotkey_start_writer_list_copy = []
            self.LineCurrentInputKey.setText("")

    def reset_hotkeys_OCR(self):
        if self.ButtonRecordNewKey_OCR.isChecked():  # Only on down press
            self.hotkey_start_ocr_list = []
            self.LineCurrentInputKey_OCR.setText("")

    # OCR tasks

    def manual_start_ocr(self):
        result = self.OCR_handler.image_to_text()
        self.TextEdit_detected_OCR_text.append(">>Output:\n")
        self.TextEdit_detected_OCR_text.append(result)

        self.TextEdit_detected_OCR_text.ensureCursorVisible()  # Scroll to last line
        self.controller_key_monitoring.reset_queue()

    def toggle_OCR_module(self):
        if self.OCR_handler.engine_enabled is True:
            self.OCR_handler.engine_enabled = False
            self.ButtonEnable_OCR.setText("Module Disabled")
            self.ButtonEnable_OCR.setStyleSheet("QPushButton {background-color:red}")
        else:
            self.OCR_handler.engine_enabled = True
            self.ButtonEnable_OCR.setText("Module Enabled")
            self.ButtonEnable_OCR.setStyleSheet("QPushButton {background-color:green}")

    def toggle_OCR_module_auto_copy_to_clipboard(self):
        if self.OCR_handler.auto_copy_to_clipboard is True:
            self.OCR_handler.auto_copy_to_clipboard = False
            self.Button_OCR_AutoCopy.setText("Auto copy to clipboard disabled")
            self.Button_OCR_AutoCopy.setStyleSheet("QPushButton {background-color:red}")
        else:
            self.OCR_handler.auto_copy_to_clipboard = True
            self.Button_OCR_AutoCopy.setText("Auto copy to clipboard enabled")
            self.Button_OCR_AutoCopy.setStyleSheet("QPushButton {background-color:green}")

    # Star writing in seperate thread

    def start_writing(self):
        if (self.controller_writing.is_running_allowed is True) and (self.writing_thread_counter < 1):
            self.writing_thread_counter = self.writing_thread_counter + 1
            print(self.writing_thread_counter)
            worker = WritingThread(self.controller_writing, pyperclip.paste())
            worker.signals.signal_writing_done.connect(self.writing_is_done)
            self.threadpool.start(worker)

    def enable_or_disable_writer(self):
        if self.controller_writing.is_running_allowed is False:
            self.controller_writing.enable_run()
            self.ButtonEnableCopy.setText("Module Enabled")
            self.ButtonEnableCopy.setStyleSheet("QPushButton {background-color:green}")
        else:
            self.controller_writing.disable_run()
            self.ButtonEnableCopy.setText("Module Disabled")
            self.ButtonEnableCopy.setStyleSheet("QPushButton {background-color:red}")

    def enable_or_disable_writer_execution_after_click(self):
        if self.controller_writing.clicked_is_checked_on_run is False:
            self.controller_writing.enable_click_detection()
            self.ButtonRunOnClick.setText("Run only after click: Enabled")
            self.ButtonRunOnClick.setStyleSheet("QPushButton {background-color:green}")
        else:
            self.controller_writing.disable_click_detection()
            self.ButtonRunOnClick.setText("Run only after click: Disabled")
            self.ButtonRunOnClick.setStyleSheet("QPushButton {background-color:red}")

    def delay_slider_released(self):
        self.controller_writing.start_delay = self.SliderStartDelay.value() / 2
        if self.controller_writing.start_delay == 0:
            self.controller_writing.start_delay = 0.3  # Safety reason, mutliple calls cannot be made this way
        self.LineStartDelay.setText(str(f"{self.controller_writing.start_delay} s"))

    def writing_is_done(self):
        self.writing_thread_counter = self.writing_thread_counter - 1

    # Page select

    def select_copy_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def select_second_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def select_third_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def toogle_size(self):
        size_status = self.window_size
        if size_status is False:
            self.window_size = True
            self.showMaximized()
        else:
            self.window_size = False
            self.showNormal()

    def move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
        if event.buttons() == Qt.LeftButton:
            logging.debug("Mouse click inside APP: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            logging.debug("Mouse click inside APP: RIGHT CLICK")

    def close_app(self, *args, **kwargs):
        print("\nProgram closed, killing all threads!\n\n")
        # TODO kill all threads
        sys.exit()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
