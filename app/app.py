import sys
import time

from key_register import KeyRegister
from MainWindow import Ui_MainWindow
from pynput import keyboard
from PySide6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

# import PySide6 before matplotlib
from PySide6.QtCore import (
    QAbstractListModel,
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


class WritingThread(QRunnable):
    def __init__(self, Writer: Writer, input_text: str) -> None:
        super().__init__()

        self.WritingController = Writer
        self.WritingController.load_text(input_text)
        self.signal_writing_done = Signal(bool)

    @Slot()
    def run(self):
        self.WritingController.run()  # TODO: If disabled, prompt enable


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
        self.ButtonManulaStart.clicked.connect(self.start_writing)

        # Start key detection thread

        self.controller_key_monitoring = KeyRegister(on_press_fn=self.detect_on_press, on_release_fn=self.detect_on_release)  
        self.hotkey_start_writer =  [keyboard.Key.caps_lock,keyboard.Key.caps_lock,keyboard.Key.caps_lock,keyboard.Key.caps_lock]
        
        #Record new hotkey
        
        ky_str = [i.name for i in self.hotkey_start_writer] # Weird naming + 2 steps, otherwise WinDefender starts to cry
        self.LineCurrentInputKey.setText(str(ky_str))
    
        self.ButtonRecordNewKey.toggled.connect(self.reset_hotkeys)
    
    # KeyPress detection

    def detect_on_press(self, key):  # TODO Seperate thread to counteract freezing!
        self.controller_key_monitoring.add_new_input_key_to_queue(key)

        
        if self.controller_key_monitoring.check_queue_to_keycombination(self.hotkey_start_writer) is True and self.ButtonRecordNewKey.isChecked() is False:
            print("Do stuff")
            
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


    def reset_hotkeys(self):
        if self.ButtonRecordNewKey.isChecked():         # Only on down press
            self.hotkey_start_writer = []
            self.LineCurrentInputKey.setText("")

    # Star writing in seperate thread

    def start_writing(self):
        worker = WritingThread(self.controller_writing, "Szia Orsi")  # TODO: Copy from clipboard or input field
        self.threadpool.start(worker)

    def enable_or_disable_writer(self):
        if self.controller_writing.is_running_allowed is False:
            self.controller_writing.enable_run()
            self.ButtonEnableCopy.setText("Enabled")
            self.ButtonEnableCopy.setStyleSheet("QPushButton {background-color:green}")
        else:
            self.controller_writing.disable_run()
            self.ButtonEnableCopy.setText("Disabled")
            self.ButtonEnableCopy.setStyleSheet("QPushButton {background-color:red}")

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
