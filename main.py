import sys
from PySide6 import QtWidgets, QtGui

from UI.animation_creator_ui import Ui_animation_creator
from Widgets.canvas import Canvas
from Widgets.settings import Settings


class AnimationCreator(QtWidgets.QMainWindow, Ui_animation_creator):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
            Sets up a new canvas object by calling Canvas()
            Sets the size policy to be expanding so that the widget fills the available space
            Sets up a new settings object which controls the newly created canvas object
            Adds the canvas to the drawing_area which is a QVBoxLayout
            Adds the settings to the settings_area which is a QVBoxLayout
        '''
        self.canvas = Canvas()
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.settings = Settings(self.canvas)
        self.drawing_area.addWidget(self.canvas)
        self.settings_area.addWidget(self.settings)
   

# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AnimationCreator()
    window.showMaximized()
    # terminates the program if it is exited
    sys.exit(app.exec())