import sys

from MainWindow import Ui_MainWindow
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


class MainWindow(QMainWindow, Ui_MainWindow):
    
    
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.ButtonCopyPageSelect.clicked.connect(self.select_copy_page)
        self.pushButton_7.clicked.connect(self.select_second_page)
        self.ButtonExit.clicked.connect(self.close_app)
            
    
    
    
    
    
    
    
    
    
    
    
        
    def select_copy_page(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def select_second_page(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def close_app(self, *args, **kwargs):
        print("\nProgram closed, killing all threads!\n\n")
        #TODO kill all threads
        sys.exit()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()