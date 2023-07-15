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

        # Calls the set_brush_size method and sets it to the value of the brushSize slider, when the value of the slider is changed
        self.h_slider_brushSize.valueChanged.connect(lambda: self.canvas.set_brush_size(self.h_slider_brushSize.value()))

# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AnimationCreator()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())