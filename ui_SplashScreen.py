# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashScreenOOAUqr.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(716, 439)
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(46, 52, 81);\n"
"	color: rgb(220,220,220);\n"
"	border-radius: 10px\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.HeadingLabel = QLabel(self.dropShadowFrame)
        self.HeadingLabel.setObjectName(u"HeadingLabel")
        self.HeadingLabel.setGeometry(QRect(0, 80, 661, 91))
        font = QFont()
        font.setPointSize(36)
        self.HeadingLabel.setFont(font)
        self.HeadingLabel.setStyleSheet(u"color: rgb(254,121,199)")
        self.HeadingLabel.setAlignment(Qt.AlignCenter)
        self.DiscriptionLabel = QLabel(self.dropShadowFrame)
        self.DiscriptionLabel.setObjectName(u"DiscriptionLabel")
        self.DiscriptionLabel.setGeometry(QRect(0, 150, 691, 31))
        self.DiscriptionLabel.setFont(font)
        self.DiscriptionLabel.setStyleSheet(u"color:white")
        self.DiscriptionLabel.setAlignment(Qt.AlignCenter)
        self.MainProgressBar = QProgressBar(self.dropShadowFrame)
        self.MainProgressBar.setObjectName(u"MainProgressBar")
        self.MainProgressBar.setGeometry(QRect(60, 240, 571, 16))
        self.MainProgressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(39, 78, 117);\n"
"	color: rgb(200,200,200);\n"
"	border-style: none;\n"
"	border-collapse: separate; \n"
"	border-radius: 8px;\n"
"	text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-collapse: separate; \n"
"	border-radius: 8px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.528409, x2:1, y2:0.528409, stop:0 rgba(255, 0, 205, 255), stop:1 rgba(167, 32, 255, 255))\n"
"}")
        self.MainProgressBar.setValue(24)
        self.Credits = QLabel(self.dropShadowFrame)
        self.Credits.setObjectName(u"Credits")
        self.Credits.setGeometry(QRect(20, 380, 661, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.Credits.setFont(font1)
        self.Credits.setStyleSheet(u"color:white")
        self.Credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.dropShadowFrame)

        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"MainWindow", None))
        self.HeadingLabel.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p>Accreditation<span style=\" font-weight:900;\"/><span style=\" font-size:28pt; vertical-align:super;\">Engine</span></p></body></html>", None))
        self.DiscriptionLabel.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p><span style=\" font-size:18pt;\">Fast and Easy... </span><span style=\" font-size:18pt; vertical-align:sub;\">Powered by A.I</span></p></body></html>", None))
        self.Credits.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Created by:</span><span style=\" font-size:10pt;\"> Mike S. Kiwalabye</span></p></body></html>", None))
    # retranslateUi

