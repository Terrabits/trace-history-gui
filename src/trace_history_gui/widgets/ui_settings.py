# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qtrf.widgets import SecondsLineEdit

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.setWindowModality(Qt.ApplicationModal)
        Settings.resize(219, 160)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.delayWidget = QWidget(Settings)
        self.delayWidget.setObjectName(u"delayWidget")
        self.formLayout = QFormLayout(self.delayWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.delayLabel = QLabel(self.delayWidget)
        self.delayLabel.setObjectName(u"delayLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.delayLabel)

        self.delay_s = SecondsLineEdit(self.delayWidget)
        self.delay_s.setObjectName(u"delay_s")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.delay_s)


        self.verticalLayout.addWidget(self.delayWidget)

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
        self.displayMeasurementCompleteDialog.setText(QCoreApplication.translate("Settings", u"Measurement complete dialog", None))
        self.cancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
        self.ok.setText(QCoreApplication.translate("Settings", u"Ok", None))
    # retranslateUi

