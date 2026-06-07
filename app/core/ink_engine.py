from PyQt6.QtCore import QPoint, Qt, pyqtSignal
from PyQt6.QtGui import QColor, QMouseEvent, QPainter, QPen, QPixmap
from PyQt6.QtWidgets import QWidget


class InkCanvas(QWidget):
    changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(640, 420)
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.canvas = QPixmap(1600, 1000)
        self.canvas.fill(QColor("#ffffff"))
        self.color = QColor("#1f6feb")
        self.pen_width = 3
        self.last_point = QPoint()
        self.drawing = False

    def paintEvent(self, _):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.canvas)

    def resizeEvent(self, event):
        if self.width() > self.canvas.width() or self.height() > self.canvas.height():
            expanded = QPixmap(max(self.width(), self.canvas.width()), max(self.height(), self.canvas.height()))
            expanded.fill(QColor("#ffffff"))
            painter = QPainter(expanded)
            painter.drawPixmap(0, 0, self.canvas)
            painter.end()
            self.canvas = expanded
        super().resizeEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_point = event.position().toPoint()
            self.drawing = True

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drawing and event.buttons() & Qt.MouseButton.LeftButton:
            point = event.position().toPoint()
            painter = QPainter(self.canvas)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setPen(QPen(self.color, self.pen_width, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
            painter.drawLine(self.last_point, point)
            painter.end()
            self.last_point = point
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self.drawing:
            self.drawing = False
            self.changed.emit()

    def clear(self):
        self.canvas.fill(QColor("#ffffff"))
        self.update()
        self.changed.emit()

    def save(self, path):
        return self.canvas.save(str(path), "PNG")
