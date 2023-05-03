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
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 596)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*  White text */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/*  No tooltip*/\n"
"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"#backgroundwidget {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#PageCopy {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }"
                        "\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left"
                        ";\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
" "
                        "    subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    "
                        "background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"\n"
"#stackedWidget QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72"
                        ");\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#stackedWidget QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#stackedWidget QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"#QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"#QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"\n"
"QTextEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"#QTextEdit:hover {\n"
"	border: 2px sol"
                        "id rgb(64, 71, 88);\n"
"}\n"
"#QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"#sidepanel QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#sidepanel QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#sidepanel QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#topPart .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#topPart .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#topPart .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.backgroundwidget = QWidget(self.centralwidget)
        self.backgroundwidget.setObjectName(u"backgroundwidget")
        self.verticalLayout_5 = QVBoxLayout(self.backgroundwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.topPart = QWidget(self.backgroundwidget)
        self.topPart.setObjectName(u"topPart")
        self.topPart.setMinimumSize(QSize(0, 50))
        self.topPart.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.topPart)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topLeft = QWidget(self.topPart)
        self.topLeft.setObjectName(u"topLeft")
        self.verticalLayout_6 = QVBoxLayout(self.topLeft)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.topLeft)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.topLeft)

        self.topMiddle = QWidget(self.topPart)
        self.topMiddle.setObjectName(u"topMiddle")
        self.horizontalLayout_5 = QHBoxLayout(self.topMiddle)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label = QLabel(self.topMiddle)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.topMiddle)

        self.topRight = QWidget(self.topPart)
        self.topRight.setObjectName(u"topRight")
        self.horizontalLayout_4 = QHBoxLayout(self.topRight)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ButtonMinimalize = QPushButton(self.topRight)
        self.ButtonMinimalize.setObjectName(u"ButtonMinimalize")
        self.ButtonMinimalize.setMinimumSize(QSize(25, 25))
        self.ButtonMinimalize.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonMinimalize.setIcon(icon)
        self.ButtonMinimalize.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.ButtonMinimalize)

        self.ButtonChangeWindowSize = QPushButton(self.topRight)
        self.ButtonChangeWindowSize.setObjectName(u"ButtonChangeWindowSize")
        self.ButtonChangeWindowSize.setMinimumSize(QSize(25, 25))
        self.ButtonChangeWindowSize.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/icon_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonChangeWindowSize.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.ButtonChangeWindowSize)

        self.ButtonExitTop = QPushButton(self.topRight)
        self.ButtonExitTop.setObjectName(u"ButtonExitTop")
        self.ButtonExitTop.setMinimumSize(QSize(25, 25))
        self.ButtonExitTop.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonExitTop.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.ButtonExitTop)


        self.horizontalLayout_2.addWidget(self.topRight)


        self.verticalLayout_5.addWidget(self.topPart)

        self.bottomPart = QWidget(self.backgroundwidget)
        self.bottomPart.setObjectName(u"bottomPart")
        self.horizontalLayout_3 = QHBoxLayout(self.bottomPart)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sidepanel = QWidget(self.bottomPart)
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


        self.horizontalLayout_3.addWidget(self.sidepanel)

        self.mainpanel = QWidget(self.bottomPart)
        self.mainpanel.setObjectName(u"mainpanel")
        self.horizontalLayout = QHBoxLayout(self.mainpanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.mainpanel)
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

        self.verticalLayout_2.addWidget(self.widget_4)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageCopy)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_5 = QPushButton(self.widget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.mainpanel)


        self.verticalLayout_5.addWidget(self.bottomPart)


        self.verticalLayout_4.addWidget(self.backgroundwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.ButtonMinimalize.setText("")
        self.ButtonChangeWindowSize.setText("")
        self.ButtonExitTop.setText("")
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
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

