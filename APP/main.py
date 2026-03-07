import os
os.environ['QT_ENABLE_FEATURE_true_property'] = '0'
os.environ['PYSIDE_FEATURE_true_property'] = '0'
import sys
import requests  # noqa: F401
from MainUI import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QStyleFactory
from PySide6.QtGui import QIcon, QPalette, QColor
import os
import ctypes
from setup import Setup
from PySide6.QtCore import QRect, Qt, QEvent, QStandardPaths
from ctypes import windll, c_int, byref, sizeof
from ctypes.wintypes import BOOL
import json
Setup()
def enable_dark_title_bar(window):
    if os.name == 'nt':  # Windows only
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = windll.dwmapi.DwmSetWindowAttribute
        hwnd = window.winId()
        rendering_policy = BOOL(True)
        set_window_attribute(
            c_int(hwnd), 
            DWMWA_USE_IMMERSIVE_DARK_MODE,
            byref(rendering_policy),
            sizeof(rendering_policy)
        )

def set_dark_theme(app):
    app.setStyle(QStyleFactory.create('Fusion'))
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    palette.setColor(QPalette.PlaceholderText, QColor(127,127,127))

    app.setPalette(palette)

    app.setStyleSheet("""
    /* Only target specific frame types */
    QFrame[frameShape="4"],  /* QFrame::HLine */
    QFrame[frameShape="5"],  /* QFrame::VLine */
    QFrame[frameShape="6"],  /* QFrame::StyledPanel */
    QFrame[frameShape="2"]   /* QFrame::Panel */
    {
        border: 0.5px solid rgba(20,20,20,0.25);
    }
                      
    QMainWindow, QMenuBar, QLabel {
        border: none;
    }
    QFrame#frame_2 {
        border: none;
    }

    /* Remove borders from text widgets */
    QLineEdit, QTextEdit, QPlainTextEdit {
        border: none;
    }
    QPlainTextEdit {
    background-color: #2A2A2A !important;
    border-radius:5px !important;
    border:none !important;
    }
    """)

def set_navy_blue_theme(app):
    app.setStyle(QStyleFactory.create('Fusion'))
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(10, 10, 30))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(15, 15, 40))
    palette.setColor(QPalette.AlternateBase, QColor(20, 20, 45))
    palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 50))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(25, 25, 50))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Link, QColor(70, 120, 220))
    palette.setColor(QPalette.Highlight, QColor(50, 100, 200))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    palette.setColor(QPalette.PlaceholderText, QColor(150, 150, 200))
    app.setPalette(palette)

    app.setStyleSheet("""
    /* Only target specific frame types */
    QFrame[frameShape="4"],  /* QFrame::HLine */
    QFrame[frameShape="5"],  /* QFrame::VLine */
    QFrame[frameShape="6"],  /* QFrame::StyledPanel */
    QFrame[frameShape="2"]   /* QFrame::Panel */
    {
        border: 0.5px solid rgba(211,211,211,0.15);
    }
                      
    QMainWindow, QMenuBar, QLabel {
        border: none;
    }
    QFrame#frame_2 {
        border: none;
    }

    /* Remove borders from text widgets */
    QLineEdit, QTextEdit, QPlainTextEdit {
        border: none;
    }
    QPlainTextEdit {
    background-color: #1b1530 !important;
    border-radius:5px !important;
    border:none !important;
    }
    """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        enable_dark_title_bar(self)
        self.setWindowTitle('DeepWarden')
        
        # Set the window icon
        self.dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        self.settings_path = os.path.join(self.dataLocation, 'data/Settings.json')
        dirpath = os.path.dirname(__file__)
        icon_path = os.path.join(dirpath, 'assets/logo.ico')
        self.setWindowIcon(QIcon(icon_path))

        # Windows taskbar icon
        if os.name == 'nt':
            myappid = 'deepwarden.deepwarden.2.0'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        

        
        # Theme handling
        def themeChanged():
            with open(self.settings_path) as f:
                settings = json.load(f) 
                themeNum = self.ui.themeComboBox.currentIndex()
                if themeNum == 0:
                    settings['theme'] = 'dark'
                elif themeNum == 1:
                    settings['theme'] = 'navy'
            
            app = QApplication.instance()
            if self.ui.themeComboBox.currentIndex() == 0:
                set_dark_theme(app)
                settings['theme'] = 'dark'
                self.setPalette(app.palette())
            elif self.ui.themeComboBox.currentIndex() == 1:
                set_navy_blue_theme(app)
                self.setPalette(app.palette())
                settings['theme'] = 'navy'
            else:
                set_dark_theme(app)
                self.setPalette(app.palette())
            
            with open(self.settings_path, 'w') as e:
                json.dump(settings, e)
            
            # Force update
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()

        self.ui.themeComboBox.currentIndexChanged.connect(themeChanged)
        
        with open(self.settings_path) as f:
            settings = json.load(f)
            if settings['theme'] == 'dark':
                self.ui.themeComboBox.setCurrentIndex(0)
            elif settings['theme'] == 'navy':
                self.ui.themeComboBox.setCurrentIndex(1)

        # Modify all QPlainTextEdit widgets
        for widget in self.findChildren(QPlainTextEdit):
            widget.installEventFilter(self)
            widget.setLineWrapMode(QPlainTextEdit.NoWrap)
            widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            widget.setContextMenuPolicy(Qt.NoContextMenu)

        # Install event filter for focus clearing
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        # Clear focus when enter is pressed
        if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return):
            focused_widget = QApplication.focusWidget()
            focused_widget.clearFocus()

        
        # Handle mouse press events for clearing focus
        if event.type() == event.Type.MouseButtonPress:
            focused_widget = QApplication.focusWidget()
            if focused_widget and isinstance(focused_widget, QPlainTextEdit):
                click_position = event.globalPosition().toPoint()
                widget_rect = QRect(focused_widget.mapToGlobal(focused_widget.rect().topLeft()),
                                focused_widget.mapToGlobal(focused_widget.rect().bottomRight()))
                
                if not widget_rect.contains(click_position):
                    focused_widget.clearFocus()
        
        # Convert uppercase to lowercase for QPlainTextEdit
        if isinstance(obj, QPlainTextEdit) and event.type() == event.Type.KeyPress:
            if event.text().isalpha():
                obj.insertPlainText(event.text().lower())
                return True
                    
        return super().eventFilter(obj, event)

    def closeEvent(self, event):
        self.ui.RunToggle.setChecked(False)
        return super().closeEvent(event)

def main():
    dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    dirpath = os.path.dirname(__file__)

    icopath = os.path.join(dirpath, 'assets', 'logo.ico')

    app = QApplication(sys.argv)
    app.setApplicationName('DeepWarden')
    app.setWindowIcon(QIcon(icopath))
    settings_path = os.path.join(dataLocation, 'data/Settings.json')
    
    try:
        with open(settings_path) as f:
            settings = json.load(f)
    
        if 'theme' in settings:
            if settings['theme'] == 'dark':
                set_dark_theme(app)  
            elif settings['theme'] == 'navy':
                set_navy_blue_theme(app)
        else:
            set_dark_theme(app)
    except Exception:
        set_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
