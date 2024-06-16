# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crawlingiDudND.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QDialog,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1324, 1050)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(800, 30, 71, 41))
        font = QFont()
        font.setPointSize(19)
        self.label_5.setFont(font)
        self.lineEdit_keyword = QLineEdit(Dialog)
        self.lineEdit_keyword.setObjectName(u"lineEdit_keyword")
        self.lineEdit_keyword.setGeometry(QRect(10, 70, 361, 61))
        font1 = QFont()
        font1.setPointSize(28)
        self.lineEdit_keyword.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 70, 131, 61))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 160, 121, 16))
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 190, 491, 741))
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 40, 161, 21))
        self.label_10.setFont(font)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(510, 10, 16, 921))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.group_option = QGroupBox(Dialog)
        self.group_option.setObjectName(u"group_option")
        self.group_option.setGeometry(QRect(530, 70, 621, 891))
        self.option_wordcloud = QCheckBox(self.group_option)
        self.option_wordcloud.setObjectName(u"option_wordcloud")
        self.option_wordcloud.setGeometry(QRect(10, 450, 121, 20))
        self.group_num = QGroupBox(self.group_option)
        self.group_num.setObjectName(u"group_num")
        self.group_num.setGeometry(QRect(190, 80, 421, 80))
        self.slider_num = QSlider(self.group_num)
        self.slider_num.setObjectName(u"slider_num")
        self.slider_num.setGeometry(QRect(10, 50, 391, 22))
        self.slider_num.setMinimum(1)
        self.slider_num.setMaximum(10000)
        self.slider_num.setOrientation(Qt.Orientation.Horizontal)
        self.label_16 = QLabel(self.group_num)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(270, 30, 60, 21))
        font2 = QFont()
        font2.setPointSize(18)
        self.label_16.setFont(font2)
        self.lineEdit_num = QLineEdit(self.group_num)
        self.lineEdit_num.setObjectName(u"lineEdit_num")
        self.lineEdit_num.setGeometry(QRect(140, 30, 113, 21))
        font3 = QFont()
        font3.setPointSize(15)
        self.lineEdit_num.setFont(font3)
        self.group_date = QGroupBox(self.group_option)
        self.group_date.setObjectName(u"group_date")
        self.group_date.setGeometry(QRect(190, 176, 362, 261))
        self.gridLayout_4 = QGridLayout(self.group_date)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.end_date = QCalendarWidget(self.group_date)
        self.end_date.setObjectName(u"end_date")
        font4 = QFont()
        font4.setPointSize(8)
        self.end_date.setFont(font4)
        self.end_date.setGridVisible(True)
        self.end_date.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)

        self.gridLayout_4.addWidget(self.end_date, 2, 1, 1, 1)

        self.label_17 = QLabel(self.group_date)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_18 = QLabel(self.group_date)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)

        self.start_date = QCalendarWidget(self.group_date)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setFont(font4)
        self.start_date.setGridVisible(True)
        self.start_date.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.start_date.setNavigationBarVisible(True)
        self.start_date.setDateEditEnabled(True)

        self.gridLayout_4.addWidget(self.start_date, 2, 0, 1, 1)

        self.label_start_date = QLabel(self.group_date)
        self.label_start_date.setObjectName(u"label_start_date")

        self.gridLayout_4.addWidget(self.label_start_date, 1, 0, 1, 1)

        self.label_end_date = QLabel(self.group_date)
        self.label_end_date.setObjectName(u"label_end_date")

        self.gridLayout_4.addWidget(self.label_end_date, 1, 1, 1, 1)

        self.group_excel = QGroupBox(self.group_option)
        self.group_excel.setObjectName(u"group_excel")
        self.group_excel.setGeometry(QRect(190, 10, 331, 71))
        self.horizontalLayout_4 = QHBoxLayout(self.group_excel)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.filename = QLineEdit(self.group_excel)
        self.filename.setObjectName(u"filename")
        self.filename.setFont(font3)

        self.horizontalLayout_4.addWidget(self.filename)

        self.label_19 = QLabel(self.group_excel)
        self.label_19.setObjectName(u"label_19")
        font5 = QFont()
        font5.setPointSize(17)
        font5.setBold(True)
        self.label_19.setFont(font5)

        self.horizontalLayout_4.addWidget(self.label_19)

        self.option_excel = QCheckBox(self.group_option)
        self.option_excel.setObjectName(u"option_excel")
        self.option_excel.setGeometry(QRect(10, 30, 131, 21))
        self.option_date = QCheckBox(self.group_option)
        self.option_date.setObjectName(u"option_date")
        self.option_date.setGeometry(QRect(10, 200, 87, 20))
        self.verticalLayoutWidget = QWidget(self.group_option)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 480, 401, 401))
        self.layout_wordcloud = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_wordcloud.setObjectName(u"layout_wordcloud")
        self.layout_wordcloud.setContentsMargins(0, 0, 0, 0)
        self.option_num = QCheckBox(self.group_option)
        self.option_num.setObjectName(u"option_num")
        self.option_num.setGeometry(QRect(10, 90, 171, 20))
        self.wordcloud_status = QLabel(self.group_option)
        self.wordcloud_status.setObjectName(u"wordcloud_status")
        self.wordcloud_status.setGeometry(QRect(180, 450, 411, 21))
        font6 = QFont()
        font6.setPointSize(16)
        self.wordcloud_status.setFont(font6)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(530, 970, 621, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"(\uc635\uc158)", None))
        self.lineEdit_keyword.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\ud06c\ub864\ub9c1 \uc2dc\uc791", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\ud06c\ub864\ub9c1 \uacb0\uacfc", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\ud0a4\uc6cc\ub4dc \uc785\ub825", None))
        self.group_option.setTitle("")
        self.option_wordcloud.setText(QCoreApplication.translate("Dialog", u"\ub2e8\uc5b4 \uad6c\ub984 \ubcf4\uae30", None))
        self.group_num.setTitle(QCoreApplication.translate("Dialog", u"\ucd5c\ub300 \ud06c\ub864\ub9c1 \uac2f\uc218\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\uac1c", None))
        self.lineEdit_num.setText("")
        self.group_date.setTitle(QCoreApplication.translate("Dialog", u"\ub0a0\uc9dc\ub97c \uc9c0\uc815\ud574\uc8fc\uc138\uc694.", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uc791 \ub0a0\uc9dc", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\ub05d \ub0a0\uc9dc", None))
        self.label_start_date.setText("")
        self.label_end_date.setText("")
        self.group_excel.setTitle(QCoreApplication.translate("Dialog", u"\uc5d1\uc140 \ud30c\uc77c\uba85\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.filename.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u".xlsx", None))
        self.option_excel.setText(QCoreApplication.translate("Dialog", u"\uc5d1\uc140\uc5d0 \uae30\ub85d\ud558\uae30", None))
        self.option_date.setText(QCoreApplication.translate("Dialog", u"\ub0a0\uc9dc \uc9c0\uc815", None))
        self.option_num.setText(QCoreApplication.translate("Dialog", u"\ucd5c\ub300 \ud06c\ub864\ub9c1 \uac2f\uc218 \uc815\ud558\uae30", None))
        self.wordcloud_status.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\ub274\uc2a4 \uae30\uc0ac \uac10\uc131 \ubd84\uc11d", None))
    # retranslateUi

