from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt, QPropertyAnimation, QRectF, QEasingCurve, Property, QParallelAnimationGroup
from PySide6.QtGui import QPainter, QColor, QPen
class CustomToggle(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setChecked(False)
        self.setFixedSize(60, 30)
        
        self._off_color = QColor(200, 200, 200)
        self._on_color = QColor(0, 150, 136)
        self._circle_color = QColor(255, 255, 255)
        
        self._circle_position = 3
        self._bg_color = self._off_color
        self._is_checked = False
        
        self.animation_group = QParallelAnimationGroup(self)
        
        self.position_animation = QPropertyAnimation(self, b"circle_position", self)
        self.position_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.position_animation.setDuration(300)
        
        self.color_animation = QPropertyAnimation(self, b"bg_color", self)
        self.color_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.color_animation.setDuration(300)
        
        self.animation_group.addAnimation(self.position_animation)
        self.animation_group.addAnimation(self.color_animation)
        
        self.stateChanged.connect(self.start_transition)

    def get_circle_position(self):
        return self._circle_position

    def set_circle_position(self, pos):
        self._circle_position = pos
        self.update()

    circle_position = Property(float, get_circle_position, set_circle_position)

    def get_bg_color(self):
        return self._bg_color

    def set_bg_color(self, color):
        self._bg_color = color
        self.update()

    bg_color = Property(QColor, get_bg_color, set_bg_color)

    def start_transition(self, value):
        self._is_checked = value
        self.position_animation.setStartValue(3 if value else 33)
        self.position_animation.setEndValue(33 if value else 3)
        self.color_animation.setStartValue(self._off_color if value else self._on_color)
        self.color_animation.setEndValue(self._on_color if value else self._off_color)
        self.animation_group.start()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw background
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._bg_color)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 15, 15)

        # Draw circle
        painter.setPen(QPen(Qt.GlobalColor.white))
        painter.setBrush(self._circle_color)
        painter.drawEllipse(QRectF(self._circle_position, 3, 24, 24))

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.setChecked(not self._is_checked)
