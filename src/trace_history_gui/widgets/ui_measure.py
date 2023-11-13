# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'measure.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

from qtrf.widgets import (FileWidget, IntValueLineEdit, SecondsLineEdit)

class Ui_Measure(object):
    def setupUi(self, Measure):
        if not Measure.objectName():
            Measure.setObjectName(u"Measure")
        Measure.resize(368, 213)
        self.formLayout = QFormLayout(Measure)
        self.formLayout.setObjectName(u"formLayout")
        self.setFileLabel = QLabel(Measure)
        self.setFileLabel.setObjectName(u"setFileLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.setFileLabel)

        self.sweepCountLabel = QLabel(Measure)
        self.sweepCountLabel.setObjectName(u"sweepCountLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sweepCountLabel)

        self.timeoutLabel = QLabel(Measure)
        self.timeoutLabel.setObjectName(u"timeoutLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.timeoutLabel)

        self.dataPathLabel = QLabel(Measure)
        self.dataPathLabel.setObjectName(u"dataPathLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.dataPathLabel)

        self.dataPath = FileWidget(Measure)
        self.dataPath.setObjectName(u"dataPath")
        self.dataPath.setMinimumSize(QSize(250, 0))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dataPath)

        self.setFile = QComboBox(Measure)
        self.setFile.addItem("")
        self.setFile.setObjectName(u"setFile")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.setFile)

        self.sweepCount = IntValueLineEdit(Measure)
        self.sweepCount.setObjectName(u"sweepCount")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sweepCount)

        self.timeout_s = SecondsLineEdit(Measure)
        self.timeout_s.setObjectName(u"timeout_s")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.timeout_s)

        self.startWidget = QWidget(Measure)
        self.startWidget.setObjectName(u"startWidget")
        self.horizontalLayout = QHBoxLayout(self.startWidget)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.start = QPushButton(self.startWidget)
        self.start.setObjectName(u"start")

        self.horizontalLayout.addWidget(self.start)

        self.startSpacer = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.startSpacer)

        self.settings = QPushButton(self.startWidget)
        self.settings.setObjectName(u"settings")

        self.horizontalLayout.addWidget(self.settings)


        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.startWidget)

        QWidget.setTabOrder(self.setFile, self.sweepCount)
        QWidget.setTabOrder(self.sweepCount, self.timeout_s)
        QWidget.setTabOrder(self.timeout_s, self.start)

        self.retranslateUi(Measure)

        QMetaObject.connectSlotsByName(Measure)
    # setupUi

    def retranslateUi(self, Measure):
        Measure.setWindowTitle(QCoreApplication.translate("Measure", u"GroupBox", None))
        Measure.setTitle(QCoreApplication.translate("Measure", u"Measure", None))
        self.setFileLabel.setText(QCoreApplication.translate("Measure", u"Set File", None))
        self.sweepCountLabel.setText(QCoreApplication.translate("Measure", u"Sweep Count", None))
        self.timeoutLabel.setText(QCoreApplication.translate("Measure", u"Timeout", None))
        self.dataPathLabel.setText(QCoreApplication.translate("Measure", u"Data Path", None))
        self.setFile.setItemText(0, QCoreApplication.translate("Measure", u"<Current Set>", None))

        self.start.setText(QCoreApplication.translate("Measure", u"Start", None))
        self.settings.setText(QCoreApplication.translate("Measure", u"\u2699\ufe0f", None))
    # retranslateUi

