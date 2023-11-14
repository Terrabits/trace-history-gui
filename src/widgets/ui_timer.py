# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLCDNumber, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Timer(object):
    def setupUi(self, Timer):
        if not Timer.objectName():
            Timer.setObjectName(u"Timer")
        Timer.resize(88, 47)
        self.verticalLayout = QVBoxLayout(Timer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lcd = QLCDNumber(Timer)
        self.lcd.setObjectName(u"lcd")

        self.verticalLayout.addWidget(self.lcd)


        self.retranslateUi(Timer)

        QMetaObject.connectSlotsByName(Timer)
    # setupUi

    def retranslateUi(self, Timer):
        Timer.setWindowTitle(QCoreApplication.translate("Timer", u"Timer", None))
    # retranslateUi

