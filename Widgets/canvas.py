'''
    This is the logic for drawing with the mouse taken from https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
    I've adapted it to fit my own program and added comments throughout
'''
from PySide6 import QtGui, QtWidgets

# Uses a QLabel as a simple way to display an image 
class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        # Scales up widget to fill it's holder
        # !!! Need to fix this as it's causing mouse + blurring issues !!!
        self.setScaledContents(True)

        '''
            Initialises a pixmap (drawing_window) that's size is the size of the QLabel (Canvas)
            Fills the background with the chosen color (#ffffff = white)
            Sets the pixmap of the QLabel (Canvas) to be the pixmap (drawing_window)
        '''
        self.drawing_window = QtGui.QPixmap(self.size())
        self.drawing_window.fill('#ffffff')
        self.setPixmap(self.drawing_window)

        '''
            Creates a QPen object that is used inside of the painter
            Calls the set_brush_size method to determine the pen size
            Creates a pen_color variable and sets it to black
            Sets the pen color to be the pen_color variable
        '''
        self.pen = QtGui.QPen()
        self.set_brush_size(4)
        self.set_pen_color()
        
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
    def set_pen_color(self, color='#000000'):
        self.pen.setColor(color)


    '''
        Defines the pen size for the painter.pen() by passing it the size argument
        Sets the default size to 4
    '''
    def set_brush_size(self, size):
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
            Sets the renderers (painter) pen to be the new pen we've called self.pen
        '''
        canvas = self.pixmap()
        self.painter = QtGui.QPainter(canvas)
        self.painter.setPen(self.pen)

        '''
            We use the QPainter drawLine to draw a line between the last recorded positions x/y and the current position x/y
            After drawing  the line we end the painting on the pixmap
            We update the QLabel widget (Canvas) with the new pixmap (canvas)
        '''
        self.painter.drawLine(self.last_x, self.last_y, current.x(), current.y())
        self.painter.end()
        self.setPixmap(canvas)

        # Updates the last x/y positions for the next mouse event
        self.last_x = current.x()
        self.last_y = current.y()

    # When the mouse is released it will set the last x/y values back to None
    def mouseReleaseEvent(self, current):
        self.last_x = None
        self.last_y = None