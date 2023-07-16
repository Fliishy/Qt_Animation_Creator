import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from UI.animation_creator_ui import Ui_animation_creator
from Widgets.canvas import Canvas


class AnimationCreator(QtWidgets.QMainWindow, Ui_animation_creator):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
            Sets up a new canvas widget by calling Canvas()
            Sets the canvas up so that it scales to the QLabel size
            Adds the canvas widget to the drawing area QVBoxLayout
        '''
        self.canvas = Canvas()
        self.canvas.setScaledContents(True)
        self.drawing_area.addWidget(self.canvas)

        '''
            Calls the set_brush_size method and sets it to the value of the brushSize slider, when the value of the slider is changed
            lambda is used to create an anonymous function, : separates it from the expression
            It allows us to pass the value of the slider into the set_brush_size(size) as it is expecting an arguement
            If this isn't there then the valueChanged will emit a signal and pass it directly to set_brush_size not it's size arguement
        '''
        self.h_slider_brushSize.valueChanged.connect(lambda: self.canvas.set_brush_size(self.h_slider_brushSize.value()))

        # Install an event filter on the color_label to handle mouse enter events
        self.color_picker.installEventFilter(self)

    '''
        If the mouse enters the color_picker it will show the color picker gui
        It looks to see if the mouse is over the color picker and if the event is a mouseover
    '''
    def eventFilter(self, obj, event):
        if obj == self.color_picker and event.type() == QtCore.QEvent.Enter:
            self.show_color_picker()

        return super().eventFilter(obj, event)
    
    '''
        Initialises a new color_dialog widget
        When the current color of the widget is changed we call the color_changed method
        QColorDialog.Accepted is a constant that has a value of 1
        If color_dialog is exited it's value set to 1
        This basically checks if the user has selected a color and clicked ok
        We don't need anything to happen so we pass
    '''
    def show_color_picker(self):
        color_dialog = QtWidgets.QColorDialog(self)

        color_dialog.currentColorChanged.connect(self.color_changed)

        if color_dialog.exec_() == QtWidgets.QColorDialog.Accepted:
            pass

    '''
        If the  selected color is a valid color
        The background color of the label is set to the selected color
        Border-radius is applied to keep the round shape
        The pen color is set to the color we just selected by calling the set_pen_color method
    '''
    def color_changed(self, color):    
        if color.isValid():
            color_picker_style = f'background-color:{color.name()}; border-radius:65%;'
            self.color_picker.setStyleSheet(color_picker_style)
            self.canvas.set_pen_color(color.name())
        

# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AnimationCreator()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())