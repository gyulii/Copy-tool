# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sidepanel = QWidget(self.centralwidget)
        self.sidepanel.setObjectName(u"sidepanel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidepanel.sizePolicy().hasHeightForWidth())
        self.sidepanel.setSizePolicy(sizePolicy)
        self.sidepanel.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.sidepanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonThirdPage = QPushButton(self.sidepanel)
        self.ButtonThirdPage.setObjectName(u"ButtonThirdPage")

        self.gridLayout.addWidget(self.ButtonThirdPage, 2, 0, 1, 1)

        self.ButtonCopyPageSelect = QPushButton(self.sidepanel)
        self.ButtonCopyPageSelect.setObjectName(u"ButtonCopyPageSelect")

        self.gridLayout.addWidget(self.ButtonCopyPageSelect, 0, 0, 1, 1)

        self.ButtonSecondPage = QPushButton(self.sidepanel)
        self.ButtonSecondPage.setObjectName(u"ButtonSecondPage")

        self.gridLayout.addWidget(self.ButtonSecondPage, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.ButtonExit = QPushButton(self.sidepanel)
        self.ButtonExit.setObjectName(u"ButtonExit")

        self.gridLayout.addWidget(self.ButtonExit, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.sidepanel, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.PageCopy = QWidget()
        self.PageCopy.setObjectName(u"PageCopy")
        self.gridLayout_3 = QGridLayout(self.PageCopy)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_2 = QWidget(self.PageCopy)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ButtonEnableCopy = QPushButton(self.widget_2)
        self.ButtonEnableCopy.setObjectName(u"ButtonEnableCopy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ButtonEnableCopy.sizePolicy().hasHeightForWidth())
        self.ButtonEnableCopy.setSizePolicy(sizePolicy1)
        self.ButtonEnableCopy.setStyleSheet(u"background-color: red;")
        self.ButtonEnableCopy.setCheckable(False)

        self.verticalLayout_2.addWidget(self.ButtonEnableCopy)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.LabelStartDelay = QLabel(self.widget)
        self.LabelStartDelay.setObjectName(u"LabelStartDelay")
        self.LabelStartDelay.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.LabelStartDelay.setWordWrap(False)
        self.LabelStartDelay.setIndent(-1)

        self.gridLayout_4.addWidget(self.LabelStartDelay, 0, 0, 1, 1)

        self.LabelInputKey = QLabel(self.widget)
        self.LabelInputKey.setObjectName(u"LabelInputKey")

        self.gridLayout_4.addWidget(self.LabelInputKey, 2, 0, 1, 1)

        self.LineCurrentInputKey = QLineEdit(self.widget)
        self.LineCurrentInputKey.setObjectName(u"LineCurrentInputKey")

        self.gridLayout_4.addWidget(self.LineCurrentInputKey, 2, 1, 1, 1)

        self.ButtonRecordNewKey = QPushButton(self.widget)
        self.ButtonRecordNewKey.setObjectName(u"ButtonRecordNewKey")
        self.ButtonRecordNewKey.setCheckable(True)

        self.gridLayout_4.addWidget(self.ButtonRecordNewKey, 2, 2, 1, 1)

        self.LineStartDelay = QLineEdit(self.widget)
        self.LineStartDelay.setObjectName(u"LineStartDelay")

        self.gridLayout_4.addWidget(self.LineStartDelay, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.SliderStartDelay = QSlider(self.widget)
        self.SliderStartDelay.setObjectName(u"SliderStartDelay")
        self.SliderStartDelay.setMaximum(10)
        self.SliderStartDelay.setSingleStep(1)
        self.SliderStartDelay.setPageStep(2)
        self.SliderStartDelay.setOrientation(Qt.Horizontal)
        self.SliderStartDelay.setTickPosition(QSlider.NoTicks)

        self.gridLayout_4.addWidget(self.SliderStartDelay, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        self.ButtonRunOnClick = QPushButton(self.widget_2)
        self.ButtonRunOnClick.setObjectName(u"ButtonRunOnClick")
        self.ButtonRunOnClick.setStyleSheet(u"background-color: green;")

        self.verticalLayout_2.addWidget(self.ButtonRunOnClick)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.TextFieldClipboard = QTextEdit(self.widget_4)
        self.TextFieldClipboard.setObjectName(u"TextFieldClipboard")

        self.verticalLayout_3.addWidget(self.TextFieldClipboard)

        self.ButtonManulaStart = QPushButton(self.widget_4)
        self.ButtonManulaStart.setObjectName(u"ButtonManulaStart")

        self.verticalLayout_3.addWidget(self.ButtonManulaStart)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageCopy)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(500, 16777215))

        self.verticalLayout.addWidget(self.lineEdit)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ButtonThirdPage.setText(QCoreApplication.translate("MainWindow", u"Coming soon", None))
        self.ButtonCopyPageSelect.setText(QCoreApplication.translate("MainWindow", u"Copy to VM", None))
        self.ButtonSecondPage.setText(QCoreApplication.translate("MainWindow", u"Coming soon", None))
        self.ButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.ButtonEnableCopy.setText(QCoreApplication.translate("MainWindow", u"Module Disabled", None))
        self.LabelStartDelay.setText(QCoreApplication.translate("MainWindow", u"Start delay:", None))
        self.LabelInputKey.setText(QCoreApplication.translate("MainWindow", u"Current input key:", None))
        self.ButtonRecordNewKey.setText(QCoreApplication.translate("MainWindow", u"Record new input key", None))
        self.LineStartDelay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ButtonRunOnClick.setText(QCoreApplication.translate("MainWindow", u"Run only after click: Enabled", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Content to be inserted:", None))
        self.ButtonManulaStart.setText(QCoreApplication.translate("MainWindow", u"Manual start", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Page2", None))
    # retranslateUi

