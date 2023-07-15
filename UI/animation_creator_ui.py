# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation_creator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_animation_creator(object):
    def setupUi(self, animation_creator):
        if not animation_creator.objectName():
            animation_creator.setObjectName(u"animation_creator")
        animation_creator.resize(742, 634)
        self.centralwidget = QWidget(animation_creator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")

        self.gridLayout.addLayout(self.right_layout, 0, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        animation_creator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(animation_creator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 742, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        animation_creator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(animation_creator)
        self.statusbar.setObjectName(u"statusbar")
        animation_creator.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(animation_creator)

        QMetaObject.connectSlotsByName(animation_creator)
    # setupUi

    def retranslateUi(self, animation_creator):
        animation_creator.setWindowTitle(QCoreApplication.translate("animation_creator", u"Animation Creator", None))
        self.pushButton.setText(QCoreApplication.translate("animation_creator", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("animation_creator", u"PushButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("animation_creator", u"File", None))
    # retranslateUi

