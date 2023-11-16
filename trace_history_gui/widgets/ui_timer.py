# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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

