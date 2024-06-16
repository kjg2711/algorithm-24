# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchxPHRXf.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTableView, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1560, 835)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 21, 301, 181))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 210, 161, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 210, 131, 31))
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 250, 851, 551))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(890, 80, 661, 731))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(890, 30, 651, 41))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 30, 571, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 70, 511, 31))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 110, 501, 31))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 150, 511, 31))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 210, 441, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_6.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SEARCH", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uae30\uc0ac \ubcf8\ubb38</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"\uae30\uc0ac \uc81c\ubaa9", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc11c\uc6d0\ub300\ud559\uad50 \ucef4\ud4e8\ud130\uacf5\ud559\uacfc \uc1a1\uc7ac\ucc2c(\ud300\uc7a5)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\uc11c\uc6d0\ub300\ud559\uad50 \ucef4\ud4e8\ud130\uacf5\ud559\uacfc \uae40\uc885\uaddc(\ud300\uc6d0)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc11c\uc6d0\ub300\ud559\uad50 \ucef4\ud4e8\ud130\uacf5\ud559\uacfc \uc11c\ud558\uc81c(\ud300\uc6d0)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\uc11c\uc6d0\ub300\ud559\uad50 \ucef4\ud4e8\ud130\uacf5\ud559\uacfc \uc784\uc218\ud658(\ud300\uc6d0)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\uc5d1\uc140 \ud30c\uc77c -> \ub2e8\uc5b4 \ucc3e\uae30 -> \ub2e8\uc5b4\uac00 \ud3ec\ud568\ub41c \ub274\uc2a4 \ubc18\ud658 -> \ud074\ub9ad \uc2dc, \ubcf8\ubb38 \ucd9c\ub825", None))
    # retranslateUi

