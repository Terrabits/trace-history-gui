# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qtrf.widgets import IPAddressLineEdit


class Ui_Connect(object):
    def setupUi(self, Connect):
        if not Connect.objectName():
            Connect.setObjectName(u"Connect")
        Connect.resize(388, 147)
        self.formLayout = QFormLayout(Connect)
        self.formLayout.setObjectName(u"formLayout")
        self.methodLabel = QLabel(Connect)
        self.methodLabel.setObjectName(u"methodLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methodLabel.sizePolicy().hasHeightForWidth())
        self.methodLabel.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.methodLabel)

        self.methods = QGroupBox(Connect)
        self.methods.setObjectName(u"methods")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.methods.sizePolicy().hasHeightForWidth())
        self.methods.setSizePolicy(sizePolicy1)
        self.methods.setFlat(True)
        self.methods.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.methods)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.isTcp = QRadioButton(self.methods)
        self.isTcp.setObjectName(u"isTcp")
        self.isTcp.setChecked(True)

        self.horizontalLayout.addWidget(self.isTcp)

        self.isVisa = QRadioButton(self.methods)
        self.isVisa.setObjectName(u"isVisa")

        self.horizontalLayout.addWidget(self.isVisa)

        self.methodsSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.methodsSpacer)

        self.horizontalLayout.setStretch(2, 1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.methods)

        self.endpointLabel = QLabel(Connect)
        self.endpointLabel.setObjectName(u"endpointLabel")
        sizePolicy.setHeightForWidth(self.endpointLabel.sizePolicy().hasHeightForWidth())
        self.endpointLabel.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.endpointLabel)

        self.endpointPages = QStackedWidget(Connect)
        self.endpointPages.setObjectName(u"endpointPages")
        sizePolicy.setHeightForWidth(self.endpointPages.sizePolicy().hasHeightForWidth())
        self.endpointPages.setSizePolicy(sizePolicy)
        self.endpointPages.setMinimumSize(QSize(200, 0))
        self.tcpEndpointPage = QWidget()
        self.tcpEndpointPage.setObjectName(u"tcpEndpointPage")
        sizePolicy.setHeightForWidth(self.tcpEndpointPage.sizePolicy().hasHeightForWidth())
        self.tcpEndpointPage.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.tcpEndpointPage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tcpHost = IPAddressLineEdit(self.tcpEndpointPage)
        self.tcpHost.setObjectName(u"tcpHost")

        self.horizontalLayout_2.addWidget(self.tcpHost)

        self.endpointPages.addWidget(self.tcpEndpointPage)
        self.visaEndpointPage = QWidget()
        self.visaEndpointPage.setObjectName(u"visaEndpointPage")
        sizePolicy.setHeightForWidth(self.visaEndpointPage.sizePolicy().hasHeightForWidth())
        self.visaEndpointPage.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.visaEndpointPage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.visaResource = QLineEdit(self.visaEndpointPage)
        self.visaResource.setObjectName(u"visaResource")

        self.horizontalLayout_3.addWidget(self.visaResource)

        self.endpointPages.addWidget(self.visaEndpointPage)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.endpointPages)

        self.connectButtonLabelSpacer = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.connectButtonLabelSpacer)

        self.connectButtonWidget = QWidget(Connect)
        self.connectButtonWidget.setObjectName(u"connectButtonWidget")
        sizePolicy.setHeightForWidth(self.connectButtonWidget.sizePolicy().hasHeightForWidth())
        self.connectButtonWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.connectButtonWidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.connect = QPushButton(self.connectButtonWidget)
        self.connect.setObjectName(u"connect")

        self.horizontalLayout_4.addWidget(self.connect)

        self.connectButtonSpacer = QSpacerItem(549, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.connectButtonSpacer)

        self.horizontalLayout_4.setStretch(1, 1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.connectButtonWidget)

        QWidget.setTabOrder(self.isTcp, self.isVisa)
        QWidget.setTabOrder(self.isVisa, self.tcpHost)
        QWidget.setTabOrder(self.tcpHost, self.visaResource)
        QWidget.setTabOrder(self.visaResource, self.connect)

        self.retranslateUi(Connect)

        self.endpointPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Connect)
    # setupUi

    def retranslateUi(self, Connect):
        Connect.setWindowTitle(QCoreApplication.translate("Connect", u"GroupBox", None))
        Connect.setTitle(QCoreApplication.translate("Connect", u"Instrument Connection", None))
        self.methodLabel.setText(QCoreApplication.translate("Connect", u"Method", None))
        self.methods.setTitle("")
        self.isTcp.setText(QCoreApplication.translate("Connect", u"TCP", None))
        self.isVisa.setText(QCoreApplication.translate("Connect", u"VISA", None))
        self.endpointLabel.setText(QCoreApplication.translate("Connect", u"Host", None))
        self.tcpHost.setPlaceholderText(QCoreApplication.translate("Connect", u"e.g. ZNA43-123456", None))
        self.visaResource.setPlaceholderText(QCoreApplication.translate("Connect", u"e.g. TCPIP::192.168.1.25::INSTR", None))
        self.connect.setText(QCoreApplication.translate("Connect", u"Connect", None))
    # retranslateUi

