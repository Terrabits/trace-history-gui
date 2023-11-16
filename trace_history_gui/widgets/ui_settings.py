# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qtrf.widgets import SecondsLineEdit


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.setWindowModality(Qt.ApplicationModal)
        Settings.resize(256, 165)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formInput = QWidget(Settings)
        self.formInput.setObjectName(u"formInput")
        self.formLayout = QFormLayout(self.formInput)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.delayLabel = QLabel(self.formInput)
        self.delayLabel.setObjectName(u"delayLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.delayLabel)

        self.delay_s = SecondsLineEdit(self.formInput)
        self.delay_s.setObjectName(u"delay_s")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.delay_s)

        self.timeoutLabel = QLabel(self.formInput)
        self.timeoutLabel.setObjectName(u"timeoutLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.timeoutLabel)

        self.timeout_s = SecondsLineEdit(self.formInput)
        self.timeout_s.setObjectName(u"timeout_s")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.timeout_s)


        self.verticalLayout.addWidget(self.formInput)

        self.displayMeasurementCompleteDialog = QCheckBox(Settings)
        self.displayMeasurementCompleteDialog.setObjectName(u"displayMeasurementCompleteDialog")

        self.verticalLayout.addWidget(self.displayMeasurementCompleteDialog)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonsWidget = QWidget(Settings)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.horizontalLayout = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel = QPushButton(self.buttonsWidget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.cancel)

        self.ok = QPushButton(self.buttonsWidget)
        self.ok.setObjectName(u"ok")

        self.horizontalLayout.addWidget(self.ok)


        self.verticalLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(Settings)

        self.ok.setDefault(True)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.delayLabel.setText(QCoreApplication.translate("Settings", u"Delay", None))
        self.timeoutLabel.setText(QCoreApplication.translate("Settings", u"Timeout", None))
        self.displayMeasurementCompleteDialog.setText(QCoreApplication.translate("Settings", u"Show measurement complete dialog", None))
        self.cancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
        self.ok.setText(QCoreApplication.translate("Settings", u"Ok", None))
    # retranslateUi

