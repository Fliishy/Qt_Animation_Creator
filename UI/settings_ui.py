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
import icons_rc

class Ui_settings_ui(object):
    def setupUi(self, settings_ui):
        if not settings_ui.objectName():
            settings_ui.setObjectName(u"settings_ui")
        settings_ui.resize(793, 826)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings_ui.sizePolicy().hasHeightForWidth())
        settings_ui.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/buttons/brush.png", QSize(), QIcon.Normal, QIcon.Off)
        settings_ui.setWindowIcon(icon)
        self.gridLayout = QGridLayout(settings_ui)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settings_frame = QFrame(settings_ui)
        self.settings_frame.setObjectName(u"settings_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settings_frame.sizePolicy().hasHeightForWidth())
        self.settings_frame.setSizePolicy(sizePolicy1)
        self.settings_frame.setMinimumSize(QSize(250, 0))
        self.settings_frame.setStyleSheet(u"color:black;")
        self.settings_frame.setFrameShape(QFrame.Box)
        self.settings_frame.setFrameShadow(QFrame.Plain)
        self.settings_frame.setLineWidth(0)
        self.settings_frame.setMidLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.settings_frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer_6 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.v_layout_settings = QVBoxLayout()
        self.v_layout_settings.setSpacing(10)
        self.v_layout_settings.setObjectName(u"v_layout_settings")
        self.v_layout_settings.setContentsMargins(-1, 0, -1, 0)
        self.v_layout_color_picker = QVBoxLayout()
        self.v_layout_color_picker.setSpacing(10)
        self.v_layout_color_picker.setObjectName(u"v_layout_color_picker")
        self.v_layout_color_picker.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.v_layout_color_picker.setContentsMargins(-1, 0, -1, 0)
        self.color_picker = QLabel(self.settings_frame)
        self.color_picker.setObjectName(u"color_picker")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.color_picker.sizePolicy().hasHeightForWidth())
        self.color_picker.setSizePolicy(sizePolicy2)
        self.color_picker.setMinimumSize(QSize(180, 180))
        self.color_picker.setMouseTracking(True)
        self.color_picker.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.color_picker.setStyleSheet(u"QLabel{\n"
"	background-color: #000000;\n"
"	border-radius: 90%;\n"
"	border: 1px solid black;\n"
"}")
        self.color_picker.setScaledContents(False)
        self.color_picker.setAlignment(Qt.AlignCenter)

        self.v_layout_color_picker.addWidget(self.color_picker, 0, Qt.AlignHCenter)

        self.color_name_text = QLabel(self.settings_frame)
        self.color_name_text.setObjectName(u"color_name_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.color_name_text.sizePolicy().hasHeightForWidth())
        self.color_name_text.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(13)
        self.color_name_text.setFont(font)
        self.color_name_text.setAlignment(Qt.AlignCenter)

        self.v_layout_color_picker.addWidget(self.color_name_text)


        self.v_layout_settings.addLayout(self.v_layout_color_picker)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.v_layout_settings.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pb_brush = QPushButton(self.settings_frame)
        self.pb_brush.setObjectName(u"pb_brush")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pb_brush.sizePolicy().hasHeightForWidth())
        self.pb_brush.setSizePolicy(sizePolicy4)
        self.pb_brush.setMinimumSize(QSize(100, 0))
        self.pb_brush.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffffff;\n"
"}")
        self.pb_brush.setIcon(icon)
        self.pb_brush.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pb_brush)

        self.pb_eraser = QPushButton(self.settings_frame)
        self.pb_eraser.setObjectName(u"pb_eraser")
        sizePolicy4.setHeightForWidth(self.pb_eraser.sizePolicy().hasHeightForWidth())
        self.pb_eraser.setSizePolicy(sizePolicy4)
        self.pb_eraser.setMinimumSize(QSize(100, 0))
        self.pb_eraser.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffffff;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_eraser.setIcon(icon1)
        self.pb_eraser.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pb_eraser)


        self.v_layout_settings.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.v_layout_settings.addItem(self.verticalSpacer_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.brush_size_text = QLabel(self.settings_frame)
        self.brush_size_text.setObjectName(u"brush_size_text")
        sizePolicy2.setHeightForWidth(self.brush_size_text.sizePolicy().hasHeightForWidth())
        self.brush_size_text.setSizePolicy(sizePolicy2)
        self.brush_size_text.setMinimumSize(QSize(83, 0))
        self.brush_size_text.setSizeIncrement(QSize(0, 0))
        self.brush_size_text.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.brush_size_text.setFont(font1)
        self.brush_size_text.setAutoFillBackground(False)
        self.brush_size_text.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.brush_size_text)

        self.brush_size_number = QLabel(self.settings_frame)
        self.brush_size_number.setObjectName(u"brush_size_number")
        sizePolicy.setHeightForWidth(self.brush_size_number.sizePolicy().hasHeightForWidth())
        self.brush_size_number.setSizePolicy(sizePolicy)
        self.brush_size_number.setMinimumSize(QSize(0, 0))
        self.brush_size_number.setSizeIncrement(QSize(0, 0))
        self.brush_size_number.setBaseSize(QSize(0, 0))
        self.brush_size_number.setFont(font1)
        self.brush_size_number.setStyleSheet(u"")
        self.brush_size_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.brush_size_number)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.h_slider_brushSize = QSlider(self.settings_frame)
        self.h_slider_brushSize.setObjectName(u"h_slider_brushSize")
        sizePolicy3.setHeightForWidth(self.h_slider_brushSize.sizePolicy().hasHeightForWidth())
        self.h_slider_brushSize.setSizePolicy(sizePolicy3)
        self.h_slider_brushSize.setMinimumSize(QSize(216, 20))
        self.h_slider_brushSize.setBaseSize(QSize(0, 0))
        self.h_slider_brushSize.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #19a9bd;\n"
"    height: 10px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #00f0ff, stop:1 #13cbe5);\n"
"    margin: 2px 0;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #a0faff, stop:1 #93eef3);\n"
"    border: 1px solid #19a9bd;\n"
"	width: 15px;\n"
"    margin: -4px 0; \n"
"    border-radius: 8px;\n"
"}")
        self.h_slider_brushSize.setMinimum(1)
        self.h_slider_brushSize.setMaximum(50)
        self.h_slider_brushSize.setSingleStep(1)
        self.h_slider_brushSize.setValue(10)
        self.h_slider_brushSize.setOrientation(Qt.Horizontal)
        self.h_slider_brushSize.setInvertedAppearance(False)
        self.h_slider_brushSize.setInvertedControls(False)
        self.h_slider_brushSize.setTickPosition(QSlider.NoTicks)
        self.h_slider_brushSize.setTickInterval(12)

        self.verticalLayout.addWidget(self.h_slider_brushSize)


        self.v_layout_settings.addLayout(self.verticalLayout)

        self.h_layout_color_buttons = QHBoxLayout()
        self.h_layout_color_buttons.setSpacing(10)
        self.h_layout_color_buttons.setObjectName(u"h_layout_color_buttons")
        self.h_layout_color_buttons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.h_layout_color_buttons.setContentsMargins(-1, 10, -1, 0)
        self.pb_black_button = QPushButton(self.settings_frame)
        self.pb_black_button.setObjectName(u"pb_black_button")
        self.pb_black_button.setMinimumSize(QSize(0, 30))
        self.pb_black_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #000000;\n"
"}")
        self.pb_black_button.setIcon(icon)
        self.pb_black_button.setIconSize(QSize(20, 20))

        self.h_layout_color_buttons.addWidget(self.pb_black_button)

        self.pb_color_button = QPushButton(self.settings_frame)
        self.pb_color_button.setObjectName(u"pb_color_button")
        self.pb_color_button.setMinimumSize(QSize(0, 30))
        self.pb_color_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #f471ff;\n"
"}")
        self.pb_color_button.setIcon(icon)
        self.pb_color_button.setIconSize(QSize(20, 20))
        self.pb_color_button.setAutoRepeat(False)
        self.pb_color_button.setAutoDefault(False)
        self.pb_color_button.setFlat(False)

        self.h_layout_color_buttons.addWidget(self.pb_color_button)

        self.pb_white_button = QPushButton(self.settings_frame)
        self.pb_white_button.setObjectName(u"pb_white_button")
        self.pb_white_button.setMinimumSize(QSize(0, 30))
        self.pb_white_button.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffffff;\n"
"}")
        self.pb_white_button.setIcon(icon)
        self.pb_white_button.setIconSize(QSize(20, 20))

        self.h_layout_color_buttons.addWidget(self.pb_white_button)


        self.v_layout_settings.addLayout(self.h_layout_color_buttons)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.v_layout_settings.addItem(self.verticalSpacer_5)

        self.v_layout_bg_picker = QVBoxLayout()
        self.v_layout_bg_picker.setSpacing(10)
        self.v_layout_bg_picker.setObjectName(u"v_layout_bg_picker")
        self.background_picker = QLabel(self.settings_frame)
        self.background_picker.setObjectName(u"background_picker")
        sizePolicy2.setHeightForWidth(self.background_picker.sizePolicy().hasHeightForWidth())
        self.background_picker.setSizePolicy(sizePolicy2)
        self.background_picker.setMinimumSize(QSize(200, 150))
        self.background_picker.setMouseTracking(True)
        self.background_picker.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.background_picker.setStyleSheet(u"QLabel{\n"
"	background-color: #ffffff;	\n"
"	border: 1px solid black;\n"
"}")
        self.background_picker.setScaledContents(False)
        self.background_picker.setAlignment(Qt.AlignCenter)

        self.v_layout_bg_picker.addWidget(self.background_picker, 0, Qt.AlignHCenter)

        self.bg_color_text = QLabel(self.settings_frame)
        self.bg_color_text.setObjectName(u"bg_color_text")
        sizePolicy3.setHeightForWidth(self.bg_color_text.sizePolicy().hasHeightForWidth())
        self.bg_color_text.setSizePolicy(sizePolicy3)
        self.bg_color_text.setFont(font)
        self.bg_color_text.setAlignment(Qt.AlignCenter)

        self.v_layout_bg_picker.addWidget(self.bg_color_text)


        self.v_layout_settings.addLayout(self.v_layout_bg_picker)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.v_layout_settings.addItem(self.verticalSpacer_4)


        self.verticalLayout_2.addLayout(self.v_layout_settings)


        self.gridLayout.addWidget(self.settings_frame, 1, 0, 1, 1)

        QWidget.setTabOrder(self.pb_black_button, self.pb_color_button)
        QWidget.setTabOrder(self.pb_color_button, self.pb_white_button)

        self.retranslateUi(settings_ui)

        self.pb_color_button.setDefault(False)


        QMetaObject.connectSlotsByName(settings_ui)
    # setupUi

    def retranslateUi(self, settings_ui):
        settings_ui.setWindowTitle(QCoreApplication.translate("settings_ui", u"Settings UI", None))
        self.color_picker.setText("")
        self.color_name_text.setText(QCoreApplication.translate("settings_ui", u"#000000", None))
        self.pb_brush.setText("")
        self.pb_eraser.setText("")
        self.brush_size_text.setText(QCoreApplication.translate("settings_ui", u"Brush Size:", None))
        self.brush_size_number.setText(QCoreApplication.translate("settings_ui", u"10", None))
        self.pb_black_button.setText("")
        self.pb_color_button.setText("")
        self.pb_white_button.setText("")
        self.background_picker.setText("")
        self.bg_color_text.setText(QCoreApplication.translate("settings_ui", u"#ffffff", None))
    # retranslateUi

