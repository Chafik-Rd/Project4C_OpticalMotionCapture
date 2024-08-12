# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_motion.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QToolBox, QToolButton,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1339, 985)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.load_menu = QGridLayout()
        self.load_menu.setObjectName(u"load_menu")
        self.checkBox_sync = QCheckBox(self.centralwidget)
        self.checkBox_sync.setObjectName(u"checkBox_sync")

        self.load_menu.addWidget(self.checkBox_sync, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.load_menu.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_LV1 = QLabel(self.centralwidget)
        self.label_LV1.setObjectName(u"label_LV1")
        font = QFont()
        font.setPointSize(10)
        self.label_LV1.setFont(font)

        self.horizontalLayout.addWidget(self.label_LV1)

        self.lineEdit_LV1 = QLineEdit(self.centralwidget)
        self.lineEdit_LV1.setObjectName(u"lineEdit_LV1")

        self.horizontalLayout.addWidget(self.lineEdit_LV1)

        self.toolButton_LV1 = QToolButton(self.centralwidget)
        self.toolButton_LV1.setObjectName(u"toolButton_LV1")

        self.horizontalLayout.addWidget(self.toolButton_LV1)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_LV2 = QLabel(self.centralwidget)
        self.label_LV2.setObjectName(u"label_LV2")
        self.label_LV2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_LV2)

        self.lineEdit_LV2 = QLineEdit(self.centralwidget)
        self.lineEdit_LV2.setObjectName(u"lineEdit_LV2")

        self.horizontalLayout_2.addWidget(self.lineEdit_LV2)

        self.toolButton_LV2 = QToolButton(self.centralwidget)
        self.toolButton_LV2.setObjectName(u"toolButton_LV2")

        self.horizontalLayout_2.addWidget(self.toolButton_LV2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.load_menu.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setObjectName(u"btn_load")

        self.load_menu.addWidget(self.btn_load, 0, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.load_menu)

        self.tab = QTabWidget(self.centralwidget)
        self.tab.setObjectName(u"tab")
        self.tab.setFont(font)
        self.cali = QWidget()
        self.cali.setObjectName(u"cali")
        self.horizontalLayout_3 = QHBoxLayout(self.cali)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.video_show = QVBoxLayout()
        self.video_show.setObjectName(u"video_show")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.calibrat_side_frame = PlotWidget(self.cali)
        self.calibrat_side_frame.setObjectName(u"calibrat_side_frame")

        self.horizontalLayout_6.addWidget(self.calibrat_side_frame)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer)

        self.calibrat_top_frame = PlotWidget(self.cali)
        self.calibrat_top_frame.setObjectName(u"calibrat_top_frame")

        self.horizontalLayout_6.addWidget(self.calibrat_top_frame)


        self.video_show.addLayout(self.horizontalLayout_6)

        self.groupBox_6 = QGroupBox(self.cali)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calibrat_sli_frame = QSlider(self.groupBox_6)
        self.calibrat_sli_frame.setObjectName(u"calibrat_sli_frame")
        self.calibrat_sli_frame.setMaximum(100)
        self.calibrat_sli_frame.setPageStep(30)
        self.calibrat_sli_frame.setOrientation(Qt.Horizontal)
        self.calibrat_sli_frame.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_9.addWidget(self.calibrat_sli_frame)


        self.video_show.addWidget(self.groupBox_6)


        self.horizontalLayout_3.addLayout(self.video_show)

        self.side_menu = QVBoxLayout()
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.calibrat_checkBox_opencv = QCheckBox(self.cali)
        self.calibrat_checkBox_opencv.setObjectName(u"calibrat_checkBox_opencv")

        self.gridLayout_3.addWidget(self.calibrat_checkBox_opencv, 9, 1, 1, 1, Qt.AlignRight)

        self.calibrat_spinBox_y = QSpinBox(self.cali)
        self.calibrat_spinBox_y.setObjectName(u"calibrat_spinBox_y")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_y.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_y.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_y.setAccelerated(True)
        self.calibrat_spinBox_y.setMinimum(-50)
        self.calibrat_spinBox_y.setMaximum(50)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_y, 7, 2, 1, 1)

        self.calibrat_spinBox_Wboard = QSpinBox(self.cali)
        self.calibrat_spinBox_Wboard.setObjectName(u"calibrat_spinBox_Wboard")
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_Wboard.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_Wboard.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_Wboard.setAccelerated(True)
        self.calibrat_spinBox_Wboard.setValue(10)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_Wboard, 1, 2, 1, 1)

        self.label_z = QLabel(self.cali)
        self.label_z.setObjectName(u"label_z")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_z.sizePolicy().hasHeightForWidth())
        self.label_z.setSizePolicy(sizePolicy1)
        self.label_z.setFont(font)

        self.gridLayout_3.addWidget(self.label_z, 8, 1, 1, 1, Qt.AlignRight)

        self.calibrat_spinBox_z = QSpinBox(self.cali)
        self.calibrat_spinBox_z.setObjectName(u"calibrat_spinBox_z")
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_z.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_z.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_z.setAccelerated(True)
        self.calibrat_spinBox_z.setMinimum(-50)
        self.calibrat_spinBox_z.setMaximum(50)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_z, 8, 2, 1, 1)

        self.calibrat_spinBox_drgree = QSpinBox(self.cali)
        self.calibrat_spinBox_drgree.setObjectName(u"calibrat_spinBox_drgree")
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_drgree.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_drgree.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_drgree.setValue(50)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_drgree, 3, 2, 1, 1)

        self.label = QLabel(self.cali)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1, Qt.AlignRight)

        self.calibrat_btn_store = QPushButton(self.cali)
        self.calibrat_btn_store.setObjectName(u"calibrat_btn_store")

        self.gridLayout_3.addWidget(self.calibrat_btn_store, 9, 2, 1, 1)

        self.calibrat_spinBox_sizesq = QSpinBox(self.cali)
        self.calibrat_spinBox_sizesq.setObjectName(u"calibrat_spinBox_sizesq")
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_sizesq.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_sizesq.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_sizesq.setAccelerated(True)
        self.calibrat_spinBox_sizesq.setMinimum(-99)
        self.calibrat_spinBox_sizesq.setValue(25)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_sizesq, 4, 2, 1, 1)

        self.calibrat_btn_reset = QPushButton(self.cali)
        self.calibrat_btn_reset.setObjectName(u"calibrat_btn_reset")
        self.calibrat_btn_reset.setFont(font)

        self.gridLayout_3.addWidget(self.calibrat_btn_reset, 10, 2, 1, 1)

        self.calibrat_btn_undo = QPushButton(self.cali)
        self.calibrat_btn_undo.setObjectName(u"calibrat_btn_undo")
        self.calibrat_btn_undo.setFont(font)

        self.gridLayout_3.addWidget(self.calibrat_btn_undo, 10, 1, 1, 1)

        self.label_2 = QLabel(self.cali)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1, Qt.AlignRight)

        self.calibrat_spinBox_Hboard = QSpinBox(self.cali)
        self.calibrat_spinBox_Hboard.setObjectName(u"calibrat_spinBox_Hboard")
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_Hboard.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_Hboard.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_Hboard.setValue(7)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_Hboard, 2, 2, 1, 1)

        self.calibrat_btn_save = QPushButton(self.cali)
        self.calibrat_btn_save.setObjectName(u"calibrat_btn_save")
        self.calibrat_btn_save.setFont(font)

        self.gridLayout_3.addWidget(self.calibrat_btn_save, 12, 2, 1, 1)

        self.label_x = QLabel(self.cali)
        self.label_x.setObjectName(u"label_x")
        sizePolicy1.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy1)
        self.label_x.setFont(font)

        self.gridLayout_3.addWidget(self.label_x, 6, 1, 1, 1, Qt.AlignRight)

        self.label_3 = QLabel(self.cali)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 1, 1, 1, Qt.AlignRight)

        self.calibrat_btn_cali = QPushButton(self.cali)
        self.calibrat_btn_cali.setObjectName(u"calibrat_btn_cali")
        self.calibrat_btn_cali.setFont(font)

        self.gridLayout_3.addWidget(self.calibrat_btn_cali, 12, 1, 1, 1)

        self.label_4 = QLabel(self.cali)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 1, 1, 1, Qt.AlignRight)

        self.label_y = QLabel(self.cali)
        self.label_y.setObjectName(u"label_y")
        sizePolicy1.setHeightForWidth(self.label_y.sizePolicy().hasHeightForWidth())
        self.label_y.setSizePolicy(sizePolicy1)
        self.label_y.setFont(font)

        self.gridLayout_3.addWidget(self.label_y, 7, 1, 1, 1, Qt.AlignRight)

        self.calibrat_spinBox_x = QSpinBox(self.cali)
        self.calibrat_spinBox_x.setObjectName(u"calibrat_spinBox_x")
        sizePolicy.setHeightForWidth(self.calibrat_spinBox_x.sizePolicy().hasHeightForWidth())
        self.calibrat_spinBox_x.setSizePolicy(sizePolicy)
        self.calibrat_spinBox_x.setAccelerated(True)
        self.calibrat_spinBox_x.setMinimum(-50)
        self.calibrat_spinBox_x.setMaximum(50)

        self.gridLayout_3.addWidget(self.calibrat_spinBox_x, 6, 2, 1, 1)


        self.side_menu.addLayout(self.gridLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.side_menu.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.side_menu)

        self.tab.addTab(self.cali, "")
        self.cali_result = QWidget()
        self.cali_result.setObjectName(u"cali_result")
        self.verticalLayout = QVBoxLayout(self.cali_result)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cali_result_frame = PlotWidget(self.cali_result)
        self.cali_result_frame.setObjectName(u"cali_result_frame")

        self.verticalLayout.addWidget(self.cali_result_frame)

        self.groupBox_5 = QGroupBox(self.cali_result)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.calibrat_result_sli_frame = QSlider(self.groupBox_5)
        self.calibrat_result_sli_frame.setObjectName(u"calibrat_result_sli_frame")
        self.calibrat_result_sli_frame.setPageStep(3)
        self.calibrat_result_sli_frame.setOrientation(Qt.Horizontal)
        self.calibrat_result_sli_frame.setInvertedAppearance(False)
        self.calibrat_result_sli_frame.setInvertedControls(False)

        self.verticalLayout_5.addWidget(self.calibrat_result_sli_frame)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.tab.addTab(self.cali_result, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.detect_side_frame = PlotWidget(self.tab_2)
        self.detect_side_frame.setObjectName(u"detect_side_frame")

        self.horizontalLayout_25.addWidget(self.detect_side_frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_25.addItem(self.verticalSpacer_3)

        self.detect_top_frame = PlotWidget(self.tab_2)
        self.detect_top_frame.setObjectName(u"detect_top_frame")

        self.horizontalLayout_25.addWidget(self.detect_top_frame)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.groupBox_9 = QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.detect_sli_frame = QSlider(self.groupBox_9)
        self.detect_sli_frame.setObjectName(u"detect_sli_frame")
        self.detect_sli_frame.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.detect_sli_frame)


        self.verticalLayout_12.addWidget(self.groupBox_9)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.detect_toolBox = QToolBox(self.tab_2)
        self.detect_toolBox.setObjectName(u"detect_toolBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.detect_toolBox.sizePolicy().hasHeightForWidth())
        self.detect_toolBox.setSizePolicy(sizePolicy2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 329, 368))
        self.verticalLayout_13 = QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox = QGroupBox(self.page_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.color_comboBox = QComboBox(self.groupBox)
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.addItem("")
        self.color_comboBox.setObjectName(u"color_comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.color_comboBox.sizePolicy().hasHeightForWidth())
        self.color_comboBox.setSizePolicy(sizePolicy4)
        self.color_comboBox.setEditable(True)

        self.horizontalLayout_20.addWidget(self.color_comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.color_hue_min_side = QSlider(self.groupBox_2)
        self.color_hue_min_side.setObjectName(u"color_hue_min_side")
        self.color_hue_min_side.setMaximum(179)
        self.color_hue_min_side.setPageStep(1)
        self.color_hue_min_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.color_hue_min_side)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.color_hue_max_side = QSlider(self.groupBox_2)
        self.color_hue_max_side.setObjectName(u"color_hue_max_side")
        self.color_hue_max_side.setMaximum(179)
        self.color_hue_max_side.setPageStep(1)
        self.color_hue_max_side.setValue(179)
        self.color_hue_max_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.color_hue_max_side)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)

        self.color_sat_min_side = QSlider(self.groupBox_2)
        self.color_sat_min_side.setObjectName(u"color_sat_min_side")
        self.color_sat_min_side.setMaximum(255)
        self.color_sat_min_side.setPageStep(1)
        self.color_sat_min_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.color_sat_min_side)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.color_sat_max_side = QSlider(self.groupBox_2)
        self.color_sat_max_side.setObjectName(u"color_sat_max_side")
        self.color_sat_max_side.setMaximum(255)
        self.color_sat_max_side.setPageStep(1)
        self.color_sat_max_side.setValue(255)
        self.color_sat_max_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.color_sat_max_side)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.color_value_min_side = QSlider(self.groupBox_2)
        self.color_value_min_side.setObjectName(u"color_value_min_side")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.color_value_min_side.setFont(font1)
        self.color_value_min_side.setMouseTracking(False)
        self.color_value_min_side.setTabletTracking(False)
        self.color_value_min_side.setFocusPolicy(Qt.StrongFocus)
        self.color_value_min_side.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.color_value_min_side.setAcceptDrops(False)
        self.color_value_min_side.setMaximum(255)
        self.color_value_min_side.setPageStep(1)
        self.color_value_min_side.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.color_value_min_side)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.color_value_max_side = QSlider(self.groupBox_2)
        self.color_value_max_side.setObjectName(u"color_value_max_side")
        self.color_value_max_side.setMaximum(255)
        self.color_value_max_side.setPageStep(1)
        self.color_value_max_side.setValue(255)
        self.color_value_max_side.setTracking(True)
        self.color_value_max_side.setOrientation(Qt.Horizontal)
        self.color_value_max_side.setInvertedAppearance(False)
        self.color_value_max_side.setInvertedControls(False)
        self.color_value_max_side.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_13.addWidget(self.color_value_max_side)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_14.addWidget(self.label_7)

        self.color_hue_min_top = QSlider(self.groupBox_3)
        self.color_hue_min_top.setObjectName(u"color_hue_min_top")
        self.color_hue_min_top.setMaximum(179)
        self.color_hue_min_top.setPageStep(1)
        self.color_hue_min_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.color_hue_min_top)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_19.addWidget(self.label_12)

        self.color_hue_max_top = QSlider(self.groupBox_3)
        self.color_hue_max_top.setObjectName(u"color_hue_max_top")
        self.color_hue_max_top.setMaximum(179)
        self.color_hue_max_top.setPageStep(1)
        self.color_hue_max_top.setValue(179)
        self.color_hue_max_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.color_hue_max_top)


        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_18.addWidget(self.label_13)

        self.color_sat_min_top = QSlider(self.groupBox_3)
        self.color_sat_min_top.setObjectName(u"color_sat_min_top")
        self.color_sat_min_top.setMaximum(255)
        self.color_sat_min_top.setPageStep(1)
        self.color_sat_min_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_18.addWidget(self.color_sat_min_top)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.color_sat_max_top = QSlider(self.groupBox_3)
        self.color_sat_max_top.setObjectName(u"color_sat_max_top")
        self.color_sat_max_top.setMaximum(255)
        self.color_sat_max_top.setPageStep(1)
        self.color_sat_max_top.setValue(255)
        self.color_sat_max_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.color_sat_max_top)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.color_value_min_top = QSlider(self.groupBox_3)
        self.color_value_min_top.setObjectName(u"color_value_min_top")
        self.color_value_min_top.setMaximum(255)
        self.color_value_min_top.setPageStep(1)
        self.color_value_min_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.color_value_min_top)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_15.addWidget(self.label_16)

        self.color_value_max_top = QSlider(self.groupBox_3)
        self.color_value_max_top.setObjectName(u"color_value_max_top")
        self.color_value_max_top.setMaximum(255)
        self.color_value_max_top.setPageStep(1)
        self.color_value_max_top.setValue(255)
        self.color_value_max_top.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.color_value_max_top)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)

        self.color_btn_undo = QPushButton(self.groupBox)
        self.color_btn_undo.setObjectName(u"color_btn_undo")

        self.horizontalLayout_21.addWidget(self.color_btn_undo)

        self.color_btn_save = QPushButton(self.groupBox)
        self.color_btn_save.setObjectName(u"color_btn_save")

        self.horizontalLayout_21.addWidget(self.color_btn_save)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_21)


        self.verticalLayout_13.addWidget(self.groupBox)

        self.detect_toolBox.addItem(self.page_3, u"Color Setting")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 1289, 192))
        self.horizontalLayout_22 = QHBoxLayout(self.page_4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.groupBox_7 = QGroupBox(self.page_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy2.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy2)
        self.gridLayout_5 = QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 3, 0, 1, 1, Qt.AlignRight)

        self.detect_spinBox_setW = QSpinBox(self.groupBox_7)
        self.detect_spinBox_setW.setObjectName(u"detect_spinBox_setW")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.detect_spinBox_setW.sizePolicy().hasHeightForWidth())
        self.detect_spinBox_setW.setSizePolicy(sizePolicy5)
        self.detect_spinBox_setW.setMaximumSize(QSize(100, 22))
        self.detect_spinBox_setW.setMaximum(2000)
        self.detect_spinBox_setW.setValue(1920)

        self.gridLayout_5.addWidget(self.detect_spinBox_setW, 2, 1, 1, 1)

        self.detect_spinBox_setH = QSpinBox(self.groupBox_7)
        self.detect_spinBox_setH.setObjectName(u"detect_spinBox_setH")
        self.detect_spinBox_setH.setMaximumSize(QSize(16777215, 22))
        self.detect_spinBox_setH.setMaximum(2000)
        self.detect_spinBox_setH.setValue(1080)

        self.gridLayout_5.addWidget(self.detect_spinBox_setH, 3, 1, 1, 1)

        self.detect_btn_start = QPushButton(self.groupBox_7)
        self.detect_btn_start.setObjectName(u"detect_btn_start")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.detect_btn_start.sizePolicy().hasHeightForWidth())
        self.detect_btn_start.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.detect_btn_start, 4, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_7)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1, Qt.AlignRight)

        self.detect_btn_stop = QPushButton(self.groupBox_7)
        self.detect_btn_stop.setObjectName(u"detect_btn_stop")
        sizePolicy6.setHeightForWidth(self.detect_btn_stop.sizePolicy().hasHeightForWidth())
        self.detect_btn_stop.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.detect_btn_stop, 5, 0, 1, 1)

        self.detect_spinBox_start = QSpinBox(self.groupBox_7)
        self.detect_spinBox_start.setObjectName(u"detect_spinBox_start")
        self.detect_spinBox_start.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_5.addWidget(self.detect_spinBox_start, 4, 1, 1, 1)

        self.detect_spinBox_stop = QSpinBox(self.groupBox_7)
        self.detect_spinBox_stop.setObjectName(u"detect_spinBox_stop")
        self.detect_spinBox_stop.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_5.addWidget(self.detect_spinBox_stop, 5, 1, 1, 1)


        self.horizontalLayout_22.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.page_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy7)
        self.gridLayout_2 = QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.detect_btn_savevideo = QPushButton(self.groupBox_8)
        self.detect_btn_savevideo.setObjectName(u"detect_btn_savevideo")
        sizePolicy6.setHeightForWidth(self.detect_btn_savevideo.sizePolicy().hasHeightForWidth())
        self.detect_btn_savevideo.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.detect_btn_savevideo, 1, 1, 1, 1)

        self.detect_btn_run = QPushButton(self.groupBox_8)
        self.detect_btn_run.setObjectName(u"detect_btn_run")
        sizePolicy6.setHeightForWidth(self.detect_btn_run.sizePolicy().hasHeightForWidth())
        self.detect_btn_run.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.detect_btn_run, 1, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.page_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy7.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy7)
        self.gridLayout_4 = QGridLayout(self.groupBox_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.detect_lineEdit_filepoint = QLineEdit(self.groupBox_10)
        self.detect_lineEdit_filepoint.setObjectName(u"detect_lineEdit_filepoint")
        sizePolicy.setHeightForWidth(self.detect_lineEdit_filepoint.sizePolicy().hasHeightForWidth())
        self.detect_lineEdit_filepoint.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.detect_lineEdit_filepoint)

        self.detect_toolButton_filepoint = QToolButton(self.groupBox_10)
        self.detect_toolButton_filepoint.setObjectName(u"detect_toolButton_filepoint")
        sizePolicy.setHeightForWidth(self.detect_toolButton_filepoint.sizePolicy().hasHeightForWidth())
        self.detect_toolButton_filepoint.setSizePolicy(sizePolicy)
        self.detect_toolButton_filepoint.setMaximumSize(QSize(27, 22))

        self.horizontalLayout_4.addWidget(self.detect_toolButton_filepoint)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.detect_checkBox_opencv = QCheckBox(self.groupBox_10)
        self.detect_checkBox_opencv.setObjectName(u"detect_checkBox_opencv")

        self.gridLayout_4.addWidget(self.detect_checkBox_opencv, 3, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_4.addWidget(self.label_20, 2, 0, 1, 1)

        self.detect_btn_plot = QPushButton(self.groupBox_10)
        self.detect_btn_plot.setObjectName(u"detect_btn_plot")
        sizePolicy6.setHeightForWidth(self.detect_btn_plot.sizePolicy().hasHeightForWidth())
        self.detect_btn_plot.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.detect_btn_plot, 3, 1, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.detect_lineEdit_filecalibrat = QLineEdit(self.groupBox_10)
        self.detect_lineEdit_filecalibrat.setObjectName(u"detect_lineEdit_filecalibrat")
        sizePolicy.setHeightForWidth(self.detect_lineEdit_filecalibrat.sizePolicy().hasHeightForWidth())
        self.detect_lineEdit_filecalibrat.setSizePolicy(sizePolicy)

        self.horizontalLayout_26.addWidget(self.detect_lineEdit_filecalibrat)

        self.detect_toolButton_filecalibrat = QToolButton(self.groupBox_10)
        self.detect_toolButton_filecalibrat.setObjectName(u"detect_toolButton_filecalibrat")
        sizePolicy.setHeightForWidth(self.detect_toolButton_filecalibrat.sizePolicy().hasHeightForWidth())
        self.detect_toolButton_filecalibrat.setSizePolicy(sizePolicy)
        self.detect_toolButton_filecalibrat.setMaximumSize(QSize(27, 22))

        self.horizontalLayout_26.addWidget(self.detect_toolButton_filecalibrat)


        self.gridLayout_4.addLayout(self.horizontalLayout_26, 2, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.groupBox_10)

        self.detect_toolBox.addItem(self.page_4, u"Processing")

        self.verticalLayout_11.addWidget(self.detect_toolBox)

        self.tab.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tab)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1339, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab.setCurrentIndex(0)
        self.detect_toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox_sync.setText(QCoreApplication.translate("MainWindow", u"Sync", None))
        self.label_LV1.setText(QCoreApplication.translate("MainWindow", u"Load Side Video", None))
        self.toolButton_LV1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_LV2.setText(QCoreApplication.translate("MainWindow", u"Load Top Video", None))
        self.toolButton_LV2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Frame", None))
        self.calibrat_checkBox_opencv.setText(QCoreApplication.translate("MainWindow", u"OpenCV", None))
        self.calibrat_spinBox_y.setSuffix(QCoreApplication.translate("MainWindow", u" cm", None))
        self.calibrat_spinBox_Wboard.setSuffix(QCoreApplication.translate("MainWindow", u" point", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
#if QT_CONFIG(tooltip)
        self.calibrat_spinBox_z.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.calibrat_spinBox_z.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.calibrat_spinBox_z.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.calibrat_spinBox_z.setSpecialValueText("")
        self.calibrat_spinBox_z.setSuffix(QCoreApplication.translate("MainWindow", u" cm", None))
        self.calibrat_spinBox_drgree.setSuffix(QCoreApplication.translate("MainWindow", u" degree", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"W_Board:", None))
        self.calibrat_btn_store.setText(QCoreApplication.translate("MainWindow", u"Store", None))
        self.calibrat_spinBox_sizesq.setSuffix(QCoreApplication.translate("MainWindow", u" mm", None))
        self.calibrat_btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.calibrat_btn_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"H_Board:", None))
        self.calibrat_spinBox_Hboard.setSuffix(QCoreApplication.translate("MainWindow", u" point", None))
        self.calibrat_btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Degree_XZ:", None))
        self.calibrat_btn_cali.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Size_sq:", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.calibrat_spinBox_x.setSuffix(QCoreApplication.translate("MainWindow", u" cm", None))
        self.tab.setTabText(self.tab.indexOf(self.cali), QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Frame", None))
        self.tab.setTabText(self.tab.indexOf(self.cali_result), QCoreApplication.translate("MainWindow", u"Calibration Result", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Frame", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"HSV Color", None))
        self.color_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pink", None))
        self.color_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.color_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.color_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.color_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Red", None))
        self.color_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.color_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Purple", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Side", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"HUE Min:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HUE Max:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SAT Min:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SAT Max:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"VALUE Min:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"VALUE Max:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Top", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"HUE Min:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"HUE Max:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SAT Min:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SAT Max:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"VALUE Min:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"VALUE Max:", None))
        self.color_btn_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.color_btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.detect_toolBox.setItemText(self.detect_toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Color Setting", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Set Video", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Set Height:", None))
        self.detect_btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Set Width:", None))
        self.detect_btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Process", None))
        self.detect_btn_savevideo.setText(QCoreApplication.translate("MainWindow", u"Save Video", None))
        self.detect_btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Plot Graph", None))
        self.detect_toolButton_filepoint.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.detect_checkBox_opencv.setText(QCoreApplication.translate("MainWindow", u"OpenCV", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"File Calibration:", None))
        self.detect_btn_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.detect_toolButton_filecalibrat.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"File Points Detect:", None))
        self.detect_toolBox.setItemText(self.detect_toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Processing", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Detect", None))
    # retranslateUi

