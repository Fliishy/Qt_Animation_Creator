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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_animation_creator(object):
    def setupUi(self, animation_creator):
        if not animation_creator.objectName():
            animation_creator.setObjectName(u"animation_creator")
        animation_creator.resize(844, 676)
        self.centralwidget = QWidget(animation_creator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settings_area = QVBoxLayout()
        self.settings_area.setObjectName(u"settings_area")

        self.horizontalLayout.addLayout(self.settings_area)

        self.drawing_area = QVBoxLayout()
        self.drawing_area.setObjectName(u"drawing_area")
        self.drawing_area.setSizeConstraint(QLayout.SetMinimumSize)

        self.horizontalLayout.addLayout(self.drawing_area)

        animation_creator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(animation_creator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 22))
        font = QFont()
        font.setPointSize(11)
        self.menubar.setFont(font)
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
        self.menuFile.setTitle(QCoreApplication.translate("animation_creator", u"File", None))
    # retranslateUi

