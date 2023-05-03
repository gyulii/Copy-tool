import sys
import time

import logging
import pyperclip


logging.basicConfig(format='%(levelname)s-%(asctime)s - %(message)s', datefmt='%H:%M:%S' , level=logging.DEBUG)



from key_register import KeyRegister
from MainWindow import Ui_MainWindow
from mouse_handler import MouseHandler
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
    QVBoxLayout,
    QWidget,
)
from writer import Writer


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

        # Button mapping

        self.ButtonCopyPageSelect.clicked.connect(self.select_copy_page)
        self.ButtonSecondPage.clicked.connect(self.select_second_page)
        self.ButtonExit.clicked.connect(self.close_app)
        self.ButtonEnableCopy.clicked.connect(self.enable_or_disable_writer)
        

        # Writer mapping and creation

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.controller_writing = Writer(input_text="Hi this is the default text")  # TODO: Copy from Clipboard
        self.writing_thread_counter = 0
        
        
        self.ButtonManulaStart.clicked.connect(self.start_writing)
        self.LineStartDelay.setText(f"{str(self.controller_writing.start_delay)} s")
        self.LineStartDelay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.SliderStartDelay.setValue(int(self.controller_writing.start_delay * 2))
        self.SliderStartDelay.sliderReleased.connect(self.delay_slider_released)
        self.ButtonRunOnClick.clicked.connect(self.enable_or_disable_writer_execution_after_click)        

        # Start key detection thread

        self.controller_key_monitoring = KeyRegister(on_press_fn=self.detect_on_press, on_release_fn=self.detect_on_release)  
        self.hotkey_start_writer =  [keyboard.Key.caps_lock,keyboard.Key.caps_lock,keyboard.Key.caps_lock,keyboard.Key.caps_lock]
        
        #Record new hotkey
        
        ky_str = [i.name for i in self.hotkey_start_writer] # Weird naming + 2 steps, otherwise WinDefender starts to cry
        self.LineCurrentInputKey.setText(str(ky_str))
    
        self.ButtonRecordNewKey.toggled.connect(self.reset_hotkeys)
        
        
        # Mouse handling
        
        self.mouse_handler = MouseHandler(on_click_fn=self.detect_mouse_click)
    
    # KeyPress detection

    def detect_on_press(self, key):  # TODO Seperate thread to counteract freezing!
        self.controller_key_monitoring.add_new_input_key_to_queue(key)
        logging.debug(f"{key} pressed")
        
        
        if key == keyboard.Key.esc:
            self.controller_writing.interrupt_execution()
        
        if self.controller_key_monitoring.check_queue_to_keycombination(self.hotkey_start_writer) is True and self.ButtonRecordNewKey.isChecked() is False:
            print("Starting task")
            self.start_writing()
            self.controller_key_monitoring.reset_queue() #Reset input sequence 
            
        # Convert keycode to redable format considering the enum type keys  
        if self.ButtonRecordNewKey.isChecked():
            self.hotkey_start_writer.append(key)
            ky_str = []
            for key in self.hotkey_start_writer:
                try:
                    ky_str.append(key.name)
                except AttributeError:
                    ky_str.append(key)
            self.LineCurrentInputKey.setText(str(ky_str))
            self.controller_key_monitoring.reset_queue()

    def detect_on_release(self, key):  # TODO Seperate thread to counteract freezing!
        pass


    def detect_mouse_click(self, x, y, button, pressed):
        if pressed:
            self.controller_writing.click_detected() 
            logging.debug('Mouse clicked')
        elif(not pressed):
            pass
            



    def reset_hotkeys(self):
        if self.ButtonRecordNewKey.isChecked():         # Only on down press
            self.hotkey_start_writer = []
            self.LineCurrentInputKey.setText("")

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
        if(self.controller_writing.start_delay == 0):
            self.controller_writing.start_delay = 0.3  # Safety reason, mutliple calls cannot be made this way
        self.LineStartDelay.setText(str(f"{self.controller_writing.start_delay} s"))
        
    def writing_is_done(self):
        self.writing_thread_counter = self.writing_thread_counter - 1
    
    # Page select

    def select_copy_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def select_second_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def close_app(self, *args, **kwargs):
        print("\nProgram closed, killing all threads!\n\n")
        # TODO kill all threads
        sys.exit()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
