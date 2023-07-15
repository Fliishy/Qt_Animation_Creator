import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from UI.animation_creator_ui import Ui_animation_creator
from Widgets.canvas import Canvas


class AnimationCreator (QtWidgets.QMainWindow, Ui_animation_creator, Canvas):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.canvas = Canvas()
        self.canvas.setScaledContents(True)
        self.right_layout.addWidget(self.canvas)

        self.pushButton.clicked.connect(lambda: self.canvas.set_pen_color('blue'))
        self.pushButton_2.clicked.connect(lambda: self.canvas.set_bg_color('red'))

# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = AnimationCreator()
    window.show()

    # terminates the program if it is exited
    sys.exit(app.exec())