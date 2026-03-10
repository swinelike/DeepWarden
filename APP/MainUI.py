from toggle import CustomToggle
from threading import Thread
import os
import json
import keyboard
import threading
import assets_rc  # noqa: F401
from time import sleep
from pyqttoast import Toast, ToastPreset
#pyside6 imports
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt, QStandardPaths)
from PySide6.QtGui import (QFont, QIcon, QColor)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(750, 800)
        MainWindow.setMinimumSize(QSize(750, 800))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.titleBar = QFrame(self.centralwidget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMinimumSize(QSize(0, 50))
        self.titleBar.setMaximumSize(QSize(16777215, 50))
        self.titleBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.titleBar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.pageName = QLabel(self.titleBar)
        self.pageName.setObjectName(u"pageName")

        self.gridLayout_2.addWidget(self.pageName, 0, 3, 1, 1)

        self.menuButton = QPushButton(self.titleBar)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(50, 50))
        self.menuButton.setMaximumSize(QSize(50, 50))
        self.menuButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/icons/menu_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(50, 50))
        self.menuButton.setFlat(True)

        self.gridLayout_2.addWidget(self.menuButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addWidget(self.titleBar, 0, 0, 1, 2)

        self.container = QWidget(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(200, 50))
        self.container.setStyleSheet(u"")
        self.gridLayout_24 = QGridLayout(self.container)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(9)
        self.gridLayout_24.setVerticalSpacing(3)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(600, 600))
        self.stackedWidget.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"}\n"
"")
        self.bellPage = QWidget()
        self.bellPage.setObjectName(u"bellPage")
        self.gridLayout_5 = QGridLayout(self.bellPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.BellMovestack = QLabel(self.bellPage)
        self.BellMovestack.setObjectName(u"BellMovestack")

        self.gridLayout_5.addWidget(self.BellMovestack, 0, 0, 1, 2)

        self.MovestackChoice = QComboBox(self.bellPage)
        self.MovestackChoice.addItem("")
        self.MovestackChoice.addItem("")
        self.MovestackChoice.setObjectName(u"MovestackChoice")

        self.gridLayout_5.addWidget(self.MovestackChoice, 2, 0, 1, 1)

        self.label_40 = QLabel(self.bellPage)
        self.label_40.setObjectName(u"label_40")
        font = QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"color:grey;")

        self.gridLayout_5.addWidget(self.label_40, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.bellPage)
        self.mantrasPage = QWidget()
        self.mantrasPage.setObjectName(u"mantrasPage")
        self.gridLayout_6 = QGridLayout(self.mantrasPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AutoMantraVariantsDescriptor = QLabel(self.mantrasPage)
        self.AutoMantraVariantsDescriptor.setObjectName(u"AutoMantraVariantsDescriptor")
        self.AutoMantraVariantsDescriptor.setFont(font)
        self.AutoMantraVariantsDescriptor.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.AutoMantraVariantsDescriptor, 6, 0, 1, 2)

        self.label_47 = QLabel(self.mantrasPage)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.label_47, 12, 0, 1, 2)

        self.plainTextEdit_10 = QPlainTextEdit(self.mantrasPage)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_10.setStyleSheet(u"")
        self.plainTextEdit_10.setMaximumBlockCount(1)

        self.gridLayout_6.addWidget(self.plainTextEdit_10, 2, 1, 1, 1)

        self.AutoMantraVariants = QLabel(self.mantrasPage)
        self.AutoMantraVariants.setObjectName(u"AutoMantraVariants")

        self.gridLayout_6.addWidget(self.AutoMantraVariants, 5, 0, 1, 1)

        self.label_21 = QLabel(self.mantrasPage)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 16, 0, 1, 2)

        self.AutoMantraVariantsKeysLabel = QLabel(self.mantrasPage)
        self.AutoMantraVariantsKeysLabel.setObjectName(u"AutoMantraVariantsKeysLabel")

        self.gridLayout_6.addWidget(self.AutoMantraVariantsKeysLabel, 7, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.mantrasPage)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_3.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_3.setStyleSheet(u"")
        self.plainTextEdit_3.setMaximumBlockCount(1)

        self.gridLayout_6.addWidget(self.plainTextEdit_3, 13, 1, 1, 1)

        self.label_8 = QLabel(self.mantrasPage)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 10, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.mantrasPage)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_2.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_2.setStyleSheet(u"")
        self.plainTextEdit_2.setMaximumBlockCount(1)

        self.gridLayout_6.addWidget(self.plainTextEdit_2, 10, 1, 1, 1)

        self.label_39 = QLabel(self.mantrasPage)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 3, 0, 1, 1)

        self.AutoMantraVariantsKeysArea = QPlainTextEdit(self.mantrasPage)
        self.AutoMantraVariantsKeysArea.setObjectName(u"AutoMantraVariantsKeysArea")
        self.AutoMantraVariantsKeysArea.setMinimumSize(QSize(0, 30))
        self.AutoMantraVariantsKeysArea.setMaximumSize(QSize(16777215, 30))
        self.AutoMantraVariantsKeysArea.setStyleSheet(u"")
        self.AutoMantraVariantsKeysArea.setMaximumBlockCount(1)

        self.gridLayout_6.addWidget(self.AutoMantraVariantsKeysArea, 7, 1, 1, 1)

        self.label_46 = QLabel(self.mantrasPage)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.label_46, 9, 0, 1, 2)

        self.AutoRitualCast = QLabel(self.mantrasPage)
        self.AutoRitualCast.setObjectName(u"AutoRitualCast")

        self.gridLayout_6.addWidget(self.AutoRitualCast, 0, 0, 1, 1)

        self.label_7 = QLabel(self.mantrasPage)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_10 = QLabel(self.mantrasPage)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 13, 0, 1, 1)

        self.label_20 = QLabel(self.mantrasPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color:grey;")

        self.gridLayout_6.addWidget(self.label_20, 1, 0, 1, 2)

        self.label_9 = QLabel(self.mantrasPage)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 11, 0, 1, 1)

        self.label_44 = QLabel(self.mantrasPage)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_6.addWidget(self.label_44, 4, 0, 1, 1)

        self.screenResolution = QComboBox(self.mantrasPage)
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.addItem("")
        self.screenResolution.setObjectName(u"screenResolution")

        self.gridLayout_6.addWidget(self.screenResolution, 3, 1, 1, 1)

        self.screenScale = QComboBox(self.mantrasPage)
        self.screenScale.addItem("")
        self.screenScale.addItem("")
        self.screenScale.setObjectName(u"screenScale")

        self.gridLayout_6.addWidget(self.screenScale, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.mantrasPage)
        self.weaponsPage = QWidget()
        self.weaponsPage.setObjectName(u"weaponsPage")
        self.weaponsPage.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.weaponsPage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.weaponsPage)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"}\n"
"")
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -349, 657, 1038))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.MotifHotkeyLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.MotifHotkeyLabel.setObjectName(u"MotifHotkeyLabel")

        self.gridLayout_19.addWidget(self.MotifHotkeyLabel, 7, 0, 1, 1)

        self.label_83 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_19.addWidget(self.label_83, 19, 0, 1, 1)

        self.HoldM1Key = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.HoldM1Key.setObjectName(u"HoldM1Key")
        self.HoldM1Key.setMinimumSize(QSize(0, 30))
        self.HoldM1Key.setMaximumSize(QSize(16777215, 30))
        self.HoldM1Key.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.HoldM1Key, 4, 1, 1, 1)

        self.label_115 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_19.addWidget(self.label_115, 27, 0, 1, 1)

        self.label_86 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_19.addWidget(self.label_86, 22, 0, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color:grey;")
        self.label_11.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_11, 1, 0, 1, 2)

        self.label_141 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_141, 26, 0, 1, 2)

        self.uppercutAssassinateHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.uppercutAssassinateHotkey.setObjectName(u"uppercutAssassinateHotkey")
        self.uppercutAssassinateHotkey.setMaximumSize(QSize(16777215, 30))
        self.uppercutAssassinateHotkey.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.uppercutAssassinateHotkey, 27, 1, 1, 1)

        self.label_85 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_85, 21, 0, 1, 2)

        self.label_82 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_82, 18, 0, 1, 2)

        self.rollParryHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.rollParryHotkey.setObjectName(u"rollParryHotkey")
        self.rollParryHotkey.setMaximumSize(QSize(16777215, 30))
        self.rollParryHotkey.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.rollParryHotkey, 24, 1, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_19.addWidget(self.label_22, 4, 0, 1, 1)

        self.HoldM1Label = QLabel(self.scrollAreaWidgetContents_3)
        self.HoldM1Label.setObjectName(u"HoldM1Label")

        self.gridLayout_19.addWidget(self.HoldM1Label, 2, 0, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_19.addWidget(self.label_18, 15, 0, 1, 1)

        self.MotifToolbarNumberLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.MotifToolbarNumberLabel.setObjectName(u"MotifToolbarNumberLabel")

        self.gridLayout_19.addWidget(self.MotifToolbarNumberLabel, 8, 0, 1, 1)

        self.uppercutAssassinateLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.uppercutAssassinateLabel.setObjectName(u"uppercutAssassinateLabel")

        self.gridLayout_19.addWidget(self.uppercutAssassinateLabel, 25, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:grey")
        self.label_2.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_2, 3, 0, 1, 2)

        self.label_89 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_19.addWidget(self.label_89, 14, 0, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_36, 13, 0, 1, 2)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_19.addWidget(self.label_23, 10, 0, 1, 1)

        self.plainTextEdit_7 = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_7.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_7.setStyleSheet(u"")
        self.plainTextEdit_7.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.plainTextEdit_7, 9, 1, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_19, 16, 0, 1, 1)

        self.RollM1Hotkey = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.RollM1Hotkey.setObjectName(u"RollM1Hotkey")
        self.RollM1Hotkey.setMaximumSize(QSize(16777215, 30))
        self.RollM1Hotkey.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.RollM1Hotkey, 19, 1, 1, 1)

        self.label_81 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_19.addWidget(self.label_81, 17, 0, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_19.addWidget(self.label_35, 12, 0, 1, 1)

        self.label_88 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_19.addWidget(self.label_88, 24, 0, 1, 1)

        self.label_84 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_19.addWidget(self.label_84, 20, 0, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_24, 11, 0, 1, 2)

        self.MotifToolbarNumberArea = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.MotifToolbarNumberArea.setObjectName(u"MotifToolbarNumberArea")
        self.MotifToolbarNumberArea.setMinimumSize(QSize(0, 30))
        self.MotifToolbarNumberArea.setMaximumSize(QSize(16777215, 30))
        self.MotifToolbarNumberArea.setStyleSheet(u"")
        self.MotifToolbarNumberArea.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.MotifToolbarNumberArea, 8, 1, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color:grey;")
        self.label_12.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_12, 6, 0, 1, 2)

        self.AerialAirDashLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.AerialAirDashLabel.setObjectName(u"AerialAirDashLabel")

        self.gridLayout_19.addWidget(self.AerialAirDashLabel, 0, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_19.addWidget(self.label_16, 9, 0, 1, 1)

        self.MotifSwapLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.MotifSwapLabel.setObjectName(u"MotifSwapLabel")

        self.gridLayout_19.addWidget(self.MotifSwapLabel, 5, 0, 1, 1)

        self.label_87 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_87, 23, 0, 1, 2)

        self.label_140 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_19.addWidget(self.label_140, 28, 0, 1, 1)

        self.MotifHotkeyArea = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.MotifHotkeyArea.setObjectName(u"MotifHotkeyArea")
        self.MotifHotkeyArea.setMinimumSize(QSize(0, 30))
        self.MotifHotkeyArea.setMaximumSize(QSize(16777215, 30))
        self.MotifHotkeyArea.setStyleSheet(u"")
        self.MotifHotkeyArea.setMaximumBlockCount(1)

        self.gridLayout_19.addWidget(self.MotifHotkeyArea, 7, 1, 1, 1)

        self.label_142 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setStyleSheet(u"color:grey;")

        self.gridLayout_19.addWidget(self.label_142, 29, 0, 1, 2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_10.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.weaponsPage)
        self.progressionPage = QWidget()
        self.progressionPage.setObjectName(u"progressionPage")
        self.progressionPage.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"}\n"
"")
        self.gridLayout_12 = QGridLayout(self.progressionPage)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.progressionPage)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"}\n"
"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, -659, 657, 1348))
        self.gridLayout_21 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_117 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_21.addWidget(self.label_117, 14, 0, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color:grey;")

        self.gridLayout_21.addWidget(self.label_27, 3, 0, 1, 2)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"color:grey;")

        self.gridLayout_21.addWidget(self.label_28, 6, 0, 1, 2)

        self.AutoDropNotesBarStartCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesBarStartCoordsButton.setObjectName(u"AutoDropNotesBarStartCoordsButton")

        self.gridLayout_21.addWidget(self.AutoDropNotesBarStartCoordsButton, 27, 0, 1, 2)

        self.label_120 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_120.setObjectName(u"label_120")

        self.gridLayout_21.addWidget(self.label_120, 28, 0, 1, 1)

        self.AutoSellLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.AutoSellLabel.setObjectName(u"AutoSellLabel")

        self.gridLayout_21.addWidget(self.AutoSellLabel, 32, 0, 1, 1)

        self.label_124 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_21.addWidget(self.label_124, 38, 0, 1, 1)

        self.AutoBuySubmitCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoBuySubmitCoords.setObjectName(u"AutoBuySubmitCoords")
        self.AutoBuySubmitCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoBuySubmitCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoBuySubmitCoords, 18, 1, 1, 1)

        self.AutoDropNotesHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesHotkey.setObjectName(u"AutoDropNotesHotkey")
        self.AutoDropNotesHotkey.setMaximumSize(QSize(16777215, 30))
        self.AutoDropNotesHotkey.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoDropNotesHotkey, 22, 1, 1, 1)

        self.AutoSellBarEndCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoSellBarEndCoords.setObjectName(u"AutoSellBarEndCoords")
        self.AutoSellBarEndCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoSellBarEndCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoSellBarEndCoords, 38, 1, 1, 1)

        self.label_114 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_21.addWidget(self.label_114, 23, 0, 1, 1)

        self.label_127 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setStyleSheet(u"color:grey;")
        self.label_127.setWordWrap(True)

        self.gridLayout_21.addWidget(self.label_127, 33, 0, 1, 2)

        self.label_119 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setStyleSheet(u"color:grey;")

        self.gridLayout_21.addWidget(self.label_119, 12, 0, 1, 2)

        self.AutoSellRepetitions = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoSellRepetitions.setObjectName(u"AutoSellRepetitions")
        self.AutoSellRepetitions.setMaximumSize(QSize(16777215, 30))
        self.AutoSellRepetitions.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoSellRepetitions, 35, 1, 1, 1)

        self.WillpowerTrainingHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.WillpowerTrainingHotkey.setObjectName(u"WillpowerTrainingHotkey")
        self.WillpowerTrainingHotkey.setMinimumSize(QSize(0, 30))
        self.WillpowerTrainingHotkey.setMaximumSize(QSize(16777215, 30))
        self.WillpowerTrainingHotkey.setStyleSheet(u"")
        self.WillpowerTrainingHotkey.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.WillpowerTrainingHotkey, 10, 1, 1, 1)

        self.AnkleWeightsTrainingHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AnkleWeightsTrainingHotkey.setObjectName(u"AnkleWeightsTrainingHotkey")
        self.AnkleWeightsTrainingHotkey.setMinimumSize(QSize(0, 30))
        self.AnkleWeightsTrainingHotkey.setMaximumSize(QSize(16777215, 30))
        self.AnkleWeightsTrainingHotkey.setStyleSheet(u"")
        self.AnkleWeightsTrainingHotkey.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AnkleWeightsTrainingHotkey, 4, 1, 1, 1)

        self.AutoDropNotesLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesLabel.setObjectName(u"AutoDropNotesLabel")

        self.gridLayout_21.addWidget(self.AutoDropNotesLabel, 20, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_21.addWidget(self.label_30, 10, 0, 1, 1)

        self.label_126 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_126.setObjectName(u"label_126")

        self.gridLayout_21.addWidget(self.label_126, 36, 0, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_21.addWidget(self.label_25, 4, 0, 1, 1)

        self.AutoSellHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoSellHotkey.setObjectName(u"AutoSellHotkey")
        self.AutoSellHotkey.setMaximumSize(QSize(16777215, 30))
        self.AutoSellHotkey.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoSellHotkey, 34, 1, 1, 1)

        self.AutoBuyBarStartCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoBuyBarStartCoords.setObjectName(u"AutoBuyBarStartCoords")
        self.AutoBuyBarStartCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoBuyBarStartCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoBuyBarStartCoords, 14, 1, 1, 1)

        self.AnkleWeightsLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.AnkleWeightsLabel.setObjectName(u"AnkleWeightsLabel")

        self.gridLayout_21.addWidget(self.AnkleWeightsLabel, 2, 0, 1, 1)

        self.AutoSellBarStartCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoSellBarStartCoords.setObjectName(u"AutoSellBarStartCoords")
        self.AutoSellBarStartCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoSellBarStartCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoSellBarStartCoords, 36, 1, 1, 1)

        self.AutoBuyBarEndCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoBuyBarEndCoordsButton.setObjectName(u"AutoBuyBarEndCoordsButton")

        self.gridLayout_21.addWidget(self.AutoBuyBarEndCoordsButton, 17, 0, 1, 2)

        self.label_139 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_21.addWidget(self.label_139, 18, 0, 1, 1)

        self.AutoSellBarEndCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoSellBarEndCoordsButton.setObjectName(u"AutoSellBarEndCoordsButton")

        self.gridLayout_21.addWidget(self.AutoSellBarEndCoordsButton, 39, 0, 1, 2)

        self.AutoBuyBarEndCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoBuyBarEndCoords.setObjectName(u"AutoBuyBarEndCoords")
        self.AutoBuyBarEndCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoBuyBarEndCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoBuyBarEndCoords, 16, 1, 1, 1)

        self.AutoDropNotesSubmitCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesSubmitCoords.setObjectName(u"AutoDropNotesSubmitCoords")
        self.AutoDropNotesSubmitCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoDropNotesSubmitCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoDropNotesSubmitCoords, 30, 1, 1, 1)

        self.CharismaAutofillLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.CharismaAutofillLabel.setObjectName(u"CharismaAutofillLabel")

        self.gridLayout_21.addWidget(self.CharismaAutofillLabel, 0, 0, 1, 1)

        self.label_130 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_130.setObjectName(u"label_130")

        self.gridLayout_21.addWidget(self.label_130, 30, 0, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_21.addWidget(self.label_26, 7, 0, 1, 1)

        self.AutoDropNotesRepetitions = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesRepetitions.setObjectName(u"AutoDropNotesRepetitions")
        self.AutoDropNotesRepetitions.setMaximumSize(QSize(16777215, 30))
        self.AutoDropNotesRepetitions.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoDropNotesRepetitions, 23, 1, 1, 1)

        self.label_123 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_123.setObjectName(u"label_123")

        self.gridLayout_21.addWidget(self.label_123, 22, 0, 1, 1)

        self.autoSellBarStartCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.autoSellBarStartCoordsButton.setObjectName(u"autoSellBarStartCoordsButton")

        self.gridLayout_21.addWidget(self.autoSellBarStartCoordsButton, 37, 0, 1, 2)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color:grey;")

        self.gridLayout_21.addWidget(self.label_13, 1, 0, 1, 2)

        self.autoDropNotesNoteCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.autoDropNotesNoteCoords.setObjectName(u"autoDropNotesNoteCoords")
        self.autoDropNotesNoteCoords.setMinimumSize(QSize(0, 30))
        self.autoDropNotesNoteCoords.setMaximumSize(QSize(16777215, 30))
        self.autoDropNotesNoteCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.autoDropNotesNoteCoords, 24, 1, 1, 1)

        self.AutoDropNotesBarEndCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesBarEndCoordsButton.setObjectName(u"AutoDropNotesBarEndCoordsButton")

        self.gridLayout_21.addWidget(self.AutoDropNotesBarEndCoordsButton, 29, 0, 1, 2)

        self.AutoDropNotesBarStartCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesBarStartCoords.setObjectName(u"AutoDropNotesBarStartCoords")
        self.AutoDropNotesBarStartCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoDropNotesBarStartCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoDropNotesBarStartCoords, 26, 1, 1, 1)

        self.label_128 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_21.addWidget(self.label_128, 35, 0, 1, 1)

        self.autoDropNotesNoteCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.autoDropNotesNoteCoordsButton.setObjectName(u"autoDropNotesNoteCoordsButton")

        self.gridLayout_21.addWidget(self.autoDropNotesNoteCoordsButton, 25, 0, 1, 2)

        self.AutoDropNotesSubmitCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesSubmitCoordsButton.setObjectName(u"AutoDropNotesSubmitCoordsButton")

        self.gridLayout_21.addWidget(self.AutoDropNotesSubmitCoordsButton, 31, 0, 1, 2)

        self.AutoBuyHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoBuyHotkey.setObjectName(u"AutoBuyHotkey")
        self.AutoBuyHotkey.setMaximumSize(QSize(16777215, 30))
        self.AutoBuyHotkey.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoBuyHotkey, 13, 1, 1, 1)

        self.AutoBuyBarStartCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoBuyBarStartCoordsButton.setObjectName(u"AutoBuyBarStartCoordsButton")

        self.gridLayout_21.addWidget(self.AutoBuyBarStartCoordsButton, 15, 0, 1, 2)

        self.WillpowerTrainingLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.WillpowerTrainingLabel.setObjectName(u"WillpowerTrainingLabel")

        self.gridLayout_21.addWidget(self.WillpowerTrainingLabel, 8, 0, 1, 1)

        self.AutoDropNotesBarEndCoords = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.AutoDropNotesBarEndCoords.setObjectName(u"AutoDropNotesBarEndCoords")
        self.AutoDropNotesBarEndCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoDropNotesBarEndCoords.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.AutoDropNotesBarEndCoords, 28, 1, 1, 1)

        self.BoulderTrainingLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.BoulderTrainingLabel.setObjectName(u"BoulderTrainingLabel")

        self.gridLayout_21.addWidget(self.BoulderTrainingLabel, 5, 0, 1, 1)

        self.BoulderTrainingHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_6)
        self.BoulderTrainingHotkey.setObjectName(u"BoulderTrainingHotkey")
        self.BoulderTrainingHotkey.setMinimumSize(QSize(0, 30))
        self.BoulderTrainingHotkey.setMaximumSize(QSize(16777215, 30))
        self.BoulderTrainingHotkey.setStyleSheet(u"")
        self.BoulderTrainingHotkey.setMaximumBlockCount(1)

        self.gridLayout_21.addWidget(self.BoulderTrainingHotkey, 7, 1, 1, 1)

        self.label_129 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_129.setObjectName(u"label_129")

        self.gridLayout_21.addWidget(self.label_129, 24, 0, 1, 1)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)
        self.label_38.setStyleSheet(u"color:grey;")

        self.gridLayout_21.addWidget(self.label_38, 9, 0, 1, 2)

        self.label_121 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setStyleSheet(u"color:grey;")

        self.gridLayout_21.addWidget(self.label_121, 21, 0, 1, 2)

        self.label_122 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_122.setObjectName(u"label_122")

        self.gridLayout_21.addWidget(self.label_122, 26, 0, 1, 1)

        self.AutoBuyLabel = QLabel(self.scrollAreaWidgetContents_6)
        self.AutoBuyLabel.setObjectName(u"AutoBuyLabel")

        self.gridLayout_21.addWidget(self.AutoBuyLabel, 11, 0, 1, 1)

        self.label_118 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_118.setObjectName(u"label_118")

        self.gridLayout_21.addWidget(self.label_118, 16, 0, 1, 1)

        self.label_125 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_125.setObjectName(u"label_125")

        self.gridLayout_21.addWidget(self.label_125, 34, 0, 1, 1)

        self.label_116 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_21.addWidget(self.label_116, 13, 0, 1, 1)

        self.AutoBuySubmitCoordsButton = QPushButton(self.scrollAreaWidgetContents_6)
        self.AutoBuySubmitCoordsButton.setObjectName(u"AutoBuySubmitCoordsButton")

        self.gridLayout_21.addWidget(self.AutoBuySubmitCoordsButton, 19, 0, 1, 2)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_12.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.progressionPage)
        self.miscPage = QWidget()
        self.miscPage.setObjectName(u"miscPage")
        self.gridLayout_8 = QGridLayout(self.miscPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_2 = QScrollArea(self.miscPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea {\n"
"    border: none;\n"
"}\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -34, 639, 705))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(16777215, 16777212))
        self.gridLayout_17 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_17.addWidget(self.label_32, 5, 0, 1, 1)

        self.plainTextEdit_14 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_14.setObjectName(u"plainTextEdit_14")
        self.plainTextEdit_14.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_14.setStyleSheet(u"")
        self.plainTextEdit_14.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.plainTextEdit_14, 6, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 30))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit.setStyleSheet(u"")
        self.plainTextEdit.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.plainTextEdit, 3, 1, 1, 1)

        self.plainTextEdit_12 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_12.setStyleSheet(u"")
        self.plainTextEdit_12.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.plainTextEdit_12, 4, 1, 1, 1)

        self.label_69 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_17.addWidget(self.label_69, 16, 0, 1, 1)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_17.addWidget(self.label_33, 6, 0, 1, 1)

        self.AutoEatFoodCoords = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.AutoEatFoodCoords.setObjectName(u"AutoEatFoodCoords")
        self.AutoEatFoodCoords.setMinimumSize(QSize(0, 30))
        self.AutoEatFoodCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoEatFoodCoords.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.AutoEatFoodCoords, 18, 1, 1, 1)

        self.monitorToScreenshot = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.monitorToScreenshot.setObjectName(u"monitorToScreenshot")
        self.monitorToScreenshot.setMinimumSize(QSize(0, 30))
        self.monitorToScreenshot.setMaximumSize(QSize(16777215, 30))
        self.monitorToScreenshot.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.monitorToScreenshot, 9, 1, 1, 1)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_17.addWidget(self.label_34, 2, 0, 1, 1)

        self.label_68 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_17.addWidget(self.label_68, 15, 0, 1, 1)

        self.plainTextEdit_13 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_13.setStyleSheet(u"")
        self.plainTextEdit_13.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.plainTextEdit_13, 5, 1, 1, 1)

        self.FlashmapLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.FlashmapLabel.setObjectName(u"FlashmapLabel")
        self.FlashmapLabel.setMinimumSize(QSize(0, 35))

        self.gridLayout_17.addWidget(self.FlashmapLabel, 10, 0, 1, 1)

        self.AutoEatFoodName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.AutoEatFoodName.setObjectName(u"AutoEatFoodName")
        self.AutoEatFoodName.setMinimumSize(QSize(0, 30))
        self.AutoEatFoodName.setMaximumSize(QSize(16777215, 30))
        self.AutoEatFoodName.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.AutoEatFoodName, 15, 1, 1, 1)

        self.AutoEatFoodCoordsButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.AutoEatFoodCoordsButton.setObjectName(u"AutoEatFoodCoordsButton")

        self.gridLayout_17.addWidget(self.AutoEatFoodCoordsButton, 19, 0, 1, 2)

        self.label_70 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_17.addWidget(self.label_70, 18, 0, 1, 1)

        self.DiscordGankPingLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.DiscordGankPingLabel.setObjectName(u"DiscordGankPingLabel")

        self.gridLayout_17.addWidget(self.DiscordGankPingLabel, 0, 0, 1, 1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"color:grey;")

        self.gridLayout_17.addWidget(self.label_49, 8, 0, 1, 2)

        self.label_61 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_17.addWidget(self.label_61, 12, 0, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"color:grey;")
        self.label_48.setWordWrap(True)

        self.gridLayout_17.addWidget(self.label_48, 1, 0, 1, 2)

        self.label_72 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_17.addWidget(self.label_72, 9, 0, 1, 1)

        self.AutoEatBoxCoordsButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.AutoEatBoxCoordsButton.setObjectName(u"AutoEatBoxCoordsButton")

        self.gridLayout_17.addWidget(self.AutoEatBoxCoordsButton, 17, 0, 1, 2)

        self.plainTextEdit_15 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_15.setObjectName(u"plainTextEdit_15")
        self.plainTextEdit_15.setMinimumSize(QSize(0, 30))
        self.plainTextEdit_15.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_15.setStyleSheet(u"")
        self.plainTextEdit_15.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.plainTextEdit_15, 2, 1, 1, 1)

        self.label_67 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"color:grey;")
        self.label_67.setWordWrap(True)

        self.gridLayout_17.addWidget(self.label_67, 13, 0, 1, 2)

        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:grey;")

        self.gridLayout_17.addWidget(self.label, 11, 0, 1, 2)

        self.DiscordGankPingSettings = QLabel(self.scrollAreaWidgetContents_2)
        self.DiscordGankPingSettings.setObjectName(u"DiscordGankPingSettings")

        self.gridLayout_17.addWidget(self.DiscordGankPingSettings, 3, 0, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_17.addWidget(self.label_31, 7, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_17.addWidget(self.label_29, 4, 0, 1, 1)

        self.AutoEatHotkey = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.AutoEatHotkey.setObjectName(u"AutoEatHotkey")
        self.AutoEatHotkey.setMinimumSize(QSize(0, 30))
        self.AutoEatHotkey.setMaximumSize(QSize(16777215, 30))
        self.AutoEatHotkey.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.AutoEatHotkey, 14, 1, 1, 1)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_17.addWidget(self.label_71, 14, 0, 1, 1)

        self.AutoEatBoxCoords = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.AutoEatBoxCoords.setObjectName(u"AutoEatBoxCoords")
        self.AutoEatBoxCoords.setMinimumSize(QSize(0, 30))
        self.AutoEatBoxCoords.setMaximumSize(QSize(16777215, 30))
        self.AutoEatBoxCoords.setMaximumBlockCount(1)

        self.gridLayout_17.addWidget(self.AutoEatBoxCoords, 16, 1, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_8.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.miscPage)
        self.movementPage = QWidget()
        self.movementPage.setObjectName(u"movementPage")
        self.gridLayout_11 = QGridLayout(self.movementPage)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.movementPage)
        self.savePage = QWidget()
        self.savePage.setObjectName(u"savePage")
        self.savePage.setEnabled(True)
        self.gridLayout_13 = QGridLayout(self.savePage)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_2 = QFrame(self.savePage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 400))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 647, 601))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_6, 3, 2, 1, 1)

        self.Preset10Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset10Name.setObjectName(u"Preset10Name")
        self.Preset10Name.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Preset10Name.sizePolicy().hasHeightForWidth())
        self.Preset10Name.setSizePolicy(sizePolicy)
        self.Preset10Name.setMinimumSize(QSize(200, 0))
        self.Preset10Name.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.Preset10Name.setFont(font1)
        self.Preset10Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset10Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset10Name, 9, 1, 1, 1)

        self.Preset7Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset7Save.setObjectName(u"Preset7Save")
        self.Preset7Save.setEnabled(True)
        self.Preset7Save.setMinimumSize(QSize(50, 50))
        self.Preset7Save.setMaximumSize(QSize(50, 50))
        self.Preset7Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u":/icons/save_green.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Preset7Save.setIcon(icon1)
        self.Preset7Save.setIconSize(QSize(30, 30))
        self.Preset7Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset7Save, 6, 3, 1, 1)

        self.Preset9EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset9EditName.setObjectName(u"Preset9EditName")
        self.Preset9EditName.setEnabled(True)
        self.Preset9EditName.setMinimumSize(QSize(50, 50))
        self.Preset9EditName.setMaximumSize(QSize(50, 50))
        self.Preset9EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Preset9EditName.setIcon(icon2)
        self.Preset9EditName.setIconSize(QSize(30, 30))
        self.Preset9EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset9EditName, 8, 0, 1, 1)

        self.Preset1EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset1EditName.setObjectName(u"Preset1EditName")
        self.Preset1EditName.setEnabled(True)
        self.Preset1EditName.setMinimumSize(QSize(50, 50))
        self.Preset1EditName.setMaximumSize(QSize(50, 50))
        self.Preset1EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset1EditName.setIcon(icon2)
        self.Preset1EditName.setIconSize(QSize(30, 30))
        self.Preset1EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset1EditName, 0, 0, 1, 1)

        self.Preset5Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset5Save.setObjectName(u"Preset5Save")
        self.Preset5Save.setEnabled(True)
        self.Preset5Save.setMinimumSize(QSize(50, 50))
        self.Preset5Save.setMaximumSize(QSize(50, 50))
        self.Preset5Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset5Save.setIcon(icon1)
        self.Preset5Save.setIconSize(QSize(30, 30))
        self.Preset5Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset5Save, 4, 3, 1, 1)

        self.Preset4Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset4Name.setObjectName(u"Preset4Name")
        self.Preset4Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset4Name.sizePolicy().hasHeightForWidth())
        self.Preset4Name.setSizePolicy(sizePolicy)
        self.Preset4Name.setMinimumSize(QSize(200, 0))
        self.Preset4Name.setMaximumSize(QSize(200, 16777215))
        self.Preset4Name.setFont(font1)
        self.Preset4Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset4Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset4Name, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.Preset1Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset1Name.setObjectName(u"Preset1Name")
        self.Preset1Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset1Name.sizePolicy().hasHeightForWidth())
        self.Preset1Name.setSizePolicy(sizePolicy)
        self.Preset1Name.setMinimumSize(QSize(200, 0))
        self.Preset1Name.setMaximumSize(QSize(200, 16777215))
        self.Preset1Name.setFont(font1)
        self.Preset1Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset1Name.setMaxLength(20)
        self.Preset1Name.setReadOnly(True)
        self.Preset1Name.setClearButtonEnabled(False)

        self.gridLayout_15.addWidget(self.Preset1Name, 0, 1, 1, 1)

        self.Preset3Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset3Save.setObjectName(u"Preset3Save")
        self.Preset3Save.setEnabled(True)
        self.Preset3Save.setMinimumSize(QSize(50, 50))
        self.Preset3Save.setMaximumSize(QSize(50, 50))
        self.Preset3Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset3Save.setIcon(icon1)
        self.Preset3Save.setIconSize(QSize(30, 30))
        self.Preset3Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset3Save, 2, 3, 1, 1)

        self.Preset9Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset9Save.setObjectName(u"Preset9Save")
        self.Preset9Save.setEnabled(True)
        self.Preset9Save.setMinimumSize(QSize(50, 50))
        self.Preset9Save.setMaximumSize(QSize(50, 50))
        self.Preset9Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset9Save.setIcon(icon1)
        self.Preset9Save.setIconSize(QSize(30, 30))
        self.Preset9Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset9Save, 8, 3, 1, 1)

        self.Preset3Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset3Name.setObjectName(u"Preset3Name")
        self.Preset3Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset3Name.sizePolicy().hasHeightForWidth())
        self.Preset3Name.setSizePolicy(sizePolicy)
        self.Preset3Name.setMinimumSize(QSize(200, 0))
        self.Preset3Name.setMaximumSize(QSize(200, 16777215))
        self.Preset3Name.setFont(font1)
        self.Preset3Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset3Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset3Name, 2, 1, 1, 1)

        self.Preset7Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset7Name.setObjectName(u"Preset7Name")
        self.Preset7Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset7Name.sizePolicy().hasHeightForWidth())
        self.Preset7Name.setSizePolicy(sizePolicy)
        self.Preset7Name.setMinimumSize(QSize(200, 0))
        self.Preset7Name.setMaximumSize(QSize(200, 16777215))
        self.Preset7Name.setFont(font1)
        self.Preset7Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset7Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset7Name, 6, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_12, 9, 2, 1, 1)

        self.Preset4Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset4Load.setObjectName(u"Preset4Load")
        self.Preset4Load.setEnabled(True)
        self.Preset4Load.setMinimumSize(QSize(50, 50))
        self.Preset4Load.setMaximumSize(QSize(50, 50))
        self.Preset4Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon3 = QIcon()
        icon3.addFile(u":/icons/load_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Preset4Load.setIcon(icon3)
        self.Preset4Load.setIconSize(QSize(30, 30))
        self.Preset4Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset4Load, 3, 4, 1, 1)

        self.Preset8Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset8Name.setObjectName(u"Preset8Name")
        self.Preset8Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset8Name.sizePolicy().hasHeightForWidth())
        self.Preset8Name.setSizePolicy(sizePolicy)
        self.Preset8Name.setMinimumSize(QSize(200, 0))
        self.Preset8Name.setMaximumSize(QSize(200, 16777215))
        self.Preset8Name.setFont(font1)
        self.Preset8Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset8Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset8Name, 7, 1, 1, 1)

        self.Preset8Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset8Load.setObjectName(u"Preset8Load")
        self.Preset8Load.setEnabled(True)
        self.Preset8Load.setMinimumSize(QSize(50, 50))
        self.Preset8Load.setMaximumSize(QSize(50, 50))
        self.Preset8Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset8Load.setIcon(icon3)
        self.Preset8Load.setIconSize(QSize(30, 30))
        self.Preset8Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset8Load, 7, 4, 1, 1)

        self.Preset4Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset4Save.setObjectName(u"Preset4Save")
        self.Preset4Save.setEnabled(True)
        self.Preset4Save.setMinimumSize(QSize(50, 50))
        self.Preset4Save.setMaximumSize(QSize(50, 50))
        self.Preset4Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset4Save.setIcon(icon1)
        self.Preset4Save.setIconSize(QSize(30, 30))
        self.Preset4Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset4Save, 3, 3, 1, 1)

        self.Preset7EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset7EditName.setObjectName(u"Preset7EditName")
        self.Preset7EditName.setEnabled(True)
        self.Preset7EditName.setMinimumSize(QSize(50, 50))
        self.Preset7EditName.setMaximumSize(QSize(50, 50))
        self.Preset7EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset7EditName.setIcon(icon2)
        self.Preset7EditName.setIconSize(QSize(30, 30))
        self.Preset7EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset7EditName, 6, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.Preset3Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset3Load.setObjectName(u"Preset3Load")
        self.Preset3Load.setEnabled(True)
        self.Preset3Load.setMinimumSize(QSize(50, 50))
        self.Preset3Load.setMaximumSize(QSize(50, 50))
        self.Preset3Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset3Load.setIcon(icon3)
        self.Preset3Load.setIconSize(QSize(30, 30))
        self.Preset3Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset3Load, 2, 4, 1, 1)

        self.Preset2Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset2Load.setObjectName(u"Preset2Load")
        self.Preset2Load.setEnabled(True)
        self.Preset2Load.setMinimumSize(QSize(50, 50))
        self.Preset2Load.setMaximumSize(QSize(50, 50))
        self.Preset2Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset2Load.setIcon(icon3)
        self.Preset2Load.setIconSize(QSize(30, 30))
        self.Preset2Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset2Load, 1, 4, 1, 1)

        self.Preset5Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset5Name.setObjectName(u"Preset5Name")
        self.Preset5Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset5Name.sizePolicy().hasHeightForWidth())
        self.Preset5Name.setSizePolicy(sizePolicy)
        self.Preset5Name.setMinimumSize(QSize(200, 0))
        self.Preset5Name.setMaximumSize(QSize(200, 16777215))
        self.Preset5Name.setFont(font1)
        self.Preset5Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset5Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset5Name, 4, 1, 1, 1)

        self.Preset10EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset10EditName.setObjectName(u"Preset10EditName")
        self.Preset10EditName.setEnabled(True)
        self.Preset10EditName.setMinimumSize(QSize(50, 50))
        self.Preset10EditName.setMaximumSize(QSize(50, 50))
        self.Preset10EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset10EditName.setIcon(icon2)
        self.Preset10EditName.setIconSize(QSize(30, 30))
        self.Preset10EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset10EditName, 9, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_9, 6, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 4, 2, 1, 1)

        self.Preset7Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset7Load.setObjectName(u"Preset7Load")
        self.Preset7Load.setEnabled(True)
        self.Preset7Load.setMinimumSize(QSize(50, 50))
        self.Preset7Load.setMaximumSize(QSize(50, 50))
        self.Preset7Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset7Load.setIcon(icon3)
        self.Preset7Load.setIconSize(QSize(30, 30))
        self.Preset7Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset7Load, 6, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_10, 7, 2, 1, 1)

        self.Preset5EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset5EditName.setObjectName(u"Preset5EditName")
        self.Preset5EditName.setEnabled(True)
        self.Preset5EditName.setMinimumSize(QSize(50, 50))
        self.Preset5EditName.setMaximumSize(QSize(50, 50))
        self.Preset5EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset5EditName.setIcon(icon2)
        self.Preset5EditName.setIconSize(QSize(30, 30))
        self.Preset5EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset5EditName, 4, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_11, 8, 2, 1, 1)

        self.Preset6Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset6Save.setObjectName(u"Preset6Save")
        self.Preset6Save.setEnabled(True)
        self.Preset6Save.setMinimumSize(QSize(50, 50))
        self.Preset6Save.setMaximumSize(QSize(50, 50))
        self.Preset6Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset6Save.setIcon(icon1)
        self.Preset6Save.setIconSize(QSize(30, 30))
        self.Preset6Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset6Save, 5, 3, 1, 1)

        self.Preset8EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset8EditName.setObjectName(u"Preset8EditName")
        self.Preset8EditName.setEnabled(True)
        self.Preset8EditName.setMinimumSize(QSize(50, 50))
        self.Preset8EditName.setMaximumSize(QSize(50, 50))
        self.Preset8EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset8EditName.setIcon(icon2)
        self.Preset8EditName.setIconSize(QSize(30, 30))
        self.Preset8EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset8EditName, 7, 0, 1, 1)

        self.Preset8Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset8Save.setObjectName(u"Preset8Save")
        self.Preset8Save.setEnabled(True)
        self.Preset8Save.setMinimumSize(QSize(50, 50))
        self.Preset8Save.setMaximumSize(QSize(50, 50))
        self.Preset8Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset8Save.setIcon(icon1)
        self.Preset8Save.setIconSize(QSize(30, 30))
        self.Preset8Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset8Save, 7, 3, 1, 1)

        self.Preset10Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset10Save.setObjectName(u"Preset10Save")
        self.Preset10Save.setEnabled(True)
        self.Preset10Save.setMinimumSize(QSize(50, 50))
        self.Preset10Save.setMaximumSize(QSize(50, 50))
        self.Preset10Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset10Save.setIcon(icon1)
        self.Preset10Save.setIconSize(QSize(30, 30))
        self.Preset10Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset10Save, 9, 3, 1, 1)

        self.Preset5Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset5Load.setObjectName(u"Preset5Load")
        self.Preset5Load.setEnabled(True)
        self.Preset5Load.setMinimumSize(QSize(50, 50))
        self.Preset5Load.setMaximumSize(QSize(50, 50))
        self.Preset5Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset5Load.setIcon(icon3)
        self.Preset5Load.setIconSize(QSize(30, 30))
        self.Preset5Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset5Load, 4, 4, 1, 1)

        self.Preset1Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset1Load.setObjectName(u"Preset1Load")
        self.Preset1Load.setEnabled(True)
        self.Preset1Load.setMinimumSize(QSize(50, 50))
        self.Preset1Load.setMaximumSize(QSize(50, 50))
        self.Preset1Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset1Load.setIcon(icon3)
        self.Preset1Load.setIconSize(QSize(30, 30))
        self.Preset1Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset1Load, 0, 4, 1, 1)

        self.Preset9Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset9Load.setObjectName(u"Preset9Load")
        self.Preset9Load.setEnabled(True)
        self.Preset9Load.setMinimumSize(QSize(50, 50))
        self.Preset9Load.setMaximumSize(QSize(50, 50))
        self.Preset9Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset9Load.setIcon(icon3)
        self.Preset9Load.setIconSize(QSize(30, 30))
        self.Preset9Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset9Load, 8, 4, 1, 1)

        self.Preset9Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset9Name.setObjectName(u"Preset9Name")
        self.Preset9Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset9Name.sizePolicy().hasHeightForWidth())
        self.Preset9Name.setSizePolicy(sizePolicy)
        self.Preset9Name.setMinimumSize(QSize(200, 0))
        self.Preset9Name.setMaximumSize(QSize(200, 16777215))
        self.Preset9Name.setFont(font1)
        self.Preset9Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset9Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset9Name, 8, 1, 1, 1)

        self.Preset4EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset4EditName.setObjectName(u"Preset4EditName")
        self.Preset4EditName.setEnabled(True)
        self.Preset4EditName.setMinimumSize(QSize(50, 50))
        self.Preset4EditName.setMaximumSize(QSize(50, 50))
        self.Preset4EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset4EditName.setIcon(icon2)
        self.Preset4EditName.setIconSize(QSize(30, 30))
        self.Preset4EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset4EditName, 3, 0, 1, 1)

        self.Preset2Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset2Name.setObjectName(u"Preset2Name")
        self.Preset2Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset2Name.sizePolicy().hasHeightForWidth())
        self.Preset2Name.setSizePolicy(sizePolicy)
        self.Preset2Name.setMinimumSize(QSize(200, 0))
        self.Preset2Name.setMaximumSize(QSize(200, 16777215))
        self.Preset2Name.setFont(font1)
        self.Preset2Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset2Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset2Name, 1, 1, 1, 1)

        self.Preset1Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset1Save.setObjectName(u"Preset1Save")
        self.Preset1Save.setEnabled(True)
        self.Preset1Save.setMinimumSize(QSize(50, 50))
        self.Preset1Save.setMaximumSize(QSize(50, 50))
        self.Preset1Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset1Save.setIcon(icon1)
        self.Preset1Save.setIconSize(QSize(30, 30))
        self.Preset1Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset1Save, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.Preset10Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset10Load.setObjectName(u"Preset10Load")
        self.Preset10Load.setEnabled(True)
        self.Preset10Load.setMinimumSize(QSize(50, 50))
        self.Preset10Load.setMaximumSize(QSize(50, 50))
        self.Preset10Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset10Load.setIcon(icon3)
        self.Preset10Load.setIconSize(QSize(30, 30))
        self.Preset10Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset10Load, 9, 4, 1, 1)

        self.Preset6Load = QPushButton(self.scrollAreaWidgetContents)
        self.Preset6Load.setObjectName(u"Preset6Load")
        self.Preset6Load.setEnabled(True)
        self.Preset6Load.setMinimumSize(QSize(50, 50))
        self.Preset6Load.setMaximumSize(QSize(50, 50))
        self.Preset6Load.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset6Load.setIcon(icon3)
        self.Preset6Load.setIconSize(QSize(30, 30))
        self.Preset6Load.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset6Load, 5, 4, 1, 1)

        self.Preset2Save = QPushButton(self.scrollAreaWidgetContents)
        self.Preset2Save.setObjectName(u"Preset2Save")
        self.Preset2Save.setEnabled(True)
        self.Preset2Save.setMinimumSize(QSize(50, 50))
        self.Preset2Save.setMaximumSize(QSize(50, 50))
        self.Preset2Save.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        self.Preset2Save.setIcon(icon1)
        self.Preset2Save.setIconSize(QSize(30, 30))
        self.Preset2Save.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset2Save, 1, 3, 1, 1)

        self.Preset6Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Preset6Name.setObjectName(u"Preset6Name")
        self.Preset6Name.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Preset6Name.sizePolicy().hasHeightForWidth())
        self.Preset6Name.setSizePolicy(sizePolicy)
        self.Preset6Name.setMinimumSize(QSize(200, 0))
        self.Preset6Name.setMaximumSize(QSize(200, 16777215))
        self.Preset6Name.setFont(font1)
        self.Preset6Name.setStyleSheet(u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"")
        self.Preset6Name.setMaxLength(20)

        self.gridLayout_15.addWidget(self.Preset6Name, 5, 1, 1, 1)

        self.Preset3EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset3EditName.setObjectName(u"Preset3EditName")
        self.Preset3EditName.setEnabled(True)
        self.Preset3EditName.setMinimumSize(QSize(50, 50))
        self.Preset3EditName.setMaximumSize(QSize(50, 50))
        self.Preset3EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset3EditName.setIcon(icon2)
        self.Preset3EditName.setIconSize(QSize(30, 30))
        self.Preset3EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset3EditName, 2, 0, 1, 1)

        self.Preset6EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset6EditName.setObjectName(u"Preset6EditName")
        self.Preset6EditName.setEnabled(True)
        self.Preset6EditName.setMinimumSize(QSize(50, 50))
        self.Preset6EditName.setMaximumSize(QSize(50, 50))
        self.Preset6EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset6EditName.setIcon(icon2)
        self.Preset6EditName.setIconSize(QSize(30, 30))
        self.Preset6EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset6EditName, 5, 0, 1, 1)

        self.Preset2EditName = QPushButton(self.scrollAreaWidgetContents)
        self.Preset2EditName.setObjectName(u"Preset2EditName")
        self.Preset2EditName.setEnabled(True)
        self.Preset2EditName.setMinimumSize(QSize(50, 50))
        self.Preset2EditName.setMaximumSize(QSize(50, 50))
        self.Preset2EditName.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(128, 128, 128, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(128, 128, 128, 100);\n"
"}\n"
"")
        self.Preset2EditName.setIcon(icon2)
        self.Preset2EditName.setIconSize(QSize(30, 30))
        self.Preset2EditName.setFlat(True)

        self.gridLayout_15.addWidget(self.Preset2EditName, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_8, 5, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_2, 2, 0, 1, 1)

        self.label_17 = QLabel(self.savePage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.gridLayout_13.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_3 = QLabel(self.savePage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_13.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.savePage)
        self.runPage = QWidget()
        self.runPage.setObjectName(u"runPage")
        self.gridLayout_14 = QGridLayout(self.runPage)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_5 = QLabel(self.runPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color:grey;")

        self.gridLayout_14.addWidget(self.label_5, 1, 0, 1, 2)

        self.label_43 = QLabel(self.runPage)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"color:grey;")

        self.gridLayout_14.addWidget(self.label_43, 3, 0, 1, 2)

        self.label_4 = QLabel(self.runPage)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_14.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_42 = QLabel(self.runPage)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_14.addWidget(self.label_42, 2, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 545, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_11, 5, 1, 1, 1)

        self.label_37 = QLabel(self.runPage)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_14.addWidget(self.label_37, 4, 0, 1, 1)

        self.plainTextEdit_17 = QPlainTextEdit(self.runPage)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_17.setStyleSheet(u"")
        self.plainTextEdit_17.setMaximumBlockCount(1)

        self.gridLayout_14.addWidget(self.plainTextEdit_17, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.runPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.gridLayout_7 = QGridLayout(self.settingsPage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.themeComboBox = QComboBox(self.settingsPage)
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.themeComboBox.setObjectName(u"themeComboBox")

        self.gridLayout_7.addWidget(self.themeComboBox, 2, 1, 1, 1)

        self.themeLabel = QLabel(self.settingsPage)
        self.themeLabel.setObjectName(u"themeLabel")

        self.gridLayout_7.addWidget(self.themeLabel, 2, 0, 1, 1)

        self.label_41 = QLabel(self.settingsPage)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(u"color:grey;")
        self.label_41.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_41, 1, 0, 1, 2)

        self.label_45 = QLabel(self.settingsPage)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"color:grey;")

        self.gridLayout_7.addWidget(self.label_45, 3, 0, 1, 2)

        self.toggleNotifsLabel = QLabel(self.settingsPage)
        self.toggleNotifsLabel.setObjectName(u"toggleNotifsLabel")

        self.gridLayout_7.addWidget(self.toggleNotifsLabel, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.autoSprintLabel = QLabel(self.settingsPage)
        self.autoSprintLabel.setObjectName(u"autoSprintLabel")

        self.gridLayout_7.addWidget(self.autoSprintLabel, 4, 0, 1, 1)

        self.label_64 = QLabel(self.settingsPage)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"color:grey;")
        self.label_64.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_64, 5, 0, 1, 2)

        self.stackedWidget.addWidget(self.settingsPage)
        self.chatPage = QWidget()
        self.chatPage.setObjectName(u"chatPage")
        self.gridLayout_16 = QGridLayout(self.chatPage)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_63 = QLabel(self.chatPage)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_16.addWidget(self.label_63, 9, 0, 1, 1)

        self.TrashTalkHotkey = QPlainTextEdit(self.chatPage)
        self.TrashTalkHotkey.setObjectName(u"TrashTalkHotkey")
        self.TrashTalkHotkey.setMinimumSize(QSize(0, 30))
        self.TrashTalkHotkey.setMaximumSize(QSize(16777215, 30))
        self.TrashTalkHotkey.setMaximumBlockCount(1)

        self.gridLayout_16.addWidget(self.TrashTalkHotkey, 9, 1, 1, 1)

        self.label_6 = QLabel(self.chatPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color:grey;")

        self.gridLayout_16.addWidget(self.label_6, 1, 0, 1, 2)

        self.label_14 = QLabel(self.chatPage)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_16.addWidget(self.label_14, 3, 0, 1, 1)

        self.GoldenTongueLabel = QLabel(self.chatPage)
        self.GoldenTongueLabel.setObjectName(u"GoldenTongueLabel")

        self.gridLayout_16.addWidget(self.GoldenTongueLabel, 0, 0, 1, 1)

        self.plainTextEdit_6 = QPlainTextEdit(self.chatPage)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_6.setStyleSheet(u"")
        self.plainTextEdit_6.setMaximumBlockCount(1)

        self.gridLayout_16.addWidget(self.plainTextEdit_6, 3, 1, 1, 1)

        self.scrollArea_4 = QScrollArea(self.chatPage)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -937, 639, 1372))
        self.gridLayout_20 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.MessageHotkeyLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel.setObjectName(u"MessageHotkeyLabel")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel, 0, 0, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)
        self.label_55.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_55, 1, 0, 1, 2)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_20.addWidget(self.label_56, 2, 0, 1, 1)

        self.MessageHotkeyArea_1 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_1.setObjectName(u"MessageHotkeyArea_1")
        self.MessageHotkeyArea_1.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_1.setStyleSheet(u"")
        self.MessageHotkeyArea_1.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_1, 2, 1, 1, 1)

        self.label_57 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_20.addWidget(self.label_57, 3, 0, 1, 1)

        self.MessageArea_1 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_1.setObjectName(u"MessageArea_1")
        self.MessageArea_1.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_1.setStyleSheet(u"")
        self.MessageArea_1.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_1, 3, 1, 1, 1)

        self.MessageHotkeyLabel2 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel2.setObjectName(u"MessageHotkeyLabel2")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel2, 4, 0, 1, 1)

        self.label_58 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)
        self.label_58.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_58, 5, 0, 1, 2)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_20.addWidget(self.label_59, 6, 0, 1, 1)

        self.MessageHotkeyArea_2 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_2.setObjectName(u"MessageHotkeyArea_2")
        self.MessageHotkeyArea_2.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_2.setStyleSheet(u"")
        self.MessageHotkeyArea_2.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_2, 6, 1, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_20.addWidget(self.label_60, 7, 0, 1, 1)

        self.MessageArea_2 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_2.setObjectName(u"MessageArea_2")
        self.MessageArea_2.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_2.setStyleSheet(u"")
        self.MessageArea_2.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_2, 7, 1, 1, 1)

        self.MessageHotkeyLabel3 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel3.setObjectName(u"MessageHotkeyLabel3")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel3, 8, 0, 1, 1)

        self.label_90 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font)
        self.label_90.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_90, 9, 0, 1, 2)

        self.label_91 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_20.addWidget(self.label_91, 10, 0, 1, 1)

        self.MessageHotkeyArea_3 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_3.setObjectName(u"MessageHotkeyArea_3")
        self.MessageHotkeyArea_3.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_3.setStyleSheet(u"")
        self.MessageHotkeyArea_3.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_3, 10, 1, 1, 1)

        self.label_92 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_20.addWidget(self.label_92, 11, 0, 1, 1)

        self.MessageArea_3 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_3.setObjectName(u"MessageArea_3")
        self.MessageArea_3.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_3.setStyleSheet(u"")
        self.MessageArea_3.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_3, 11, 1, 1, 1)

        self.MessageHotkeyLabel4 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel4.setObjectName(u"MessageHotkeyLabel4")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel4, 12, 0, 1, 1)

        self.label_93 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font)
        self.label_93.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_93, 13, 0, 1, 2)

        self.label_94 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_20.addWidget(self.label_94, 14, 0, 1, 1)

        self.MessageHotkeyArea_4 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_4.setObjectName(u"MessageHotkeyArea_4")
        self.MessageHotkeyArea_4.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_4.setStyleSheet(u"")
        self.MessageHotkeyArea_4.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_4, 14, 1, 1, 1)

        self.label_95 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_20.addWidget(self.label_95, 15, 0, 1, 1)

        self.MessageArea_4 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_4.setObjectName(u"MessageArea_4")
        self.MessageArea_4.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_4.setStyleSheet(u"")
        self.MessageArea_4.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_4, 15, 1, 1, 1)

        self.MessageHotkeyLabel5 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel5.setObjectName(u"MessageHotkeyLabel5")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel5, 16, 0, 1, 1)

        self.label_96 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font)
        self.label_96.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_96, 17, 0, 1, 2)

        self.label_97 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_20.addWidget(self.label_97, 18, 0, 1, 1)

        self.MessageHotkeyArea_5 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_5.setObjectName(u"MessageHotkeyArea_5")
        self.MessageHotkeyArea_5.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_5.setStyleSheet(u"")
        self.MessageHotkeyArea_5.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_5, 18, 1, 1, 1)

        self.label_98 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_20.addWidget(self.label_98, 19, 0, 1, 1)

        self.MessageArea_5 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_5.setObjectName(u"MessageArea_5")
        self.MessageArea_5.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_5.setStyleSheet(u"")
        self.MessageArea_5.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_5, 19, 1, 1, 1)

        self.MessageHotkeyLabel6 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel6.setObjectName(u"MessageHotkeyLabel6")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel6, 20, 0, 1, 1)

        self.label_99 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font)
        self.label_99.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_99, 21, 0, 1, 2)

        self.label_101 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_20.addWidget(self.label_101, 22, 0, 1, 1)

        self.MessageHotkeyArea_6 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_6.setObjectName(u"MessageHotkeyArea_6")
        self.MessageHotkeyArea_6.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_6.setStyleSheet(u"")
        self.MessageHotkeyArea_6.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_6, 22, 1, 1, 1)

        self.label_100 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_20.addWidget(self.label_100, 23, 0, 1, 1)

        self.MessageArea_6 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_6.setObjectName(u"MessageArea_6")
        self.MessageArea_6.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_6.setStyleSheet(u"")
        self.MessageArea_6.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_6, 23, 1, 1, 1)

        self.MessageHotkeyLabel7 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel7.setObjectName(u"MessageHotkeyLabel7")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel7, 24, 0, 1, 1)

        self.label_102 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font)
        self.label_102.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_102, 25, 0, 1, 2)

        self.label_104 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_20.addWidget(self.label_104, 26, 0, 1, 1)

        self.MessageHotkeyArea_7 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_7.setObjectName(u"MessageHotkeyArea_7")
        self.MessageHotkeyArea_7.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_7.setStyleSheet(u"")
        self.MessageHotkeyArea_7.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_7, 26, 1, 1, 1)

        self.label_103 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_20.addWidget(self.label_103, 27, 0, 1, 1)

        self.MessageArea_7 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_7.setObjectName(u"MessageArea_7")
        self.MessageArea_7.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_7.setStyleSheet(u"")
        self.MessageArea_7.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_7, 27, 1, 1, 1)

        self.MessageHotkeyLabel8 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel8.setObjectName(u"MessageHotkeyLabel8")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel8, 28, 0, 1, 1)

        self.label_107 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font)
        self.label_107.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_107, 29, 0, 1, 2)

        self.label_105 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_20.addWidget(self.label_105, 30, 0, 1, 1)

        self.MessageHotkeyArea_8 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_8.setObjectName(u"MessageHotkeyArea_8")
        self.MessageHotkeyArea_8.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_8.setStyleSheet(u"")
        self.MessageHotkeyArea_8.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_8, 30, 1, 1, 1)

        self.label_106 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_20.addWidget(self.label_106, 31, 0, 1, 1)

        self.MessageArea_8 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_8.setObjectName(u"MessageArea_8")
        self.MessageArea_8.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_8.setStyleSheet(u"")
        self.MessageArea_8.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_8, 31, 1, 1, 1)

        self.MessageHotkeyLabel9 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel9.setObjectName(u"MessageHotkeyLabel9")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel9, 32, 0, 1, 1)

        self.label_110 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font)
        self.label_110.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_110, 33, 0, 1, 2)

        self.label_108 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_20.addWidget(self.label_108, 34, 0, 1, 1)

        self.MessageHotkeyArea_9 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_9.setObjectName(u"MessageHotkeyArea_9")
        self.MessageHotkeyArea_9.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_9.setStyleSheet(u"")
        self.MessageHotkeyArea_9.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_9, 34, 1, 1, 1)

        self.label_109 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_20.addWidget(self.label_109, 35, 0, 1, 1)

        self.MessageArea_9 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_9.setObjectName(u"MessageArea_9")
        self.MessageArea_9.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_9.setStyleSheet(u"")
        self.MessageArea_9.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_9, 35, 1, 1, 1)

        self.MessageHotkeyLabel10 = QLabel(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyLabel10.setObjectName(u"MessageHotkeyLabel10")

        self.gridLayout_20.addWidget(self.MessageHotkeyLabel10, 36, 0, 1, 1)

        self.label_113 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font)
        self.label_113.setStyleSheet(u"color:grey;")

        self.gridLayout_20.addWidget(self.label_113, 37, 0, 1, 2)

        self.label_111 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_20.addWidget(self.label_111, 38, 0, 1, 1)

        self.MessageHotkeyArea_10 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageHotkeyArea_10.setObjectName(u"MessageHotkeyArea_10")
        self.MessageHotkeyArea_10.setMaximumSize(QSize(16777215, 30))
        self.MessageHotkeyArea_10.setStyleSheet(u"")
        self.MessageHotkeyArea_10.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageHotkeyArea_10, 38, 1, 1, 1)

        self.label_112 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_20.addWidget(self.label_112, 39, 0, 1, 1)

        self.MessageArea_10 = QPlainTextEdit(self.scrollAreaWidgetContents_5)
        self.MessageArea_10.setObjectName(u"MessageArea_10")
        self.MessageArea_10.setMaximumSize(QSize(16777215, 30))
        self.MessageArea_10.setStyleSheet(u"")
        self.MessageArea_10.setMaximumBlockCount(1)

        self.gridLayout_20.addWidget(self.MessageArea_10, 39, 1, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_16.addWidget(self.scrollArea_4, 10, 0, 1, 2)

        self.label_15 = QLabel(self.chatPage)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_16.addWidget(self.label_15, 2, 0, 1, 1)

        self.GoldenTongueHotkeyArea = QPlainTextEdit(self.chatPage)
        self.GoldenTongueHotkeyArea.setObjectName(u"GoldenTongueHotkeyArea")
        self.GoldenTongueHotkeyArea.setMaximumSize(QSize(16777215, 30))
        self.GoldenTongueHotkeyArea.setStyleSheet(u"")
        self.GoldenTongueHotkeyArea.setMaximumBlockCount(1)

        self.gridLayout_16.addWidget(self.GoldenTongueHotkeyArea, 2, 1, 1, 1)

        self.TrashTalkLabel = QLabel(self.chatPage)
        self.TrashTalkLabel.setObjectName(u"TrashTalkLabel")

        self.gridLayout_16.addWidget(self.TrashTalkLabel, 5, 0, 1, 1)

        self.label_62 = QLabel(self.chatPage)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color:grey;")

        self.gridLayout_16.addWidget(self.label_62, 7, 0, 1, 2)

        self.stackedWidget.addWidget(self.chatPage)
        self.combatPage = QWidget()
        self.combatPage.setObjectName(u"combatPage")
        self.gridLayout_18 = QGridLayout(self.combatPage)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.autoLogLabel = QLabel(self.combatPage)
        self.autoLogLabel.setObjectName(u"autoLogLabel")

        self.gridLayout_18.addWidget(self.autoLogLabel, 3, 0, 1, 1)

        self.autoLogHotkey = QPlainTextEdit(self.combatPage)
        self.autoLogHotkey.setObjectName(u"autoLogHotkey")
        self.autoLogHotkey.setMinimumSize(QSize(30, 30))
        self.autoLogHotkey.setMaximumSize(QSize(1677215, 30))
        self.autoLogHotkey.setMaximumBlockCount(1)

        self.gridLayout_18.addWidget(self.autoLogHotkey, 5, 1, 1, 2)

        self.label_65 = QLabel(self.combatPage)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color:grey;")

        self.gridLayout_18.addWidget(self.label_65, 4, 0, 1, 3)

        self.autoLogCoordButton = QPushButton(self.combatPage)
        self.autoLogCoordButton.setObjectName(u"autoLogCoordButton")

        self.gridLayout_18.addWidget(self.autoLogCoordButton, 7, 0, 1, 3)

        self.label_54 = QLabel(self.combatPage)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color:grey;")

        self.gridLayout_18.addWidget(self.label_54, 14, 0, 1, 2)

        self.AutoTacetLabel = QLabel(self.combatPage)
        self.AutoTacetLabel.setObjectName(u"AutoTacetLabel")

        self.gridLayout_18.addWidget(self.AutoTacetLabel, 9, 0, 1, 2)

        self.AutoUncrouchLabel = QLabel(self.combatPage)
        self.AutoUncrouchLabel.setObjectName(u"AutoUncrouchLabel")

        self.gridLayout_18.addWidget(self.AutoUncrouchLabel, 13, 0, 1, 2)

        self.label_53 = QLabel(self.combatPage)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_18.addWidget(self.label_53, 6, 0, 1, 1)

        self.autoLogCoords = QPlainTextEdit(self.combatPage)
        self.autoLogCoords.setObjectName(u"autoLogCoords")
        self.autoLogCoords.setMaximumSize(QSize(16777215, 30))
        self.autoLogCoords.setMaximumBlockCount(1)

        self.gridLayout_18.addWidget(self.autoLogCoords, 6, 1, 1, 2)

        self.MbAllHotkeyArea = QPlainTextEdit(self.combatPage)
        self.MbAllHotkeyArea.setObjectName(u"MbAllHotkeyArea")
        self.MbAllHotkeyArea.setMinimumSize(QSize(0, 30))
        self.MbAllHotkeyArea.setMaximumSize(QSize(16777215, 30))
        self.MbAllHotkeyArea.setStyleSheet(u"")
        self.MbAllHotkeyArea.setMaximumBlockCount(1)

        self.gridLayout_18.addWidget(self.MbAllHotkeyArea, 2, 1, 1, 2)

        self.label_66 = QLabel(self.combatPage)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_18.addWidget(self.label_66, 5, 0, 1, 1)

        self.label_50 = QLabel(self.combatPage)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(u"color:grey;")

        self.gridLayout_18.addWidget(self.label_50, 1, 0, 1, 3)

        self.MbAllDropdown = QLabel(self.combatPage)
        self.MbAllDropdown.setObjectName(u"MbAllDropdown")

        self.gridLayout_18.addWidget(self.MbAllDropdown, 2, 0, 1, 1)

        self.label_52 = QLabel(self.combatPage)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color:grey;")

        self.gridLayout_18.addWidget(self.label_52, 10, 0, 1, 2)

        self.MbAllLabel = QLabel(self.combatPage)
        self.MbAllLabel.setObjectName(u"MbAllLabel")

        self.gridLayout_18.addWidget(self.MbAllLabel, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_5, 15, 0, 1, 1)

        self.autoTacetKeybind = QPlainTextEdit(self.combatPage)
        self.autoTacetKeybind.setObjectName(u"autoTacetKeybind")
        self.autoTacetKeybind.setMinimumSize(QSize(0, 30))
        self.autoTacetKeybind.setMaximumSize(QSize(16777215, 30))
        self.autoTacetKeybind.setStyleSheet(u"")
        self.autoTacetKeybind.setMaximumBlockCount(1)

        self.gridLayout_18.addWidget(self.autoTacetKeybind, 11, 1, 1, 1)

        self.label_51 = QLabel(self.combatPage)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_18.addWidget(self.label_51, 11, 0, 1, 1)

        self.stackedWidget.addWidget(self.combatPage)
        self.silentheartPage = QWidget()
        self.silentheartPage.setObjectName(u"silentheartPage")
        self.gridLayout_22 = QGridLayout(self.silentheartPage)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_136 = QLabel(self.silentheartPage)
        self.label_136.setObjectName(u"label_136")

        self.gridLayout_22.addWidget(self.label_136, 7, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_6, 17, 1, 1, 1)

        self.AnkleCutterHotkey = QPlainTextEdit(self.silentheartPage)
        self.AnkleCutterHotkey.setObjectName(u"AnkleCutterHotkey")
        self.AnkleCutterHotkey.setMinimumSize(QSize(0, 30))
        self.AnkleCutterHotkey.setMaximumSize(QSize(16777215, 30))
        self.AnkleCutterHotkey.setStyleSheet(u"")
        self.AnkleCutterHotkey.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.AnkleCutterHotkey, 15, 1, 1, 1)

        self.MayhemLabel = QLabel(self.silentheartPage)
        self.MayhemLabel.setObjectName(u"MayhemLabel")

        self.gridLayout_22.addWidget(self.MayhemLabel, 4, 0, 1, 1)

        self.RisingStarLabel = QLabel(self.silentheartPage)
        self.RisingStarLabel.setObjectName(u"RisingStarLabel")

        self.gridLayout_22.addWidget(self.RisingStarLabel, 8, 0, 1, 1)

        self.label_131 = QLabel(self.silentheartPage)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font)
        self.label_131.setStyleSheet(u"color:grey;")

        self.gridLayout_22.addWidget(self.label_131, 1, 0, 1, 2)

        self.RelentlessHuntHotkeyLabel = QLabel(self.silentheartPage)
        self.RelentlessHuntHotkeyLabel.setObjectName(u"RelentlessHuntHotkeyLabel")

        self.gridLayout_22.addWidget(self.RelentlessHuntHotkeyLabel, 2, 0, 1, 1)

        self.label_135 = QLabel(self.silentheartPage)
        self.label_135.setObjectName(u"label_135")

        self.gridLayout_22.addWidget(self.label_135, 3, 0, 1, 1)

        self.FlowStateKeybind = QPlainTextEdit(self.silentheartPage)
        self.FlowStateKeybind.setObjectName(u"FlowStateKeybind")
        self.FlowStateKeybind.setMaximumSize(QSize(16777215, 30))
        self.FlowStateKeybind.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.FlowStateKeybind, 3, 1, 1, 1)

        self.FlowStateKeybind_3 = QPlainTextEdit(self.silentheartPage)
        self.FlowStateKeybind_3.setObjectName(u"FlowStateKeybind_3")
        self.FlowStateKeybind_3.setMaximumSize(QSize(16777215, 30))
        self.FlowStateKeybind_3.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.FlowStateKeybind_3, 12, 1, 1, 1)

        self.label_132 = QLabel(self.silentheartPage)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font)
        self.label_132.setStyleSheet(u"color:grey;")

        self.gridLayout_22.addWidget(self.label_132, 5, 0, 1, 2)

        self.AnkleCutterLabel = QLabel(self.silentheartPage)
        self.AnkleCutterLabel.setObjectName(u"AnkleCutterLabel")

        self.gridLayout_22.addWidget(self.AnkleCutterLabel, 13, 0, 1, 1)

        self.label_137 = QLabel(self.silentheartPage)
        self.label_137.setObjectName(u"label_137")

        self.gridLayout_22.addWidget(self.label_137, 12, 0, 1, 1)

        self.RelentlessHuntLabel = QLabel(self.silentheartPage)
        self.RelentlessHuntLabel.setObjectName(u"RelentlessHuntLabel")

        self.gridLayout_22.addWidget(self.RelentlessHuntLabel, 0, 0, 1, 1)

        self.RelentlessHuntHotkey = QPlainTextEdit(self.silentheartPage)
        self.RelentlessHuntHotkey.setObjectName(u"RelentlessHuntHotkey")
        self.RelentlessHuntHotkey.setMinimumSize(QSize(0, 30))
        self.RelentlessHuntHotkey.setMaximumSize(QSize(16777215, 30))
        self.RelentlessHuntHotkey.setStyleSheet(u"")
        self.RelentlessHuntHotkey.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.RelentlessHuntHotkey, 2, 1, 1, 1)

        self.MayhemHotkey = QPlainTextEdit(self.silentheartPage)
        self.MayhemHotkey.setObjectName(u"MayhemHotkey")
        self.MayhemHotkey.setMinimumSize(QSize(0, 30))
        self.MayhemHotkey.setMaximumSize(QSize(16777215, 30))
        self.MayhemHotkey.setStyleSheet(u"")
        self.MayhemHotkey.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.MayhemHotkey, 6, 1, 1, 1)

        self.label_134 = QLabel(self.silentheartPage)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font)
        self.label_134.setStyleSheet(u"color:grey;")

        self.gridLayout_22.addWidget(self.label_134, 14, 0, 1, 2)

        self.FlowStateKeybind_2 = QPlainTextEdit(self.silentheartPage)
        self.FlowStateKeybind_2.setObjectName(u"FlowStateKeybind_2")
        self.FlowStateKeybind_2.setMaximumSize(QSize(16777215, 30))
        self.FlowStateKeybind_2.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.FlowStateKeybind_2, 7, 1, 1, 1)

        self.AnkleCutterHotkeyLabel = QLabel(self.silentheartPage)
        self.AnkleCutterHotkeyLabel.setObjectName(u"AnkleCutterHotkeyLabel")

        self.gridLayout_22.addWidget(self.AnkleCutterHotkeyLabel, 15, 0, 1, 1)

        self.RisingStarHotkey = QPlainTextEdit(self.silentheartPage)
        self.RisingStarHotkey.setObjectName(u"RisingStarHotkey")
        self.RisingStarHotkey.setMinimumSize(QSize(0, 30))
        self.RisingStarHotkey.setMaximumSize(QSize(16777215, 30))
        self.RisingStarHotkey.setStyleSheet(u"")
        self.RisingStarHotkey.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.RisingStarHotkey, 11, 1, 1, 1)

        self.MayhemHotkeyLabel = QLabel(self.silentheartPage)
        self.MayhemHotkeyLabel.setObjectName(u"MayhemHotkeyLabel")

        self.gridLayout_22.addWidget(self.MayhemHotkeyLabel, 6, 0, 1, 1)

        self.RisingStarHotkeyLabel = QLabel(self.silentheartPage)
        self.RisingStarHotkeyLabel.setObjectName(u"RisingStarHotkeyLabel")

        self.gridLayout_22.addWidget(self.RisingStarHotkeyLabel, 11, 0, 1, 1)

        self.label_133 = QLabel(self.silentheartPage)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font)
        self.label_133.setStyleSheet(u"color:grey;")

        self.gridLayout_22.addWidget(self.label_133, 9, 0, 1, 2)

        self.FlowStateKeybind_4 = QPlainTextEdit(self.silentheartPage)
        self.FlowStateKeybind_4.setObjectName(u"FlowStateKeybind_4")
        self.FlowStateKeybind_4.setMaximumSize(QSize(16777215, 30))
        self.FlowStateKeybind_4.setMaximumBlockCount(1)

        self.gridLayout_22.addWidget(self.FlowStateKeybind_4, 16, 1, 1, 1)

        self.label_138 = QLabel(self.silentheartPage)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_22.addWidget(self.label_138, 16, 0, 1, 1)

        self.stackedWidget.addWidget(self.silentheartPage)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout_24.addWidget(self.frame, 0, 1, 1, 1)

        self.menuBar = QFrame(self.container)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setMinimumSize(QSize(50, 0))
        self.menuBar.setMaximumSize(QSize(50, 16777215))
        self.menuBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.menuBar)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressionButton = QPushButton(self.menuBar)
        self.progressionButton.setObjectName(u"progressionButton")
        self.progressionButton.setMinimumSize(QSize(50, 50))
        self.progressionButton.setMaximumSize(QSize(50, 50))
        self.progressionButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon4 = QIcon()
        icon4.addFile(u":/icons/progression.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.progressionButton.setIcon(icon4)
        self.progressionButton.setIconSize(QSize(35, 35))
        self.progressionButton.setFlat(True)

        self.gridLayout_3.addWidget(self.progressionButton, 4, 0, 1, 1)

        self.chatButton = QPushButton(self.menuBar)
        self.chatButton.setObjectName(u"chatButton")
        self.chatButton.setMinimumSize(QSize(50, 50))
        self.chatButton.setMaximumSize(QSize(50, 50))
        self.chatButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon5 = QIcon()
        icon5.addFile(u":/icons/chat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chatButton.setIcon(icon5)
        self.chatButton.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.chatButton, 8, 0, 1, 1)

        self.combatButton = QPushButton(self.menuBar)
        self.combatButton.setObjectName(u"combatButton")
        self.combatButton.setMinimumSize(QSize(50, 50))
        self.combatButton.setMaximumSize(QSize(50, 50))
        self.combatButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon6 = QIcon()
        icon6.addFile(u":/icons/combat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.combatButton.setIcon(icon6)
        self.combatButton.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.combatButton, 7, 0, 1, 1)

        self.saveButton = QPushButton(self.menuBar)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(50, 50))
        self.saveButton.setMaximumSize(QSize(50, 50))
        self.saveButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon7)
        self.saveButton.setIconSize(QSize(30, 30))
        self.saveButton.setFlat(True)

        self.gridLayout_3.addWidget(self.saveButton, 0, 0, 1, 1)

        self.bellButton = QPushButton(self.menuBar)
        self.bellButton.setObjectName(u"bellButton")
        self.bellButton.setMinimumSize(QSize(50, 50))
        self.bellButton.setMaximumSize(QSize(50, 50))
        self.bellButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon8 = QIcon()
        icon8.addFile(u":/icons/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bellButton.setIcon(icon8)
        self.bellButton.setIconSize(QSize(30, 30))
        self.bellButton.setFlat(True)

        self.gridLayout_3.addWidget(self.bellButton, 1, 0, 1, 1)

        self.playButton = QPushButton(self.menuBar)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(50, 50))
        self.playButton.setMaximumSize(QSize(50, 50))
        self.playButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon9 = QIcon()
        icon9.addFile(u":/icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playButton.setIcon(icon9)
        self.playButton.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.playButton, 10, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 12, 0, 1, 1)

        self.settingsButton = QPushButton(self.menuBar)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(50, 50))
        self.settingsButton.setMaximumSize(QSize(50, 50))
        self.settingsButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon10 = QIcon()
        icon10.addFile(u":/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon10)
        self.settingsButton.setIconSize(QSize(35, 35))
        self.settingsButton.setFlat(True)

        self.gridLayout_3.addWidget(self.settingsButton, 11, 0, 1, 1)

        self.mantrasButton = QPushButton(self.menuBar)
        self.mantrasButton.setObjectName(u"mantrasButton")
        self.mantrasButton.setMinimumSize(QSize(50, 50))
        self.mantrasButton.setMaximumSize(QSize(50, 50))
        self.mantrasButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon11 = QIcon()
        icon11.addFile(u":/icons/mantras.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mantrasButton.setIcon(icon11)
        self.mantrasButton.setIconSize(QSize(35, 35))
        self.mantrasButton.setFlat(True)

        self.gridLayout_3.addWidget(self.mantrasButton, 2, 0, 1, 1)

        self.weaponsButton = QPushButton(self.menuBar)
        self.weaponsButton.setObjectName(u"weaponsButton")
        self.weaponsButton.setMinimumSize(QSize(50, 50))
        self.weaponsButton.setMaximumSize(QSize(50, 50))
        self.weaponsButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon12 = QIcon()
        icon12.addFile(u":/icons/weapons.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.weaponsButton.setIcon(icon12)
        self.weaponsButton.setIconSize(QSize(35, 35))
        self.weaponsButton.setFlat(True)

        self.gridLayout_3.addWidget(self.weaponsButton, 3, 0, 1, 1)

        self.silentheartButton = QPushButton(self.menuBar)
        self.silentheartButton.setObjectName(u"silentheartButton")
        self.silentheartButton.setMinimumSize(QSize(50, 50))
        self.silentheartButton.setMaximumSize(QSize(50, 50))
        self.silentheartButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon13 = QIcon()
        icon13.addFile(u":/icons/silentheart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.silentheartButton.setIcon(icon13)
        self.silentheartButton.setIconSize(QSize(35, 35))

        self.gridLayout_3.addWidget(self.silentheartButton, 9, 0, 1, 1)

        self.miscButton = QPushButton(self.menuBar)
        self.miscButton.setObjectName(u"miscButton")
        self.miscButton.setMinimumSize(QSize(50, 50))
        self.miscButton.setMaximumSize(QSize(50, 50))
        self.miscButton.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        padding: 2px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgba(128, 128, 128, 50);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgba(128, 128, 128, 100);\n"
"    }")
        icon14 = QIcon()
        icon14.addFile(u":/icons/miscellaneous.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.miscButton.setIcon(icon14)
        self.miscButton.setIconSize(QSize(35, 35))
        self.miscButton.setFlat(True)

        self.gridLayout_3.addWidget(self.miscButton, 5, 0, 1, 1)


        self.gridLayout_24.addWidget(self.menuBar, 0, 0, 1, 1)

        self.contacts_frame = QFrame(self.container)
        self.contacts_frame.setObjectName(u"contacts_frame")
        self.contacts_frame.setMinimumSize(QSize(0, 30))
        self.contacts_frame.setStyleSheet(u"border:none;")
        self.contacts_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contacts_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contacts_frame)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 3, -1, 3)
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.label_144 = QLabel(self.contacts_frame)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label_144)

        self.label_143 = QLabel(self.contacts_frame)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout.addWidget(self.label_143, 0, Qt.AlignmentFlag.AlignVCenter)

        self.lineEdit = QLineEdit(self.contacts_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(60, 16777215))
        self.lineEdit.setStyleSheet(u"border:none;background:transparent;color:grey;qproperty-alignment: 'AlignHCenter | AlignVCenter';")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_73 = QLabel(self.contacts_frame)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label_73)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)


        self.gridLayout_24.addWidget(self.contacts_frame, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.container, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Save</span></p></body></html>", None))
        self.menuButton.setText("")
        self.BellMovestack.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Bell Movestack</span></p></body></html>", None))
        self.MovestackChoice.setItemText(0, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.MovestackChoice.setItemText(1, QCoreApplication.translate("MainWindow", u"Parry", None))

        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Rolls or parries whenever you press C (activating bell)", None))
        self.AutoMantraVariantsDescriptor.setText(QCoreApplication.translate("MainWindow", u"Performs the special variant of a mantra activated by pressing F during windup", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Performs a roll when using a mantra", None))
        self.plainTextEdit_10.setPlainText("")
        self.plainTextEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Approximate ping, default is 100 (Shift + F3 to see ping)", None))
        self.AutoMantraVariants.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Mantra Variants </span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Ping</span></p></body></html>", None))
        self.AutoMantraVariantsKeysLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mantra Keys</span></p></body></html>", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numbers or letters separated by commas, like 1,2,e,3,z", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mantra Keys</span></p></body></html>", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numbers or letters separated by commas, like 1,2,e,3,z", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Screen Resolution</span></p></body></html>", None))
        self.AutoMantraVariantsKeysArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numbers or letters separated by commas, like 1,2,e,3,z", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Performs a slide when using a mantra while running", None))
        self.AutoRitualCast.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Ritual Casts</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mantra Slide Tech</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Mantra Keys</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Automatically activates all ritual casts.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mantra Roll Tech</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Screen Scale</span></p></body></html>", None))
        self.screenResolution.setItemText(0, QCoreApplication.translate("MainWindow", u"1128 x 634", None))
        self.screenResolution.setItemText(1, QCoreApplication.translate("MainWindow", u"1366 x 1768", None))
        self.screenResolution.setItemText(2, QCoreApplication.translate("MainWindow", u"1600x900", None))
        self.screenResolution.setItemText(3, QCoreApplication.translate("MainWindow", u"1600x1200", None))
        self.screenResolution.setItemText(4, QCoreApplication.translate("MainWindow", u"1920 x 1080", None))
        self.screenResolution.setItemText(5, QCoreApplication.translate("MainWindow", u"1920 x 1200", None))
        self.screenResolution.setItemText(6, QCoreApplication.translate("MainWindow", u"2560x1080", None))
        self.screenResolution.setItemText(7, QCoreApplication.translate("MainWindow", u"2560 x 1440", None))
        self.screenResolution.setItemText(8, QCoreApplication.translate("MainWindow", u"3440x1440", None))

        self.screenResolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your computer's screen resolution", None))
        self.screenScale.setItemText(0, QCoreApplication.translate("MainWindow", u"100%", None))
        self.screenScale.setItemText(1, QCoreApplication.translate("MainWindow", u"125%", None))

        self.screenScale.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your computer screen's scale (%)", None))
        self.MotifHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.HoldM1Key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The key you want to be spammed when m1 is held", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Roll Parry</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Does an air dash / roll in the middle of your aerial attack. Does not activate when you do not jump shortly before", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Automatically uppercuts, says mb all, and then assassinates a person when you press a key</span></p></body></html>", None))
        self.uppercutAssassinateHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to uppercut assassinate", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Presses Q when you press R</span></p></body></html>", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Roll M1s for you when you press a key</span></p></body></html>", None))
        self.rollParryHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to roll parry", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Key</span></p></body></html>", None))
        self.HoldM1Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Faster Hold M1</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Feint</span></p></body></html>", None))
        self.MotifToolbarNumberLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Motif Toolbar Number</span></p></body></html>", None))
        self.uppercutAssassinateLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Uppercut Assassinate</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Automatically spams any key when M1 is held (default `). The key MUST be binded to basic attack (you can have two keybinds at a time)", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Roll Uppercut</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Same as auto uppercut but doesn't trigger when you're running", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Uppercut</span></p></body></html>", None))
        self.plainTextEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The toolbar number of the weapon", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Feints for you when you press F</span></p></body></html>", None))
        self.RollM1Hotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to roll m1", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Roll M1</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Dynamic Uppercuts</span></p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Roll Crit</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Uppercuts as soon as you press ctrl", None))
        self.MotifToolbarNumberArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The toolbar number of the motif", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Quickly swaps your weapon's motif (the critical attack of your weapon) for you.", None))
        self.AerialAirDashLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Aerial M1 Dash</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Weapon Toolbar Number</span></p></body></html>", None))
        self.MotifSwapLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Motif Swap</span></p></body></html>", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Presses Q when you press a key (F will cause you to always roll parry)</span></p></body></html>", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Roll Cancel</span></p></body></html>", None))
        self.MotifHotkeyArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The key you want to press to swap motifs", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Right clicks when you press Q (may conflict with other macros)</span></p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bar Start Coordinates</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Make sure the Ankle Weights tool is equipped before starting", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Make sure the Boulder tool is held out before starting and you are near a campfire", None))
        self.AutoDropNotesBarStartCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the place where the circle starts at to fill in the above field", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bar End Coordinates</span></p></body></html>", None))
        self.AutoSellLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Sell</span></p></body></html>", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Confirmation Coordinates</span></p></body></html>", None))
        self.AutoBuySubmitCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the submit purchase button (X + space + Y)", None))
        self.AutoDropNotesHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to start dropping notes automatically", None))
        self.AutoSellBarEndCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the sell confirmation button (X + space + Y)", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Repetitions</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Sells soulbounded/enchanted/legendary weapons multiple times. Need to be talking to him already before activating", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Buys 5 bulk purchases of any item. Good for buying in bulk", None))
        self.AutoSellRepetitions.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount of items you want to sell", None))
        self.WillpowerTrainingHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey to start/stop training willpower", None))
        self.AnkleWeightsTrainingHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey to start/stop training agility", None))
        self.AutoDropNotesLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Drop Notes</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sell Button Coordinates</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.AutoSellHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to start selling automatically", None))
        self.AutoBuyBarStartCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the bar's start (X + space + Y)", None))
        self.AnkleWeightsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Agility Auto-train</span></p></body></html>", None))
        self.AutoSellBarStartCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the sell button (X + space + Y)", None))
        self.AutoBuyBarEndCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the end place you drag the circle to for max amount to fill in the above field", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Submit Button Coordinates</span></p></body></html>", None))
        self.AutoSellBarEndCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the sell confirmation button to fill in the above field", None))
        self.AutoBuyBarEndCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the bar's end (X + space + Y)", None))
        self.AutoDropNotesSubmitCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the submit button (X + space + Y)", None))
        self.CharismaAutofillLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Charisma Autofill</span></p></body></html>", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Submit Button Coordinates</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.AutoDropNotesRepetitions.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount of times you want to drop notes", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.autoSellBarStartCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the sell button to fill in the above field", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Type out part of the charisma line and it will finish it for you", None))
        self.autoDropNotesNoteCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the notes icon (X + space + Y)", None))
        self.AutoDropNotesBarEndCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the end place you drag the circle to for max amount to fill in the above field", None))
        self.AutoDropNotesBarStartCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the bar's start (X + space + Y)", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Repetitions</span></p></body></html>", None))
        self.autoDropNotesNoteCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the notes icon to fill in the above field", None))
        self.AutoDropNotesSubmitCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the submit button (confirm notes amount) to fill in the above field", None))
        self.AutoBuyHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to start auto buying", None))
        self.AutoBuyBarStartCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the place where the circle starts at to fill in the above field", None))
        self.WillpowerTrainingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Prayer Auto-train</span></p></body></html>", None))
        self.AutoDropNotesBarEndCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coordinates of the bar's end (X + space + Y )", None))
        self.BoulderTrainingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Boulder Auto-train</span></p></body></html>", None))
        self.BoulderTrainingHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey to start/stop training fortitude(boulder)", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Note Icon Coordinates</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Make sure the Prayer Beads tool is held out before starting", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Drops notes multiple times, good for trading", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bar Start Coordinates</span></p></body></html>", None))
        self.AutoBuyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Buy</span></p></body></html>", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Bar End Coordinates</span></p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.AutoBuySubmitCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the submit purchase button to fill in the above field", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Username</span></p></body></html>", None))
        self.plainTextEdit_14.setPlainText("")
        self.plainTextEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank if you do not want a custom one", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Found in Server Settings > Integrations > Webhooks", None))
        self.plainTextEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Message you want the bot to send", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Search Box Coordinates</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Profile Picture Link</span></p></body></html>", None))
        self.AutoEatFoodCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Where the food appears after you search it up (X + space + Y)", None))
        self.monitorToScreenshot.setPlainText(QCoreApplication.translate("MainWindow", u"1", None))
        self.monitorToScreenshot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Monitor number you want to screenshot", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Food Name</span></p></body></html>", None))
        self.plainTextEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leave blank if you do not want a custom one", None))
        self.FlashmapLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Flash Map</span></p></body></html>", None))
        self.AutoEatFoodName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full name of the food you want to eat", None))
        self.AutoEatFoodCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the food item to fill in the above field automatically", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Food Coordinates</span></p></body></html>", None))
        self.DiscordGankPingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Discord Message</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Useful to let people know where you are", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Eat</span></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Automatically sends a discord message when a key is pressed", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Monitor to Screenshot</span></p></body></html>", None))
        self.AutoEatBoxCoordsButton.setText(QCoreApplication.translate("MainWindow", u"Click me and click on the search box to fill in the above field automatically", None))
        self.plainTextEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to send the message", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Automatically opens up your inventory and eats a food. Inventory must not be open before using</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Keeps map open while holding m and then closes it when you release m", None))
        self.DiscordGankPingSettings.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Discord Webhook</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Take Screenshot</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Message</span></p></body></html>", None))
        self.AutoEatHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to start eating food ", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.AutoEatBoxCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Where you search for items (X + space + Y)", None))
        self.savePage.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit\n"
"{\n"
"color:grey;\n"
"background-color:transparent;\n"
"}\n"
"QLineEdit:disabled{\n"
"color:white;\n"
"}\n"
"", None))
        self.Preset10Name.setText(QCoreApplication.translate("MainWindow", u"Preset 10", None))
        self.Preset7Save.setText("")
        self.Preset9EditName.setText("")
        self.Preset1EditName.setText("")
        self.Preset5Save.setText("")
        self.Preset4Name.setText(QCoreApplication.translate("MainWindow", u"Preset 4", None))
        self.Preset1Name.setText(QCoreApplication.translate("MainWindow", u"Preset 1", None))
        self.Preset3Save.setText("")
        self.Preset9Save.setText("")
        self.Preset3Name.setText(QCoreApplication.translate("MainWindow", u"Preset 3", None))
        self.Preset7Name.setText(QCoreApplication.translate("MainWindow", u"Preset 7", None))
        self.Preset4Load.setText("")
        self.Preset8Name.setText(QCoreApplication.translate("MainWindow", u"Preset 8", None))
        self.Preset8Load.setText("")
        self.Preset4Save.setText("")
        self.Preset7EditName.setText("")
        self.Preset3Load.setText("")
        self.Preset2Load.setText("")
        self.Preset5Name.setText(QCoreApplication.translate("MainWindow", u"Preset 5", None))
        self.Preset10EditName.setText("")
        self.Preset7Load.setText("")
        self.Preset5EditName.setText("")
        self.Preset6Save.setText("")
        self.Preset8EditName.setText("")
        self.Preset8Save.setText("")
        self.Preset10Save.setText("")
        self.Preset5Load.setText("")
        self.Preset1Load.setText("")
        self.Preset9Load.setText("")
        self.Preset9Name.setText(QCoreApplication.translate("MainWindow", u"Preset 9", None))
        self.Preset4EditName.setText("")
        self.Preset2Name.setText(QCoreApplication.translate("MainWindow", u"Preset 2", None))
        self.Preset1Save.setText("")
        self.Preset10Load.setText("")
        self.Preset6Load.setText("")
        self.Preset2Save.setText("")
        self.Preset6Name.setText(QCoreApplication.translate("MainWindow", u"Preset 6", None))
        self.Preset3EditName.setText("")
        self.Preset6EditName.setText("")
        self.Preset2EditName.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Note: If you load a preset and change it, it will NOT automatically save.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Presets</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Activates / deactivates all toggled macros", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Activates / deactivates macros with a keypress instead of having to click the toggle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Activate Macros</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Activate Macros Hotkey</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Keybind to toggle the macros </span></p></body></html>", None))
        self.themeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dark", None))
        self.themeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Navy Blue", None))

        self.themeLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Theme</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"When something togglable is used, such as \"Toggle Activate Macros\", a small popup will be activated in the bottom right of the screen", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Changes the theme of the application</p></body></html>", None))
        self.toggleNotifsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Toggle Notifications</span></p></body></html>", None))
        self.autoSprintLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Sprint</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Automatically starts sprinting after either Golden Tongue or Custom Chat Hotkey is used</span></p></body></html>", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.TrashTalkHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to trash talk", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.GoldenTongueLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Golden Tongue</span></p></body></html>", None))
        self.plainTextEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 1</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 2</span></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 3</span></p></body></html>", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 4</span></p></body></html>", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 5</span></p></body></html>", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 6</span></p></body></html>", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 7</span></p></body></html>", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 8</span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 9</span></p></body></html>", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.MessageHotkeyLabel10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Message Hotkey 10</span></p></body></html>", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and types whatever you want when you press a hotkey", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.MessageHotkeyArea_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Text</span></p></body></html>", None))
        self.MessageArea_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Thing you want to say (can be a sentence)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.GoldenTongueHotkeyArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say your thing", None))
        self.TrashTalkLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Trash Talk Hotkey</span></p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Automatically trash talks</span></p></body></html>", None))
        self.autoLogLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Log</span></p></body></html>", None))
        self.autoLogHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to log", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Automatically logs/leaves from the server when a button is pressed</span></p></body></html>", None))
        self.autoLogCoordButton.setText(QCoreApplication.translate("MainWindow", u"Click me and then click the log button to fill in the above field automatically", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Leaves crouch automatically afterwards", None))
        self.AutoTacetLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Auto Tacet</span></p></body></html>", None))
        self.AutoUncrouchLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Auto Uncrouch</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Log Button Coordinates</span></p></body></html>", None))
        self.autoLogCoords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X coordinate + space + Y coordinate", None))
        self.MbAllHotkeyArea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to say mb all", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Automatically opens the chat and says mb all whenever you press the hotkey", None))
        self.MbAllDropdown.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Automatically enables tacet", None))
        self.MbAllLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Mb All </span></p></body></html>", None))
        self.autoTacetKeybind.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key to be pressed to activate tacet automatically", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Keybind</span></p></body></html>", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Flow state</span></p></body></html>", None))
        self.AnkleCutterHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to do ankle cutter", None))
        self.MayhemLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\"> Mayhem</span></p></body></html>", None))
        self.RisingStarLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Rising Star</span></p></body></html>", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Automatically does relentless hunt when you press the hotkey", None))
        self.RelentlessHuntHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Flowstate</span></p></body></html>", None))
        self.FlowStateKeybind.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Flow state keybind", None))
        self.FlowStateKeybind_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Flow state keybind", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Automatically does Mayhem when you press the hotkey", None))
        self.AnkleCutterLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Ankle Cutter</span></p></body></html>", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Flow state</span></p></body></html>", None))
        self.RelentlessHuntLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Relentless Hunt</span></p></body></html>", None))
        self.RelentlessHuntHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to do relentless hunt", None))
        self.MayhemHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to do mayhem", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Automatically does Ankle Cutter when you press the hotkey", None))
        self.FlowStateKeybind_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Flow state keybind", None))
        self.AnkleCutterHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.RisingStarHotkey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key you want to press to do rising star", None))
        self.MayhemHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.RisingStarHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hotkey</span></p></body></html>", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Automatically does Rising Star when you press the hotkey", None))
        self.FlowStateKeybind_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Flow state keybind", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Flow state</span></p></body></html>", None))
        self.progressionButton.setText("")
        self.chatButton.setText("")
        self.combatButton.setText("")
        self.saveButton.setText("")
        self.bellButton.setText("")
        self.playButton.setText("")
        self.settingsButton.setText("")
        self.mantrasButton.setText("")
        self.weaponsButton.setText("")
        self.silentheartButton.setText("")
        self.miscButton.setText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#808080;\">For new versions: </span><a href=\"https://github.com/swinelike/DeepWarden\"><span style=\" font-size:10pt; text-decoration: underline; color:#99ebff;\">https://github.com/swinelike/DeepWarden</span></a></p></body></html>", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#808080;\">For support, DM me:</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"pigyboi", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#808080;\">or join </span><a href=\"https://discord.com/invite/Wg5ccj6vE6\"><span style=\" font-size:10pt; text-decoration: underline; color:#99ebff;\">this discord server</span></a></p></body></html>", None))
    # retranslateUi









               
































        print('importing macros')
        from macros.rolling import rollCrit, rollM1, rollParry
        from macros.training import autocharisma, autofortitude, autoagility, autowillpower
        from macros import threadedkeyb, holdm1, autovariants, mball, goldentongue, motifswap, gankpinger, flashmap, autofeint, autoritualcast, autotacet, autotrashtalk, autolog, autoeat, uppercutAssassinate, autobuy, autodropnotes, autosell, autorollcancel
        from macros.bellStack import bellStackParry, bellStackDodge
        from macros.mantraTech import mantraTechRoll, mantraTechSlide
        from macros.uppercuts import autoUppercutAlways, autoUppercutDYNAMIC
        from macros.silentheart import anklecutter, mayhem, relentlesshunt, risingstar
        from functions.getpixels import get_pos
        print('macros imported')
        # talents, bells, mantras, weapons, movement, progression, misc, settings
        self.bellButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mantrasButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.weaponsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.progressionButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.miscButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        #self.movementButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.saveButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.playButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.settingsButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(8))
        self.chatButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.combatButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(10))
        self.silentheartButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(11))
        def changeBarVis():
            if self.menuBar.isVisible():
                self.menuBar.hide()
            elif self.menuBar.isHidden():
                self.menuBar.show()
        self.menuButton.clicked.connect(changeBarVis)
        self.screenResolution.setCurrentIndex(3)
        def set_pos(element):
               coords = get_pos()
               element.setPlainText(str(coords[0]) + ' ' + str(coords[1]))
        self.autoLogCoordButton.clicked.connect(lambda: set_pos(self.autoLogCoords))
        self.AutoEatBoxCoordsButton.clicked.connect(lambda: set_pos(self.AutoEatBoxCoords))
        self.AutoEatFoodCoordsButton.clicked.connect(lambda: set_pos(self.AutoEatFoodCoords))
        self.AutoBuyBarStartCoordsButton.clicked.connect(lambda: set_pos(self.AutoBuyBarStartCoords))
        self.AutoBuyBarEndCoordsButton.clicked.connect(lambda: set_pos(self.AutoBuyBarEndCoords))
        self.AutoBuySubmitCoordsButton.clicked.connect(lambda: set_pos(self.AutoBuySubmitCoords))
        self.autoDropNotesNoteCoordsButton.clicked.connect(lambda:set_pos(self.autoDropNotesNoteCoords))
        self.AutoDropNotesBarStartCoordsButton.clicked.connect(lambda: set_pos(self.AutoDropNotesBarStartCoords))
        self.AutoDropNotesBarEndCoordsButton.clicked.connect(lambda: set_pos(self.AutoDropNotesBarEndCoords))
        self.AutoDropNotesSubmitCoordsButton.clicked.connect(lambda: set_pos(self.AutoDropNotesSubmitCoords))
        self.autoSellBarStartCoordsButton.clicked.connect(lambda: set_pos(self.AutoSellBarStartCoords))
        self.AutoSellBarEndCoordsButton.clicked.connect(lambda: set_pos(self.AutoSellBarEndCoords))

        self.bellButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Bells</span></p></body></html>", None)))
        self.mantrasButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Mantras</span></p></body></html>", None)))
        self.weaponsButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Weapons</span></p></body></html>", None)))
        self.progressionButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Progression</span></p></body></html>", None)))
        self.miscButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Miscellaneous</span></p></body></html>", None)))
        #self.movementButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Movement</span></p></body></html>", None)))
        self.saveButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Save</span></p></body></html>", None)))
        self.playButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Run</span></p></body></html>", None)))
        self.settingsButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Settings</span></p></body></html>", None)))
        self.chatButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Chat</span></p></body></html>", None)))
        self.combatButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Combat</span></p></body></html>", None)))
        self.silentheartButton.clicked.connect(lambda: self.pageName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Silentheart</span></p></body></html>", None)))

        #! Toggles
        #!BELLS
        self.BellMovestackToggle = CustomToggle(self.bellPage)
        self.gridLayout_5.addWidget(self.BellMovestackToggle, 0, 1, 1, 2)

        #!MANTRAS
        self.RitualCastToggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.RitualCastToggle, 0,1,1,1)
        self.mantraVariantToggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.mantraVariantToggle, 5, 1, 1, 1)
        self.mantraTechRollToggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.mantraTechRollToggle, 11,1,1,2)
        self.mantraTechSlidetoggle = CustomToggle(self.mantrasPage)
        self.gridLayout_6.addWidget(self.mantraTechSlidetoggle, 8,1,1,2)



        # label 9 = mantra roll label 7 = mantra slide
        # AutoMantraVariantsKeysArea


        #! WEAPONS
        #toggles
        self.AirDashToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.AirDashToggle, 0,1,1,2)
        self.HoldM1Toggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.HoldM1Toggle, 2,1,1,2)
        self.MotifSwapToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.MotifSwapToggle, 5,1,1,2)
        self.uppercutToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.uppercutToggle, 10,1,1,1)
        self.uppercutDynamicToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.uppercutDynamicToggle, 12,1,1,1)
        self.rollUppercutToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.rollUppercutToggle, 14,1,1,1)
        self.autoFeintToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.autoFeintToggle, 15,1,1,1)
        self.rollM1Toggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.rollM1Toggle, 17,1,1,1)
        self.rollCritToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.rollCritToggle, 20,1,1,1)
        self.rollParryToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.rollParryToggle, 22,1,1,1)
        self.uppercutAssassinateToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.uppercutAssassinateToggle, 25,1,1,1)
        self.AutoRollCancelToggle = CustomToggle(self.weaponsPage)
        self.scrollAreaWidgetContents_3.layout().addWidget(self.AutoRollCancelToggle, 28, 1, 1, 1)



        #functions

        #!RUNNING
        self.RunToggle = CustomToggle(self.runPage)
        self.gridLayout_14.addWidget(self.RunToggle, 0,1,1,2)
        self.RunKeybindToggle = CustomToggle(self.runPage)
        self.gridLayout_14.addWidget(self.RunKeybindToggle, 2, 1, 1, 1)



        #! MISCELLANEOUS

        self.GankPingerToggle = CustomToggle(self.miscPage)
        self.scrollAreaWidgetContents_2.layout().addWidget(self.GankPingerToggle, 0,1,1,1)
        self.ScreenshotToggle = CustomToggle(self.miscPage)
        self.scrollAreaWidgetContents_2.layout().addWidget(self.ScreenshotToggle, 7,1,1,1)
        self.FlashMapToggle = CustomToggle(self.miscPage)
        self.scrollAreaWidgetContents_2.layout().addWidget(self.FlashMapToggle, 10,1,1,2)
        self.AutoEatToggle = CustomToggle(self.miscPage)
        self.scrollAreaWidgetContents_2.layout().addWidget(self.AutoEatToggle, 12, 1, 1, 2)

        #! CHAT

        self.GoldenTongueToggle = CustomToggle(self.chatPage)
        self.gridLayout_16.addWidget(self.GoldenTongueToggle, 0, 1, 1, 1)
        self.TrashTalkToggle = CustomToggle(self.chatPage)
        self.gridLayout_16.addWidget(self.TrashTalkToggle, 5, 1, 1, 1)


        self.MessageToggle_1 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_1, 0, 1, 1, 1)
        self.MessageToggle_2 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_2, 4, 1, 1, 1)
        self.MessageToggle_3 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_3, 8, 1, 1, 1)
        self.MessageToggle_4 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_4, 12, 1, 1, 1)
        self.MessageToggle_5 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_5, 16, 1, 1, 1)
        self.MessageToggle_6 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_6, 20, 1, 1, 1)
        self.MessageToggle_7 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_7, 24, 1, 1, 1)
        self.MessageToggle_8 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_8, 28, 1, 1, 1)
        self.MessageToggle_9 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_9, 32, 1, 1, 1)
        self.MessageToggle_10 = CustomToggle(self.chatPage)
        self.scrollAreaWidgetContents_5.layout().addWidget(self.MessageToggle_10, 36, 1, 1, 1)



        

        #!PROGRESSION
        self.CharismaAutofillToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.CharismaAutofillToggle, 0,1,1,1)
        self.AutoAgilityToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.AutoAgilityToggle, 2,1,1,1)
        self.AutoFortitudeToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.AutoFortitudeToggle, 5,1,1,1)
        self.AutoWillpowerToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.AutoWillpowerToggle, 8,1,1,1)
        self.AutoBuyToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.AutoBuyToggle, 11,1,1,1)

        self.AutoDropNotesToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.AutoDropNotesToggle, 20,1,1,1)

        self.AutoSellToggle = CustomToggle(self.progressionPage)
        self.scrollAreaWidgetContents_6.layout().addWidget(self.AutoSellToggle, 32, 1, 1, 1)

        

        #! COMBAT
 
        self.MbAllToggle = CustomToggle(self.combatPage)
        self.gridLayout_18.addWidget(self.MbAllToggle, 0, 1, 1, 3)
        self.AutoLogToggle = CustomToggle(self.combatPage)
        self.gridLayout_18.layout().addWidget(self.AutoLogToggle, 3,1,1,3)
        self.tacetToggle = CustomToggle(self.combatPage)
        self.gridLayout_18.addWidget(self.tacetToggle, 9,1,1,3)
        self.uncrouchToggle = CustomToggle(self.combatPage)
        self.gridLayout_18.addWidget(self.uncrouchToggle, 13,1,1,3)

        #! SILENTHEART
        self.RelentlessHuntToggle = CustomToggle(self.silentheartPage)
        self.gridLayout_22.addWidget(self.RelentlessHuntToggle, 0, 1, 1, 1)
        self.MayhemToggle = CustomToggle(self.silentheartPage)
        self.gridLayout_22.addWidget(self.MayhemToggle, 4, 1, 1, 1)

        self.RisingStarToggle = CustomToggle(self.silentheartPage)
        self.gridLayout_22.addWidget(self.RisingStarToggle, 8, 1, 1, 1)

        self.AnkleCutterToggle = CustomToggle(self.silentheartPage)
        self.gridLayout_22.addWidget(self.AnkleCutterToggle, 13, 1, 1, 1)

        #! SETTINGS
        self.toggleNotifsToggle = CustomToggle(self.settingsPage)
        self.gridLayout_7.addWidget(self.toggleNotifsToggle, 0,1,1,1)
        self.autoSprintToggle = CustomToggle(self.settingsPage)
        self.gridLayout_7.addWidget(self.autoSprintToggle, 4, 1, 1, 1)

        self.toggles = [
                self.BellMovestackToggle,

                self.mantraVariantToggle,
                self.mantraTechRollToggle,
                self.mantraTechSlidetoggle,
                self.RitualCastToggle,

                self.AirDashToggle,
                self.HoldM1Toggle,
                self.MotifSwapToggle,
                self.uppercutToggle,
                self.uppercutDynamicToggle,
                self.rollUppercutToggle,
                self.autoFeintToggle,
                self.rollM1Toggle,
                self.rollCritToggle,
                self.rollParryToggle,
                self.AutoRollCancelToggle,


                self.GankPingerToggle,
                self.ScreenshotToggle,
                self.AutoLogToggle,
                self.AutoEatToggle,

                self.MbAllToggle,
                self.GoldenTongueToggle,
                self.MessageToggle_1,
                self.MessageToggle_2,
                self.MessageToggle_3,
                self.MessageToggle_4,
                self.MessageToggle_5,
                self.MessageToggle_6,
                self.MessageToggle_7,
                self.MessageToggle_8,
                self.MessageToggle_9,
                self.MessageToggle_10,
                self.TrashTalkToggle,

                self.tacetToggle,
                self.uncrouchToggle,

                self.CharismaAutofillToggle,
                self.AutoAgilityToggle,
                self.AutoFortitudeToggle,
                self.AutoWillpowerToggle,
                self.AutoBuyToggle,
                self.AutoDropNotesToggle,
                self.AutoSellToggle,

                self.RelentlessHuntToggle,
                self.MayhemToggle,
                self.RisingStarToggle,
                self.AnkleCutterToggle
        ]
        
        for toggle in self.toggles:
                toggle.toggled.connect(lambda: self.RunToggle.setChecked(False))
        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
        settingsPath = os.path.join(dataLocation, 'data/Settings.json') 
        with open(settingsPath) as f:
                currentInfo = json.load(f)
                if currentInfo['notifs']:
                        self.toggleNotifsToggle.setChecked(True)
                elif not currentInfo['notifs']:
                       self.toggleNotifsToggle.setChecked(False)
                if 'autoSprint' not in currentInfo or not currentInfo['autoSprint']:
                        self.autoSprintToggle.setChecked(False)
                else:
                       self.autoSprintToggle.setChecked(True)




        #! conditional toggles
        def disableDynUp():
               if self.uppercutToggle._is_checked == 2:
                      self.uppercutDynamicToggle.setChecked(False)
        def disableNormUp():
               if self.uppercutDynamicToggle._is_checked == 2:
                      self.uppercutToggle.setChecked(False)
        self.uppercutToggle.toggled.connect(disableDynUp)
        self.uppercutDynamicToggle.toggled.connect(disableNormUp)

        def toggleNotifs():
                if self.toggleNotifsToggle._is_checked == 2: 
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        f.close()
                        currentSettings['notifs'] = True
                        with open(settingsPath, 'w') as f:
                               json.dump(currentSettings, f)
                if self.toggleNotifsToggle._is_checked == 0:
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        f.close()
                        currentSettings['notifs'] = False
                        with open(settingsPath, 'w') as f:
                               json.dump(currentSettings, f)
        self.toggleNotifsToggle.toggled.connect(toggleNotifs)

        def toggleAutoSprint():
                if self.autoSprintToggle._is_checked == 2: 
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        f.close()
                        currentSettings['autoSprint'] = True
                        with open(settingsPath, 'w') as f:
                               json.dump(currentSettings, f)
                if self.autoSprintToggle._is_checked == 0:
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        f.close()
                        currentSettings['autoSprint'] = False
                        with open(settingsPath, 'w') as f:
                               json.dump(currentSettings, f)
        self.autoSprintToggle.toggled.connect(toggleAutoSprint)

                                                      


        def show_warning(title='', text=''):
                # configurations
                toast = Toast(self.centralwidget)
                toast.setStayOnTop(True)
                toast.setDuration(10000)  # 3 seconds
                toast.setTitle(title)
                toast.setText(text)
                toast.setResetDurationOnHover(False)
                toast.setMaximumOnScreen(10)
                toast.setFixedWidth(400)
                
                
                # style preset
                toast.applyPreset(ToastPreset.WARNING)

                # background color
                toast.setBackgroundColor(QColor("#333333"))  # Use QColor instead of string
                
                # stylesheet
                toast.setStyleSheet("""
                QWidget {
                        background-color: #333333;  /* Dark gray background */
                        border: 0px solid #555555;  /* Light gray border */
                        border-radius: 5px;         /* Rounded corners */
                        color: #ffffff
                }
                
                """)

                # Show the toast
                toast.setTitleColor(QColor("#D3D3D3"))
                toast.setTextColor(QColor("#D3D3D3"))
                toast.setCloseButtonIconColor(QColor("#ff073a"))
                toast.setBorderRadius(5)
                toast.show()
                             
        def runToggle():
                def addMacro(name:str, toggle, listener_class, **run_kwargs):
                        if toggle._is_checked != 2:
                               return
                        print(run_kwargs)
                        exceptions = ['ping_ms', 'keyToPress', 'avatar_url', 'username']
                        for field, value in run_kwargs.items():
                               if type(value) is str:
                                      if len(value) == 0 and field not in exceptions:
                                        show_warning(f'Error in macro {name}', 'This macro is missing one or more parameters and was not enabled')
                                        return
                        listener_instance = listener_class()
                        setattr(self, name, listener_instance)
                        self.threads.append(listener_instance)
                        thread = Thread(
                                        target=lambda: listener_instance.run(**run_kwargs),
                                        name=f"{name} Thread"
                        )
                        thread.daemon = True
                        thread.start()
                if self.RunToggle._is_checked == 2:  # is checked
                        self.threads = []       
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                        with open(settingsPath) as f:
                                currentSettings = json.load(f)
                        addMacro('Air Dash M1 Movestack', self.AirDashToggle, threadedkeyb.AirListener)
                        addMacro('Faster Hold M1', self.HoldM1Toggle, holdm1.M1Listener, keyToPress=self.HoldM1Key.toPlainText())
                        if self.BellMovestackToggle._is_checked == 2:
                                if self.MovestackChoice.currentIndex() == 1:     
                                        addMacro('Bell Stack Parry', self.BellMovestackToggle, bellStackParry.BellStackParryListener) # Either a logic error or i need to fix some jank on this one
                                elif self.MovestackChoice.currentIndex() == 0:
                                        addMacro('Bell Stack Dodge', self.BellMovestackToggle, bellStackDodge.BellStackDodgeListener)
                        addMacro('Mantra Roll Tech', self.mantraTechRollToggle, mantraTechRoll.MantraRollTechListener, keybinds=self.plainTextEdit_3.toPlainText())
                        addMacro('Mantra Slide Tech', self.mantraTechSlidetoggle, mantraTechSlide.MantraSlideTechListener, keybinds=self.plainTextEdit_2.toPlainText())
                        addMacro('Mb All', self.MbAllToggle, mball.MbAllListener, keybind=self.MbAllHotkeyArea.toPlainText())
                        addMacro('Golden Tongue', self.GoldenTongueToggle, goldentongue.GoldenTongueListener, keybind=self.GoldenTongueHotkeyArea.toPlainText(), content=self.plainTextEdit_6.toPlainText(), autosprint=currentSettings['autoSprint'])

                        addMacro('Mantra Variants', self.mantraVariantToggle, autovariants.MantraVariantListener, keybinds=self.AutoMantraVariantsKeysArea.toPlainText())
                        #To test:
                        addMacro('Motif Swap', self.MotifSwapToggle, motifswap.MotifSwapListener, keybind=self.MotifHotkeyArea.toPlainText(), motifnum=self.MotifToolbarNumberArea.toPlainText(), weaponnum=self.plainTextEdit_7.toPlainText())
                        filepath = os.path.dirname(os.path.abspath(__file__))
                        templatepath = os.path.join(filepath, 'assets/letter_templates')
                        addMacro('Ritual Cast', self.RitualCastToggle, autoritualcast.RitualCastListener, ping_ms=self.plainTextEdit_10.toPlainText(), basepath=templatepath, scale=self.screenScale.currentIndex(), resolution=self.screenResolution.currentIndex())
                        addMacro('Charisma Autofill', self.CharismaAutofillToggle, autocharisma.autoCharismaListener)
                        addMacro('Auto Fortitude', self.AutoFortitudeToggle, autofortitude.AutoFortitudeListener, keybind=self.BoulderTrainingHotkey.toPlainText())
                        addMacro('Auto Willpower', self.AutoWillpowerToggle, autowillpower.AutoWillpowerListener, keybind=self.WillpowerTrainingHotkey.toPlainText())

                        addMacro('Auto Agility', self.AutoAgilityToggle, autoagility.AutoAgilityListener, keybind=self.AnkleWeightsTrainingHotkey.toPlainText())
                        addMacro('Gank Pinger', self.GankPingerToggle, gankpinger.GankPingListener, hotkey=self.plainTextEdit_15.toPlainText(),  webhook_url=self.plainTextEdit.toPlainText(), message=self.plainTextEdit_12.toPlainText(), username=self.plainTextEdit_13.toPlainText(), avatar_url=self.plainTextEdit_14.toPlainText(), takeimage=(self.ScreenshotToggle._is_checked == 2), monitornumber=self.monitorToScreenshot.toPlainText())
                        addMacro('Auto Uppercut', self.uppercutToggle, autoUppercutAlways.UppercutListener)
                        addMacro('Dynamic Auto Uppercut', self.uppercutDynamicToggle, autoUppercutDYNAMIC.DynamicUppercutListener, toRoll=(self.rollUppercutToggle._is_checked == 2))
                        addMacro('Auto Feint', self.autoFeintToggle, autofeint.autoFeintListener)
                        addMacro('Flash Map', self.FlashMapToggle, flashmap.flashMapListener)
                        addMacro('Tacet Toggle', self.tacetToggle,  autotacet.autoTacetListener, keybind=self.autoTacetKeybind.toPlainText(), uncrouch=(self.uncrouchToggle._is_checked == 2))        

                        addMacro('Message Hotkey', self.MessageToggle_1, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_1.toPlainText(), content=self.MessageArea_1.toPlainText(), autosprint=currentSettings['autoSprint'])  
                        addMacro('Message Hotkey 2', self.MessageToggle_2, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_2.toPlainText(), content=self.MessageArea_2.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_3, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_3.toPlainText(), content=self.MessageArea_3.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_4, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_4.toPlainText(), content=self.MessageArea_4.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_5, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_5.toPlainText(), content=self.MessageArea_5.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_6, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_6.toPlainText(), content=self.MessageArea_6.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_7, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_7.toPlainText(), content=self.MessageArea_7.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_8, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_8.toPlainText(), content=self.MessageArea_8.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_9, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_9.toPlainText(), content=self.MessageArea_9.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        addMacro('Message Hotkey 2', self.MessageToggle_10, goldentongue.GoldenTongueListener, keybind=self.MessageHotkeyArea_10.toPlainText(), content=self.MessageArea_10.toPlainText(), autosprint=currentSettings['autoSprint']) 
                        txtpath = os.path.join(filepath, 'assets', 'trashtalks.txt') 
                        addMacro('Trash Talk', self.TrashTalkToggle, autotrashtalk.TrashTalkListener, keybind=self.TrashTalkHotkey.toPlainText(), txtpath=txtpath)
                        addMacro('Auto Log', self.AutoLogToggle, autolog.AutoLogListener, keybind=self.autoLogHotkey.toPlainText(), coordinates=self.autoLogCoords.toPlainText())
                        addMacro('Auto Eat', self.AutoEatToggle, autoeat.AutoEatListener, keybind=self.AutoEatHotkey.toPlainText(), foodname=self.AutoEatFoodName.toPlainText(), boxcoordinates=self.AutoEatBoxCoords.toPlainText(), foodcoordinates=self.AutoEatFoodCoords.toPlainText())
                        addMacro('Roll M1', self.rollM1Toggle, rollM1.rollM1Listener, keybind=self.RollM1Hotkey.toPlainText())
                        addMacro('Roll Crit', self.rollCritToggle, rollCrit.rollCritListener)
                        addMacro('Roll Parry', self.rollParryToggle, rollParry.rollParryListener, keybind=self.rollParryHotkey.toPlainText())
                        addMacro('Uppercut Assassinate', self.uppercutAssassinateToggle, uppercutAssassinate.uppercutAssassinateListener, keybind=self.uppercutAssassinateHotkey.toPlainText())
                        addMacro('Auto Buy', self.AutoBuyToggle, autobuy.AutoBuyListener, keybind=self.AutoBuyHotkey.toPlainText(), submitcoordinates=self.AutoBuySubmitCoords.toPlainText(), startcoordinates=self.AutoBuyBarStartCoords.toPlainText(), endcoordinates=self.AutoBuyBarEndCoords.toPlainText())
                        addMacro('Auto Drop Notes', self.AutoDropNotesToggle, autodropnotes.AutoDropNotesListener, keybind=self.AutoDropNotesHotkey.toPlainText(), repetitions=self.AutoDropNotesRepetitions.toPlainText(), notecoordinates=self.autoDropNotesNoteCoords.toPlainText(), startcoordinates=self.AutoDropNotesBarStartCoords.toPlainText(), endcoordinates=self.AutoDropNotesBarEndCoords.toPlainText(), confirmationcoordinates=self.AutoDropNotesSubmitCoords.toPlainText())
                        addMacro('Auto Sell', self.AutoSellToggle, autosell.AutoSellListener, keybind=self.AutoSellHotkey.toPlainText(), repetitions=self.AutoSellRepetitions.toPlainText(), itemcoordinates=self.AutoSellBarStartCoords.toPlainText(), confirmationcoordinates=self.AutoSellBarEndCoords.toPlainText())
                        addMacro('Relentless Hunt', self.RelentlessHuntToggle, relentlesshunt.relentlessHuntListener, keybind=self.RelentlessHuntHotkey.toPlainText(), flowstatekeybind=self.FlowStateKeybind.toPlainText())
                        addMacro('Mayhem', self.MayhemToggle, mayhem.mayhemListener, keybind=self.MayhemHotkey.toPlainText(), flowstatekeybind=self.FlowStateKeybind_2.toPlainText())
                        addMacro('Rising Star', self.RisingStarToggle, risingstar.risingStarListener, keybind=self.RisingStarHotkey.toPlainText(), flowstatekeybind=self.FlowStateKeybind_3.toPlainText())
                        addMacro('Ankle Cutter', self.AnkleCutterToggle, anklecutter.ankleCutterListener, keybind=self.AnkleCutterHotkey.toPlainText(), flowstatekeybind=self.FlowStateKeybind_4.toPlainText())
                        addMacro('Auto Feint', self.AutoRollCancelToggle, autorollcancel.rollCancelListener)

                        



                else:
                        print('start')
                        try:
                                for thread in self.threads:
                                        thread.stop()
                                        print('stopped ' + thread.__class__.__name__)
                                self.threads = []  # Clear thread list
                                print('RAN')
                        except Exception as e:
                                print(f'Error stopping {thread}: {e}')
                        

                        
                        

        def show_toast(title='', text=''):
                # configurations
                toast = Toast(self.centralwidget)
                toast.setStayOnTop(True)
                toast.setDuration(3000)  # 3 seconds
                toast.setTitle(title)
                toast.setText(text)
                toast.setResetDurationOnHover(False)
                
                # style preset
                toast.applyPreset(ToastPreset.SUCCESS)

                # background color
                toast.setBackgroundColor(QColor("#333333"))  # Use QColor instead of string
                
                # stylesheet
                toast.setStyleSheet("""
                QWidget {
                        background-color: #333333;  /* Dark gray background */
                        border: 0px solid #555555;  /* Light gray border */
                        border-radius: 5px;         /* Rounded corners */
                        color: #ffffff
                }
                
                """)

                # Show the toast
                toast.setTitleColor(QColor("#D3D3D3"))
                toast.setTextColor(QColor("#D3D3D3"))
                toast.setCloseButtonIconColor(QColor("#ff073a"))
                toast.setBorderRadius(5)
                toast.show()
        self.RunToggle.toggled.connect(runToggle)
        def notifs():
                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                settingsPath = os.path.join(dataLocation, 'data/Settings.json')
                with open(settingsPath) as f:
                        currentSettings = json.load(f)
                if currentSettings['notifs']:
                        if self.RunToggle._is_checked == 2:
                               show_toast(title='Macro activated!')
                        elif self.RunToggle._is_checked == 0:
                               show_toast(title='Macro disabled.')
                else:
                       print('notif would have been played if not disabled')
        self.RunToggle.toggled.connect(notifs)
        def toggling():
                def on_key(event):
                        if event.name == self.plainTextEdit_17.toPlainText():
                                if self.RunToggle._is_checked == 2:
                                        self.RunToggle.setChecked(False)
                                elif self.RunToggle._is_checked == 0:
                                        self.RunToggle.setChecked(True)
                keyboard.on_press(on_key)
                
                # Keep the thread alive
                while True:
                        sleep(0.1)  # Prevent high CPU usage

        def startStopToggling():
                global t1  # Make thread accessible globally
                if self.RunKeybindToggle._is_checked == 2:
                        t1 = threading.Thread(target=toggling)
                        t1.daemon = True
                        t1.start()
                elif self.RunKeybindToggle._is_checked == 0:
                        print('disabling hotkeys')
                        keyboard.unhook_all()

        self.RunKeybindToggle.toggled.connect(startStopToggling)


        
        #! saving mechanism (fuck this)

        def saveCurrentData(number):

                currentData = {}
                def saveMacro(currentData, toggleName, params=None, elements=None):
                        element = getattr(self, toggleName)
                        if element._is_checked == 2:
                                currentData[toggleName] = True
                                if params and elements:
                                       for i in range(len(params)):
                                              parameterName = params[i]
                                              elementName = getattr(self, elements[i])
                                              currentData[parameterName] = elementName.toPlainText()
                        else:
                                currentData[toggleName] = False
                        
                       
                #!bells
                if self.BellMovestackToggle._is_checked == 2:
                        currentData['BellMovestackToggle'] = True
                        currentData['MovestackChoice'] = self.MovestackChoice.currentIndex()
                else:
                       currentData['BellMovestackToggle'] = False

                #!mantras
                if self.RitualCastToggle._is_checked == 2:
                       currentData['RitualCastToggle'] = True
                       currentData['ritualCastPing'] = self.plainTextEdit_10.toPlainText()
                       currentData['screenResolution'] = self.screenResolution.currentIndex()
                       currentData['screenScale'] = self.screenScale.currentIndex()
                else:
                       currentData['RitualCastToggle'] = False


                saveMacro(currentData, 'mantraVariantToggle', params=['AutoMantraVariantsKeysArea'], elements=['AutoMantraVariantsKeysArea'])
                saveMacro(currentData, 'mantraTechSlidetoggle', params=['mantraTechSlidetoggleKeysArea'], elements=['plainTextEdit_2'])
                saveMacro(currentData, 'mantraTechRollToggle', params=['mantraTechRollToggleKeysArea'], elements=['plainTextEdit_3'])

                #!weapons

                saveMacro(currentData, 'AirDashToggle')
                saveMacro(currentData, 'HoldM1Toggle')
                saveMacro(currentData, 'MotifSwapToggle', params=['MotifHotkeyArea', 'MotifToolbarNumberArea', 'MotifWeaponNumberArea'], elements=['MotifHotkeyArea', 'MotifToolbarNumberArea', 'plainTextEdit_7'])
                saveMacro(currentData, 'uppercutToggle')
                saveMacro(currentData, 'uppercutDynamicToggle')
                saveMacro(currentData, 'rollUppercutToggle')
                saveMacro(currentData, 'autoFeintToggle')
                saveMacro(currentData, 'rollM1Toggle', params=['RollM1Hotkey'], elements=['RollM1Hotkey'])
                saveMacro(currentData, 'rollCritToggle')
                saveMacro(currentData, 'rollParryToggle', params=['rollParryHotkey'], elements=['rollParryHotkey'])
                saveMacro(currentData, 'uppercutAssassinateToggle', params=['uppercutAssassinateHotkey'], elements=['uppercutAssassinateHotkey'])
                saveMacro(currentData, 'AutoRollCancelToggle')

                #! misc
                saveMacro(currentData, 'FlashMapToggle')
                saveMacro(currentData, 'GankPingerToggle', params=['GankPingerHotkey', 'webhook_url', 'message', 'username', 'avatar_url', 'monitorToScreenshot'], elements=['plainTextEdit_15', 'plainTextEdit', 'plainTextEdit_12', 'plainTextEdit_13', 'plainTextEdit_14', 'monitorToScreenshot'])
                saveMacro(currentData, 'ScreenshotToggle')
                saveMacro(currentData, 'AutoLogToggle', params=['autoLogHotkey', 'autoLogCoords'], elements=['autoLogHotkey', 'autoLogCoords'])
                saveMacro(currentData, 'AutoEatToggle', params=['AutoEatHotkey', 'AutoEatFoodName', 'AutoEatBoxCoords', 'AutoEatFoodCoords'], elements=['AutoEatHotkey', 'AutoEatFoodName', 'AutoEatBoxCoords', 'AutoEatFoodCoords'])


                #! chatting

                saveMacro(currentData, 'MessageToggle_1', params=['MessageHotkeyArea_1', 'MessageArea_1'], elements=['MessageHotkeyArea_1', 'MessageArea_1'])
                saveMacro(currentData, 'MessageToggle_2', params=['MessageHotkeyArea_2', 'MessageArea_2'], elements=['MessageHotkeyArea_2', 'MessageArea_2'])
                saveMacro(currentData, 'MessageToggle_3', params=['MessageHotkeyArea_3', 'MessageArea_3'], elements=['MessageHotkeyArea_3', 'MessageArea_3'])
                saveMacro(currentData, 'MessageToggle_4', params=['MessageHotkeyArea_4', 'MessageArea_4'], elements=['MessageHotkeyArea_4', 'MessageArea_4'])
                saveMacro(currentData, 'MessageToggle_5', params=['MessageHotkeyArea_5', 'MessageArea_5'], elements=['MessageHotkeyArea_5', 'MessageArea_5'])
                saveMacro(currentData, 'MessageToggle_6', params=['MessageHotkeyArea_6', 'MessageArea_6'], elements=['MessageHotkeyArea_6', 'MessageArea_6'])
                saveMacro(currentData, 'MessageToggle_7', params=['MessageHotkeyArea_7', 'MessageArea_7'], elements=['MessageHotkeyArea_7', 'MessageArea_7'])
                saveMacro(currentData, 'MessageToggle_8', params=['MessageHotkeyArea_8', 'MessageArea_8'], elements=['MessageHotkeyArea_8', 'MessageArea_8'])
                saveMacro(currentData, 'MessageToggle_9', params=['MessageHotkeyArea_9', 'MessageArea_9'], elements=['MessageHotkeyArea_9', 'MessageArea_9'])
                saveMacro(currentData, 'MessageToggle_10', params=['MessageHotkeyArea_10', 'MessageArea_10'], elements=['MessageHotkeyArea_10', 'MessageArea_10'])

                saveMacro(currentData, 'MbAllToggle', params=['MbAllHotkeyArea'], elements=['MbAllHotkeyArea'])
                saveMacro(currentData, 'GoldenTongueToggle', params=['GoldenTongueHotkeyArea', 'GoldenTongueTextArea'], elements=['GoldenTongueHotkeyArea', 'plainTextEdit_6'])

                saveMacro(currentData, 'TrashTalkToggle', params=['TrashTalkHotkey'], elements=['TrashTalkHotkey'])



                #! progresssion

                saveMacro(currentData, 'CharismaAutofillToggle')
                saveMacro(currentData, 'AutoFortitudeToggle', params=['BoulderTrainingHotkey'], elements=['BoulderTrainingHotkey'])
                saveMacro(currentData, 'AutoWillpowerToggle', params=['WillpowerTrainingHotkey'], elements=['WillpowerTrainingHotkey'])
                saveMacro(currentData, 'AutoAgilityToggle', params=['AnkleWeightsTrainingHotkey'], elements=['AnkleWeightsTrainingHotkey'])
                saveMacro(currentData, 'AutoBuyToggle', params=['AutoBuyHotkey', 'AutoBuyBarStartCoords', 'AutoBuyBarEndCoords', 'AutoBuySubmitCoords'], elements=['AutoBuyHotkey', 'AutoBuyBarStartCoords', 'AutoBuyBarEndCoords', 'AutoBuySubmitCoords'])
                saveMacro(currentData, 'AutoDropNotesToggle', params=['AutoDropNotesHotkey', 'AutoDropNotesRepetitions', 'autoDropNotesNoteCoords', 'AutoDropNotesBarStartCoords', 'AutoDropNotesBarEndCoords', 'AutoDropNotesSubmitCoords'], elements=['AutoDropNotesHotkey', 'AutoDropNotesRepetitions', 'autoDropNotesNoteCoords', 'AutoDropNotesBarStartCoords', 'AutoDropNotesBarEndCoords', 'AutoDropNotesSubmitCoords'])
                saveMacro(currentData, 'AutoSellToggle', params=['AutoSellHotkey', 'AutoSellRepetitions', 'AutoSellBarStartCoords', 'AutoSellBarEndCoords'], elements=['AutoSellHotkey', 'AutoSellRepetitions', 'AutoSellBarStartCoords', 'AutoSellBarEndCoords'])


                #! movement
                saveMacro(currentData, 'tacetToggle', elements=['autoTacetKeybind'], params=['autoTacetKeybind'])
                saveMacro(currentData, 'uncrouchToggle')

                #! silentheart

                saveMacro(currentData, 'RelentlessHuntToggle', elements=['RelentlessHuntHotkey', 'FlowStateKeybind'], params=['RelentlessHuntHotkey', 'FlowStateKeybind'])
                saveMacro(currentData, 'MayhemToggle', elements=['MayhemHotkey', 'FlowStateKeybind_2'], params=['MayhemHotkey', 'FlowStateKeybind_2'])
                saveMacro(currentData, 'RisingStarToggle', elements=['RisingStarHotkey', 'FlowStateKeybind_3'], params=['RisingStarHotkey', 'FlowStateKeybind_3'])
                saveMacro(currentData, 'AnkleCutterToggle', elements=['AnkleCutterHotkey', 'FlowStateKeybind_4'], params=['AnkleCutterHotkey', 'FlowStateKeybind_4'])


                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                filename = os.path.join(dataLocation, f'data/Preset{number}Data.json')
                try:
                        # Create the file if it doesn't exist
                        with open(filename, 'x') as f:
                                json.dump({}, f)  # create empty JSON object
                except FileExistsError:
                        print('file already exists')
                #!running

                saveMacro(currentData, 'RunKeybindToggle', params=['RunKeybindToggleKeybind'], elements=['plainTextEdit_17'])

                # Write the current data
                with open(filename, 'w') as f:
                        json.dump(currentData, f)
                

        def loadData(number):
                #!opening fiel
                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                filepath = os.path.join(dataLocation, f'data/Preset{number}Data.json')
                with open(filepath) as f:
                        savedData = json.load(f)
                def loadMacro(savedData, name, elementName=None, elementData = None): # generic loader for most toggles
                        toggle = getattr(self, name)
                        if savedData[name]:
                                toggle.setChecked(True)
                                if elementName and elementData:
                                        for i in range(len(elementName)):
                                                try:
                                                        nameOfElement = elementName[i]
                                                        dataOfElement = elementData[i] # location of element data in json
                                                except:
                                                        print('macro fields not filled out properly')
                                                element = getattr(self, nameOfElement)
                                                element.setPlainText(str(savedData[dataOfElement]))
                                return True
                        elif not savedData[name]:
                                toggle.setChecked(False)
                                return False
                        #load toggle data if applicable

                #!bells

                if savedData['BellMovestackToggle']: # can't pass element data here bc of combobox
                        self.BellMovestackToggle.setChecked(True)
                        self.MovestackChoice.setCurrentIndex(int(savedData['MovestackChoice']))
                elif not savedData['BellMovestackToggle']:
                       self.BellMovestackToggle.setChecked(False)

                if savedData['RitualCastToggle']:
                       self.RitualCastToggle.setChecked(True)
                       self.screenScale.setCurrentIndex(int(savedData['screenScale']))
                       self.screenResolution.setCurrentIndex(int(savedData['screenResolution']))
                       self.plainTextEdit_10.setPlainText(str(savedData['ritualCastPing']))
                else:
                       self.RitualCastToggle.setChecked(False)
                loadMacro(savedData, 'mantraVariantToggle', ['AutoMantraVariantsKeysArea'], ['AutoMantraVariantsKeysArea'])
                loadMacro(savedData, 'mantraTechRollToggle', ['plainTextEdit_3'], ['mantraTechRollToggleKeysArea'])
                loadMacro(savedData, 'mantraTechSlidetoggle', ['plainTextEdit_2'], ['mantraTechSlidetoggleKeysArea'])

                #!weapons

                loadMacro(savedData, 'HoldM1Toggle')
                loadMacro(savedData, 'AirDashToggle')
                loadMacro(savedData, 'uppercutDynamicToggle')
                loadMacro(savedData, 'rollUppercutToggle')
                loadMacro(savedData, 'uppercutToggle')
                loadMacro(savedData, 'autoFeintToggle')
                loadMacro(savedData, 'MotifSwapToggle', ['MotifHotkeyArea', 'MotifToolbarNumberArea', 'plainTextEdit_7'], ['MotifHotkeyArea', 'MotifToolbarNumberArea', 'MotifWeaponNumberArea'])
                loadMacro(savedData, 'rollM1Toggle', ['RollM1Hotkey'], ['RollM1Hotkey'])
                loadMacro(savedData, 'rollCritToggle')
                loadMacro(savedData, 'rollParryToggle', ['rollParryHotkey'], ['rollParryHotkey'])
                loadMacro(savedData, 'uppercutAssassinateToggle', ['uppercutAssassinateHotkey'], ['uppercutAssassinateHotkey'])
                loadMacro(savedData, 'AutoRollCancelToggle')


                #!misc

                if loadMacro(savedData, 'GankPingerToggle', ['plainTextEdit_15', 'plainTextEdit', 'plainTextEdit_12', 'plainTextEdit_13', 'plainTextEdit_14', 'monitorToScreenshot'], ['GankPingerHotkey', 'webhook_url', 'message', 'username', 'avatar_url', 'monitorToScreenshot']):
                        loadMacro(savedData, 'ScreenshotToggle')

                loadMacro(savedData, 'FlashMapToggle')
                loadMacro(savedData, 'AutoLogToggle', ['autoLogHotkey', 'autoLogCoords'], ['autoLogHotkey', 'autoLogCoords'])
                loadMacro(savedData, 'AutoEatToggle', ['AutoEatHotkey', 'AutoEatFoodName', 'AutoEatBoxCoords', 'AutoEatFoodCoords'], ['AutoEatHotkey', 'AutoEatFoodName', 'AutoEatBoxCoords', 'AutoEatFoodCoords'])

                
                       
                #!progression

                loadMacro(savedData, 'CharismaAutofillToggle')
                loadMacro(savedData, 'AutoFortitudeToggle', ['BoulderTrainingHotkey'],['BoulderTrainingHotkey'])
                loadMacro(savedData, 'AutoWillpowerToggle', ['WillpowerTrainingHotkey'], ['WillpowerTrainingHotkey'])
                loadMacro(savedData, 'AutoAgilityToggle', ['AnkleWeightsTrainingHotkey'], ['AnkleWeightsTrainingHotkey'])
                loadMacro(savedData, 'AutoBuyToggle', ['AutoBuyHotkey', 'AutoBuyBarStartCoords', 'AutoBuyBarEndCoords', 'AutoBuySubmitCoords'], ['AutoBuyHotkey', 'AutoBuyBarStartCoords', 'AutoBuyBarEndCoords', 'AutoBuySubmitCoords'])
                loadMacro(savedData, 'AutoDropNotesToggle', ['AutoDropNotesHotkey', 'AutoDropNotesRepetitions', 'autoDropNotesNoteCoords', 'AutoDropNotesBarStartCoords', 'AutoDropNotesBarEndCoords', 'AutoDropNotesSubmitCoords'], ['AutoDropNotesHotkey', 'AutoDropNotesRepetitions', 'autoDropNotesNoteCoords', 'AutoDropNotesBarStartCoords', 'AutoDropNotesBarEndCoords', 'AutoDropNotesSubmitCoords'])
                loadMacro(savedData, 'AutoSellToggle', ['AutoSellHotkey', 'AutoSellRepetitions', 'AutoSellBarStartCoords', 'AutoSellBarEndCoords'], ['AutoSellHotkey', 'AutoSellRepetitions', 'AutoSellBarStartCoords', 'AutoSellBarEndCoords'])

                #! movement
                loadMacro(savedData, 'tacetToggle', ['autoTacetKeybind'], ['autoTacetKeybind'])
                loadMacro(savedData, 'uncrouchToggle')

                #! chatting
                loadMacro(savedData, 'MbAllToggle')
                loadMacro(savedData, 'GoldenTongueToggle', ['GoldenTongueHotkeyArea', 'plainTextEdit_6'], ['GoldenTongueHotkeyArea', 'GoldenTongueTextArea'])

                loadMacro(savedData, 'TrashTalkToggle', ['TrashTalkHotkey'], ['TrashTalkHotkey'])
                loadMacro(savedData, 'MessageToggle_1', ['MessageHotkeyArea_1', 'MessageArea_1'], ['MessageHotkeyArea_1', 'MessageArea_1'])
                loadMacro(savedData, 'MessageToggle_2', ['MessageHotkeyArea_2', 'MessageArea_2'], ['MessageHotkeyArea_2', 'MessageArea_2'])
                loadMacro(savedData, 'MessageToggle_3', ['MessageHotkeyArea_3', 'MessageArea_3'], ['MessageHotkeyArea_3', 'MessageArea_3'])
                loadMacro(savedData, 'MessageToggle_4', ['MessageHotkeyArea_4', 'MessageArea_4'], ['MessageHotkeyArea_4', 'MessageArea_4'])
                loadMacro(savedData, 'MessageToggle_5', ['MessageHotkeyArea_5', 'MessageArea_5'], ['MessageHotkeyArea_5', 'MessageArea_5'])
                loadMacro(savedData, 'MessageToggle_6', ['MessageHotkeyArea_6', 'MessageArea_6'], ['MessageHotkeyArea_6', 'MessageArea_6'])
                loadMacro(savedData, 'MessageToggle_7', ['MessageHotkeyArea_7', 'MessageArea_7'], ['MessageHotkeyArea_7', 'MessageArea_7'])
                loadMacro(savedData, 'MessageToggle_8', ['MessageHotkeyArea_8', 'MessageArea_8'], ['MessageHotkeyArea_8', 'MessageArea_8'])
                loadMacro(savedData, 'MessageToggle_9', ['MessageHotkeyArea_9', 'MessageArea_9'], ['MessageHotkeyArea_9', 'MessageArea_9'])
                loadMacro(savedData, 'MessageToggle_10', ['MessageHotkeyArea_10', 'MessageArea_10'], ['MessageHotkeyArea_10', 'MessageArea_10'])

                #! silentheart
                loadMacro(savedData, 'RelentlessHuntToggle', ['RelentlessHuntHotkey', 'FlowStateKeybind'], ['RelentlessHuntHotkey', 'FlowStateKeybind'])
                loadMacro(savedData, 'MayhemToggle', ['MayhemHotkey', 'FlowStateKeybind_2'], ['MayhemHotkey', 'FlowStateKeybind_2'])
                loadMacro(savedData, 'RisingStarToggle', ['RisingStarHotkey', 'FlowStateKeybind_3'], ['RisingStarHotkey', 'FlowStateKeybind_3'])
                loadMacro(savedData, 'AnkleCutterToggle', ['AnkleCutterHotkey', 'FlowStateKeybind_4'], ['AnkleCutterHotkey', 'FlowStateKeybind_4'])
                
                #! running
                loadMacro(savedData, 'RunKeybindToggle', ['plainTextEdit_17'], ['RunKeybindToggleKeybind'])

                

                
        self.Preset1Save.clicked.connect(lambda:saveCurrentData(1))
        self.Preset1Load.clicked.connect(lambda:loadData(1))

        self.Preset2Save.clicked.connect(lambda:saveCurrentData(2))
        self.Preset2Load.clicked.connect(lambda:loadData(2))

        self.Preset3Save.clicked.connect(lambda:saveCurrentData(3))
        self.Preset3Load.clicked.connect(lambda:loadData(3))

        self.Preset4Save.clicked.connect(lambda:saveCurrentData(4))
        self.Preset4Load.clicked.connect(lambda:loadData(4))

        self.Preset5Save.clicked.connect(lambda:saveCurrentData(5))
        self.Preset5Load.clicked.connect(lambda:loadData(5))

        self.Preset6Save.clicked.connect(lambda:saveCurrentData(6))
        self.Preset6Load.clicked.connect(lambda:loadData(6))

        self.Preset7Save.clicked.connect(lambda:saveCurrentData(7))
        self.Preset7Load.clicked.connect(lambda:loadData(7))

        self.Preset8Save.clicked.connect(lambda:saveCurrentData(8))
        self.Preset8Load.clicked.connect(lambda:loadData(8))

        self.Preset9Save.clicked.connect(lambda:saveCurrentData(9))
        self.Preset9Load.clicked.connect(lambda:loadData(9))

        self.Preset10Save.clicked.connect(lambda:saveCurrentData(10))
        self.Preset10Load.clicked.connect(lambda:loadData(10))        
        def CheckNames():
                dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                filename = os.path.join(dataLocation, 'data/PresetNames.json')
                with open(filename) as f:
                        presetNames = json.load(f)
                self.Preset1Name.setText(presetNames['Preset1Name'])
                self.Preset2Name.setText(presetNames['Preset2Name'])
                self.Preset3Name.setText(presetNames['Preset3Name'])
                self.Preset4Name.setText(presetNames['Preset4Name'])
                self.Preset5Name.setText(presetNames['Preset5Name'])
                self.Preset6Name.setText(presetNames['Preset6Name'])
                self.Preset7Name.setText(presetNames['Preset7Name'])
                self.Preset8Name.setText(presetNames['Preset8Name'])
                self.Preset9Name.setText(presetNames['Preset9Name'])
                self.Preset10Name.setText(presetNames['Preset10Name'])
        CheckNames()

        def NameEditor(number):
                preset_widget = getattr(self, f"Preset{number}Name")
                preset_widget.setEnabled(True)
                preset_widget.setReadOnly(False)
                # Select all text and set focus
                preset_widget.setFocus()
                preset_widget.selectAll()
        
                def on_focus_lost(event):
                        preset_widget.setEnabled(False)
                        preset_widget.setReadOnly(True)
                        dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation) 
                        filename = os.path.join(dataLocation, 'data/PresetNames.json')
                        with open(filename) as f:
                                prevData = json.load(f)
                                varname = f'Preset{number}Name'
                                prevData[varname] = preset_widget.text()
                                f.close()
                        with open(filename, 'w') as f:
                                json.dump(prevData, f)
        
                preset_widget.focusOutEvent = on_focus_lost

        self.Preset1EditName.clicked.connect(lambda:NameEditor(1))
        self.Preset2EditName.clicked.connect(lambda:NameEditor(2))
        self.Preset3EditName.clicked.connect(lambda:NameEditor(3))
        self.Preset4EditName.clicked.connect(lambda:NameEditor(4))
        self.Preset5EditName.clicked.connect(lambda:NameEditor(5))
        self.Preset6EditName.clicked.connect(lambda:NameEditor(6))
        self.Preset7EditName.clicked.connect(lambda:NameEditor(7))
        self.Preset8EditName.clicked.connect(lambda:NameEditor(8))
        self.Preset9EditName.clicked.connect(lambda:NameEditor(9))
        self.Preset10EditName.clicked.connect(lambda:NameEditor(10))
        # Starting the thread (inside some class or context)