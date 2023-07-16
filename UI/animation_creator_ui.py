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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_animation_creator(object):
    def setupUi(self, animation_creator):
        if not animation_creator.objectName():
            animation_creator.setObjectName(u"animation_creator")
        animation_creator.resize(844, 676)
        self.centralwidget = QWidget(animation_creator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.drawing_area = QVBoxLayout()
        self.drawing_area.setObjectName(u"drawing_area")
        self.drawing_area.setSizeConstraint(QLayout.SetMinimumSize)

        self.gridLayout.addLayout(self.drawing_area, 0, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.color_picker = QLabel(self.frame)
        self.color_picker.setObjectName(u"color_picker")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.color_picker.sizePolicy().hasHeightForWidth())
        self.color_picker.setSizePolicy(sizePolicy1)
        self.color_picker.setMinimumSize(QSize(130, 130))
        self.color_picker.setMouseTracking(True)
        self.color_picker.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.color_picker.setStyleSheet(u"QLabel{\n"
"	background-color: #000000;\n"
"	border-radius: 65%;\n"
"}")
        self.color_picker.setScaledContents(False)
        self.color_picker.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.color_picker, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label)

        self.h_slider_brushSize = QSlider(self.frame)
        self.h_slider_brushSize.setObjectName(u"h_slider_brushSize")
        sizePolicy2.setHeightForWidth(self.h_slider_brushSize.sizePolicy().hasHeightForWidth())
        self.h_slider_brushSize.setSizePolicy(sizePolicy2)
        self.h_slider_brushSize.setMinimumSize(QSize(130, 0))
        self.h_slider_brushSize.setMaximum(30)
        self.h_slider_brushSize.setValue(4)
        self.h_slider_brushSize.setOrientation(Qt.Horizontal)
        self.h_slider_brushSize.setTickPosition(QSlider.NoTicks)
        self.h_slider_brushSize.setTickInterval(12)

        self.verticalLayout_2.addWidget(self.h_slider_brushSize)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        animation_creator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(animation_creator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 20))
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
        self.color_picker.setText("")
        self.label.setText(QCoreApplication.translate("animation_creator", u"Brush Size:", None))
        self.menuFile.setTitle(QCoreApplication.translate("animation_creator", u"File", None))
    # retranslateUi

