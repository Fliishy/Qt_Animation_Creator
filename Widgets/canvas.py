'''
    This is the logic for drawing with the mouse taken from https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
    I've adapted it to fit my own program
'''
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

# Uses a QLabel as a simple way to display an image 
class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        '''
            Initialises a pixmap (drawing_window) that's size is the size of the QLabel (Canvas)
            Fills the background with the chosen color (#ffffff = white)
            Sets the pixmap of the QLabel (Canvas) to be the pixmap (drawing_window)
        '''
        self.drawing_window = QtGui.QPixmap(self.size())
        self.drawing_window.fill('#ffffff')
        self.setPixmap(self.drawing_window)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#000000')

    def set_bg_color(self, color):
        self.bg_color = QtGui.QColor(color)
        self.drawing_window.fill(self.bg_color)
        self.setPixmap(self.drawing_window)

    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None