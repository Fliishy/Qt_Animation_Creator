'''
    This is the logic for drawing with the mouse taken from https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
    I've adapted it to fit my own program and added comments throughout
'''
from PySide6 import QtGui, QtWidgets

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

        '''
            Initialises the pen_color to be #000000 (black)
            We set the QPen object with this in a later method
        '''
        self.pen_color = QtGui.QColor('#000000')

        '''
            Initialises two variables to record the last recorded x, y positons of the mouse
            We set them to None to help identify the first mouse event
        '''
        self.last_x, self.last_y = None, None

    '''
        The bg_color variable is set to color argument passed by the user
        The drawing_window (pixmap) is filled to display the color given
        The QLabel (Canvas) is then redrawn with the updated color
        This erases anything that is on the screen at that time
    '''
    def set_bg_color(self, color):
        self.bg_color = QtGui.QColor(color)
        self.drawing_window.fill(self.bg_color)
        self.setPixmap(self.drawing_window)

    '''
        Defines the pen_color variable by passing it the color argument
    '''
    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)

    '''
        Defines the pen size for the painter.pen() by passing it the size argument
    '''
    def set_pen_width(self, size):
        self.pen.setWidth(size)

    '''
        Handles when the mouse moves over the canvas
        This is set to None by default in the __init__
        If None is set then we set the event x,y coordinates to also be None
        Returns nothing as we want nothing to happen until the mouse event happens
    '''
    def mouseMoveEvent(self, current):
        if self.last_x is None:
            self.last_x = current.x()
            self.last_y = current.y()
            return # Ignore the first time

        '''
            self.pixmap() returns the QLabel(Canvas) and sets it to a variable canvas
            Defins the renderer (painter) for displaying graphics and sets canvas as the pixmap for drawing
            Creates a QPen object that is used inside of the painter
            Calls the set_pen_width method to determine the pen size
            Sets the colour to be the initial colour during setup by calling the pen_color variable: #000000 (Black) in this case
            Sets the renderers (painter) pen to be the new pen we've called self.pen
        '''
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        self.pen = painter.pen()
        self.set_pen_width(4)
        self.pen.setColor(self.pen_color)
        painter.setPen(self.pen)

        '''
            We use the QPainter drawLine to draw a line between the last recorded positions x/y and the current position x/y
            After drawing  the line we end the painting on the pixmap
            We update the QLabel widget (Canvas) with the new pixmap (canvas)
        '''
        painter.drawLine(self.last_x, self.last_y, current.x(), current.y())
        painter.end()
        self.setPixmap(canvas)

        # Updates the last x/y positions for the next mouse event
        self.last_x = current.x()
        self.last_y = current.y()

    # When the mouse is released it will set the last x/y values back to None
    def mouseReleaseEvent(self):
        self.last_x = None
        self.last_y = None