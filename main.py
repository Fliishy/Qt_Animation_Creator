import sys
from PySide6 import QtWidgets

from UI.animation_creator_ui import Ui_animation_creator
from Widgets.canvas import Canvas
from Widgets.settings import Settings


class AnimationCreator(QtWidgets.QMainWindow, Ui_animation_creator):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
            Sets up a new canvas widget by calling Canvas()
            Adds the canvas to the drawing_area which is a QVBoxLayout
        '''
        self.canvas = Canvas()
        self.settings = Settings(self.canvas)
        self.drawing_area.addWidget(self.canvas)
        self.settings_area.addWidget(self.settings)
   

# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AnimationCreator()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())