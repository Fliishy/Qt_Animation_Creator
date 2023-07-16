# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_settings_ui(object):
    def setupUi(self, settings_ui):
        if not settings_ui.objectName():
            settings_ui.setObjectName(u"settings_ui")
        settings_ui.resize(415, 673)
        self.gridLayout = QGridLayout(settings_ui)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settings_frame = QFrame(settings_ui)
        self.settings_frame.setObjectName(u"settings_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_frame.sizePolicy().hasHeightForWidth())
        self.settings_frame.setSizePolicy(sizePolicy)
        self.settings_frame.setMinimumSize(QSize(250, 0))
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.settings_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.color_picker = QLabel(self.settings_frame)
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
"	border: 1px solid black;\n"
"}")
        self.color_picker.setScaledContents(False)
        self.color_picker.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.color_picker, 0, Qt.AlignHCenter)

        self.color_name_text = QLabel(self.settings_frame)
        self.color_name_text.setObjectName(u"color_name_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.color_name_text.sizePolicy().hasHeightForWidth())
        self.color_name_text.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        self.color_name_text.setFont(font)
        self.color_name_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.color_name_text)

        self.pb_brush = QPushButton(self.settings_frame)
        self.pb_brush.setObjectName(u"pb_brush")
        sizePolicy1.setHeightForWidth(self.pb_brush.sizePolicy().hasHeightForWidth())
        self.pb_brush.setSizePolicy(sizePolicy1)
        self.pb_brush.setMinimumSize(QSize(75, 0))
        self.pb_brush.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffffff;\n"
"}")

        self.verticalLayout_2.addWidget(self.pb_brush, 0, Qt.AlignHCenter)

        self.h_layout_color_buttons = QHBoxLayout()
        self.h_layout_color_buttons.setObjectName(u"h_layout_color_buttons")
        self.h_layout_color_buttons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.h_layout_color_buttons.setContentsMargins(-1, 10, -1, -1)
        self.pb_black_button = QPushButton(self.settings_frame)
        self.pb_black_button.setObjectName(u"pb_black_button")
        self.pb_black_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #000000;\n"
"}")

        self.h_layout_color_buttons.addWidget(self.pb_black_button)

        self.pb_color_button = QPushButton(self.settings_frame)
        self.pb_color_button.setObjectName(u"pb_color_button")
        self.pb_color_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #ff0000;\n"
"}")

        self.h_layout_color_buttons.addWidget(self.pb_color_button)

        self.pb_white_button = QPushButton(self.settings_frame)
        self.pb_white_button.setObjectName(u"pb_white_button")
        self.pb_white_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffffff;\n"
"}")

        self.h_layout_color_buttons.addWidget(self.pb_white_button)


        self.verticalLayout_2.addLayout(self.h_layout_color_buttons)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.background_picker = QLabel(self.settings_frame)
        self.background_picker.setObjectName(u"background_picker")
        sizePolicy1.setHeightForWidth(self.background_picker.sizePolicy().hasHeightForWidth())
        self.background_picker.setSizePolicy(sizePolicy1)
        self.background_picker.setMinimumSize(QSize(100, 100))
        self.background_picker.setMouseTracking(True)
        self.background_picker.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.background_picker.setStyleSheet(u"QLabel{\n"
"	background-color: #ffffff;	\n"
"	border: 1px solid black;\n"
"}")
        self.background_picker.setScaledContents(False)
        self.background_picker.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.background_picker, 0, Qt.AlignHCenter)

        self.bg_color_text = QLabel(self.settings_frame)
        self.bg_color_text.setObjectName(u"bg_color_text")
        sizePolicy2.setHeightForWidth(self.bg_color_text.sizePolicy().hasHeightForWidth())
        self.bg_color_text.setSizePolicy(sizePolicy2)
        self.bg_color_text.setFont(font)
        self.bg_color_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.bg_color_text)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.pb_eraser = QPushButton(self.settings_frame)
        self.pb_eraser.setObjectName(u"pb_eraser")
        sizePolicy1.setHeightForWidth(self.pb_eraser.sizePolicy().hasHeightForWidth())
        self.pb_eraser.setSizePolicy(sizePolicy1)
        self.pb_eraser.setMinimumSize(QSize(100, 0))
        self.pb_eraser.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffffff;\n"
"}")

        self.verticalLayout_2.addWidget(self.pb_eraser, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.brush_size_text = QLabel(self.settings_frame)
        self.brush_size_text.setObjectName(u"brush_size_text")
        sizePolicy2.setHeightForWidth(self.brush_size_text.sizePolicy().hasHeightForWidth())
        self.brush_size_text.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.brush_size_text)

        self.h_slider_brushSize = QSlider(self.settings_frame)
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

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.background_picker.raise_()
        self.h_slider_brushSize.raise_()
        self.brush_size_text.raise_()
        self.color_picker.raise_()
        self.color_name_text.raise_()
        self.bg_color_text.raise_()
        self.pb_eraser.raise_()
        self.pb_brush.raise_()

        self.gridLayout.addWidget(self.settings_frame, 0, 0, 1, 1)


        self.retranslateUi(settings_ui)

        QMetaObject.connectSlotsByName(settings_ui)
    # setupUi

    def retranslateUi(self, settings_ui):
        settings_ui.setWindowTitle(QCoreApplication.translate("settings_ui", u"Settings UI", None))
        self.color_picker.setText("")
        self.color_name_text.setText(QCoreApplication.translate("settings_ui", u"#000000", None))
        self.pb_brush.setText("")
        self.pb_black_button.setText("")
        self.pb_color_button.setText("")
        self.pb_white_button.setText("")
        self.background_picker.setText("")
        self.bg_color_text.setText(QCoreApplication.translate("settings_ui", u"#ffffff", None))
        self.pb_eraser.setText("")
        self.brush_size_text.setText(QCoreApplication.translate("settings_ui", u"Brush Size:", None))
    # retranslateUi

