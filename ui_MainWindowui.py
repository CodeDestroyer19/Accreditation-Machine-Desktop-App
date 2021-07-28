# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowuiLkcOyE.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QSize(1000, 700))
        font = QFont()
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	border-radius: 10px\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Nav = QFrame(self.centralwidget)
        self.Nav.setObjectName(u"Nav")
        self.Nav.setMinimumSize(QSize(0, 45))
        self.Nav.setMaximumSize(QSize(16777215, 45))
        self.Nav.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.438, y1:0, x2:1, y2:0, stop:0 rgba(1, 0, 91, 255), stop:1 rgba(87, 0, 144, 255));")
        self.Nav.setFrameShape(QFrame.NoFrame)
        self.Nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Nav)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NavMenuButtonHolder = QFrame(self.Nav)
        self.NavMenuButtonHolder.setObjectName(u"NavMenuButtonHolder")
        self.NavMenuButtonHolder.setMinimumSize(QSize(70, 0))
        self.NavMenuButtonHolder.setMaximumSize(QSize(50, 16777215))
        self.NavMenuButtonHolder.setStyleSheet(u"background-color: rgb(60, 60,55);")
        self.NavMenuButtonHolder.setFrameShape(QFrame.NoFrame)
        self.NavMenuButtonHolder.setFrameShadow(QFrame.Plain)
        self.NavMenuButtonHolder.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.NavMenuButtonHolder)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MenuButton = QPushButton(self.NavMenuButtonHolder)
        self.MenuButton.setObjectName(u"MenuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuButton.sizePolicy().hasHeightForWidth())
        self.MenuButton.setSizePolicy(sizePolicy)
        self.MenuButton.setStyleSheet(u"width: 100%;\n"
"height: 100%;\n"
"color: white;\n"
"border: 0px solid")
        self.MenuButton.setAutoDefault(False)
        self.MenuButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.MenuButton)


        self.horizontalLayout_2.addWidget(self.NavMenuButtonHolder)

        self.NavMainContainer = QFrame(self.Nav)
        self.NavMainContainer.setObjectName(u"NavMainContainer")
        self.NavMainContainer.setStyleSheet(u"")
        self.NavMainContainer.setFrameShape(QFrame.StyledPanel)
        self.NavMainContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.NavMainContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.InfoFrame = QFrame(self.NavMainContainer)
        self.InfoFrame.setObjectName(u"InfoFrame")
        self.InfoFrame.setMinimumSize(QSize(0, 45))
        self.InfoFrame.setMaximumSize(QSize(16777215, 45))
        self.InfoFrame.setStyleSheet(u"background-color: transparent;")
        self.InfoFrame.setFrameShape(QFrame.NoFrame)
        self.InfoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.InfoFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PageInfoFrame = QFrame(self.InfoFrame)
        self.PageInfoFrame.setObjectName(u"PageInfoFrame")
        self.PageInfoFrame.setMinimumSize(QSize(0, 20))
        self.PageInfoFrame.setMaximumSize(QSize(200, 20))
        self.PageInfoFrame.setStyleSheet(u"background-color: transparent")
        self.PageInfoFrame.setFrameShape(QFrame.NoFrame)
        self.PageInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.PageInfoFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(8, 0, 0, 0)
        self.PageInfo = QLabel(self.PageInfoFrame)
        self.PageInfo.setObjectName(u"PageInfo")
        self.PageInfo.setMinimumSize(QSize(0, 20))
        self.PageInfo.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.PageInfo.setFont(font1)
        self.PageInfo.setStyleSheet(u"color: white;\n"
"background-color: transparent")

        self.verticalLayout_7.addWidget(self.PageInfo)


        self.gridLayout.addWidget(self.PageInfoFrame, 1, 0, 1, 1)

        self.WindowNameFrame = QFrame(self.InfoFrame)
        self.WindowNameFrame.setObjectName(u"WindowNameFrame")
        self.WindowNameFrame.setMinimumSize(QSize(0, 20))
        self.WindowNameFrame.setMaximumSize(QSize(16777215, 25))
        self.WindowNameFrame.setStyleSheet(u"")
        self.WindowNameFrame.setFrameShape(QFrame.NoFrame)
        self.WindowNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.WindowNameFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(8, 0, 0, 0)
        self.WindoName = QLabel(self.WindowNameFrame)
        self.WindoName.setObjectName(u"WindoName")
        self.WindoName.setMinimumSize(QSize(0, 25))
        self.WindoName.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.WindoName.setFont(font2)
        self.WindoName.setStyleSheet(u"color: white")
        self.WindoName.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_6.addWidget(self.WindoName)


        self.gridLayout.addWidget(self.WindowNameFrame, 0, 0, 1, 3)

        self.MainInfoFrame = QFrame(self.InfoFrame)
        self.MainInfoFrame.setObjectName(u"MainInfoFrame")
        self.MainInfoFrame.setMinimumSize(QSize(0, 20))
        self.MainInfoFrame.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setPointSize(14)
        self.MainInfoFrame.setFont(font3)
        self.MainInfoFrame.setStyleSheet(u"background-color: transparent")
        self.MainInfoFrame.setFrameShape(QFrame.NoFrame)
        self.MainInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.MainInfoFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 0, 0, 0)
        self.MainInfo = QLabel(self.MainInfoFrame)
        self.MainInfo.setObjectName(u"MainInfo")
        self.MainInfo.setMinimumSize(QSize(0, 20))
        self.MainInfo.setMaximumSize(QSize(16777215, 20))
        self.MainInfo.setFont(font3)
        self.MainInfo.setStyleSheet(u"color: white;\n"
"background-color: transparent")

        self.verticalLayout_8.addWidget(self.MainInfo)


        self.gridLayout.addWidget(self.MainInfoFrame, 1, 1, 1, 2)

        self.PageInfoFrame.raise_()
        self.MainInfoFrame.raise_()
        self.WindowNameFrame.raise_()

        self.horizontalLayout_3.addWidget(self.InfoFrame)

        self.WindowOperationsFrame = QFrame(self.NavMainContainer)
        self.WindowOperationsFrame.setObjectName(u"WindowOperationsFrame")
        self.WindowOperationsFrame.setMaximumSize(QSize(100, 16777215))
        self.WindowOperationsFrame.setStyleSheet(u"background-color: transparent;")
        self.WindowOperationsFrame.setFrameShape(QFrame.StyledPanel)
        self.WindowOperationsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.WindowOperationsFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Minimize = QPushButton(self.WindowOperationsFrame)
        self.Minimize.setObjectName(u"Minimize")
        self.Minimize.setMinimumSize(QSize(20, 20))
        self.Minimize.setMaximumSize(QSize(20, 20))
        self.Minimize.setStyleSheet(u"border-radius: 10px;\n"
"background-color:rgb(72, 218, 0);")

        self.horizontalLayout_4.addWidget(self.Minimize)

        self.Maximize = QPushButton(self.WindowOperationsFrame)
        self.Maximize.setObjectName(u"Maximize")
        self.Maximize.setMinimumSize(QSize(20, 20))
        self.Maximize.setMaximumSize(QSize(20, 20))
        self.Maximize.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(255, 157, 0);")

        self.horizontalLayout_4.addWidget(self.Maximize)

        self.Exit = QPushButton(self.WindowOperationsFrame)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setMinimumSize(QSize(20, 20))
        self.Exit.setMaximumSize(QSize(20, 20))
        self.Exit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: red;")

        self.horizontalLayout_4.addWidget(self.Exit)


        self.horizontalLayout_3.addWidget(self.WindowOperationsFrame)


        self.horizontalLayout_2.addWidget(self.NavMainContainer)


        self.verticalLayout.addWidget(self.Nav)

        self.MainContainer = QFrame(self.centralwidget)
        self.MainContainer.setObjectName(u"MainContainer")
        self.MainContainer.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.MainContainer.setFrameShape(QFrame.NoFrame)
        self.MainContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MainContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Menu = QFrame(self.MainContainer)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMinimumSize(QSize(70, 0))
        self.Menu.setMaximumSize(QSize(50, 16777215))
        self.Menu.setStyleSheet(u"background-color: rgb(60, 60,55);")
        self.Menu.setFrameShape(QFrame.NoFrame)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ButtonContainerMenu = QFrame(self.Menu)
        self.ButtonContainerMenu.setObjectName(u"ButtonContainerMenu")
        self.ButtonContainerMenu.setMinimumSize(QSize(0, 250))
        self.ButtonContainerMenu.setLayoutDirection(Qt.LeftToRight)
        self.ButtonContainerMenu.setFrameShape(QFrame.NoFrame)
        self.ButtonContainerMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ButtonContainerMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.HomeButton = QPushButton(self.ButtonContainerMenu)
        self.HomeButton.setObjectName(u"HomeButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy1)
        self.HomeButton.setMinimumSize(QSize(0, 40))
        self.HomeButton.setMaximumSize(QSize(16777215, 40))
        self.HomeButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(86, 0, 143);\n"
"}")

        self.verticalLayout_4.addWidget(self.HomeButton)

        self.RenameButton = QPushButton(self.ButtonContainerMenu)
        self.RenameButton.setObjectName(u"RenameButton")
        sizePolicy1.setHeightForWidth(self.RenameButton.sizePolicy().hasHeightForWidth())
        self.RenameButton.setSizePolicy(sizePolicy1)
        self.RenameButton.setMinimumSize(QSize(0, 40))
        self.RenameButton.setMaximumSize(QSize(16777215, 40))
        self.RenameButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(86, 0, 143);\n"
"}")

        self.verticalLayout_4.addWidget(self.RenameButton)

        self.EditDocButton = QPushButton(self.ButtonContainerMenu)
        self.EditDocButton.setObjectName(u"EditDocButton")
        sizePolicy1.setHeightForWidth(self.EditDocButton.sizePolicy().hasHeightForWidth())
        self.EditDocButton.setSizePolicy(sizePolicy1)
        self.EditDocButton.setMinimumSize(QSize(0, 40))
        self.EditDocButton.setMaximumSize(QSize(16777215, 40))
        self.EditDocButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(86, 0, 143);\n"
"}")

        self.verticalLayout_4.addWidget(self.EditDocButton)

        self.UploadButton = QPushButton(self.ButtonContainerMenu)
        self.UploadButton.setObjectName(u"UploadButton")
        sizePolicy1.setHeightForWidth(self.UploadButton.sizePolicy().hasHeightForWidth())
        self.UploadButton.setSizePolicy(sizePolicy1)
        self.UploadButton.setMinimumSize(QSize(0, 40))
        self.UploadButton.setMaximumSize(QSize(16777215, 40))
        self.UploadButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(86, 0, 143);\n"
"}")

        self.verticalLayout_4.addWidget(self.UploadButton)

        self.ConvertButton = QPushButton(self.ButtonContainerMenu)
        self.ConvertButton.setObjectName(u"ConvertButton")
        sizePolicy1.setHeightForWidth(self.ConvertButton.sizePolicy().hasHeightForWidth())
        self.ConvertButton.setSizePolicy(sizePolicy1)
        self.ConvertButton.setMinimumSize(QSize(0, 40))
        self.ConvertButton.setMaximumSize(QSize(16777215, 40))
        self.ConvertButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(86, 0, 143);\n"
"}")

        self.verticalLayout_4.addWidget(self.ConvertButton)

        self.Replace = QPushButton(self.ButtonContainerMenu)
        self.Replace.setObjectName(u"Replace")
        self.Replace.setMinimumSize(QSize(40, 0))
        self.Replace.setMaximumSize(QSize(16777215, 40))
        self.Replace.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: rgb(60,60,60);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(86, 0, 143);\n"
"}")

        self.verticalLayout_4.addWidget(self.Replace)


        self.verticalLayout_3.addWidget(self.ButtonContainerMenu, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.Menu)

        self.Content_right = QFrame(self.MainContainer)
        self.Content_right.setObjectName(u"Content_right")
        self.Content_right.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.438, y1:0, x2:1, y2:0, stop:0 rgba(1, 0, 91, 255), stop:1 rgba(87, 0, 144, 255))")
        self.Content_right.setFrameShape(QFrame.StyledPanel)
        self.Content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Content_right)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PageHolder = QStackedWidget(self.Content_right)
        self.PageHolder.setObjectName(u"PageHolder")
        self.PageHolder.setFont(font)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.horizontalLayout_5 = QHBoxLayout(self.Home)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.Home)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(48)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: white\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.PageHolder.addWidget(self.Home)
        self.Rename = QWidget()
        self.Rename.setObjectName(u"Rename")
        self.verticalLayout_9 = QVBoxLayout(self.Rename)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.RenameFilesORFoldersFrame = QFrame(self.Rename)
        self.RenameFilesORFoldersFrame.setObjectName(u"RenameFilesORFoldersFrame")
        self.RenameFilesORFoldersFrame.setMaximumSize(QSize(16777215, 60))
        self.RenameFilesORFoldersFrame.setFrameShape(QFrame.StyledPanel)
        self.RenameFilesORFoldersFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.RenameFilesORFoldersFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.RenameFilesORFoldersLabel = QLabel(self.RenameFilesORFoldersFrame)
        self.RenameFilesORFoldersLabel.setObjectName(u"RenameFilesORFoldersLabel")
        font5 = QFont()
        font5.setPointSize(36)
        self.RenameFilesORFoldersLabel.setFont(font5)
        self.RenameFilesORFoldersLabel.setStyleSheet(u"color: white")

        self.verticalLayout_10.addWidget(self.RenameFilesORFoldersLabel)


        self.verticalLayout_9.addWidget(self.RenameFilesORFoldersFrame)

        self.BodyFrameRenamePage = QFrame(self.Rename)
        self.BodyFrameRenamePage.setObjectName(u"BodyFrameRenamePage")
        self.BodyFrameRenamePage.setFrameShape(QFrame.StyledPanel)
        self.BodyFrameRenamePage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.BodyFrameRenamePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ButtonHolderRenamePage = QFrame(self.BodyFrameRenamePage)
        self.ButtonHolderRenamePage.setObjectName(u"ButtonHolderRenamePage")
        self.ButtonHolderRenamePage.setMaximumSize(QSize(16777215, 40))
        self.ButtonHolderRenamePage.setStyleSheet(u"background-color: transparent")
        self.ButtonHolderRenamePage.setFrameShape(QFrame.StyledPanel)
        self.ButtonHolderRenamePage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ButtonHolderRenamePage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.OpenFileFolder = QPushButton(self.ButtonHolderRenamePage)
        self.OpenFileFolder.setObjectName(u"OpenFileFolder")
        self.OpenFileFolder.setMaximumSize(QSize(360, 16777215))
        font6 = QFont()
        font6.setPointSize(12)
        self.OpenFileFolder.setFont(font6)
        self.OpenFileFolder.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.horizontalLayout_6.addWidget(self.OpenFileFolder)

        self.OpenFolderDir = QPushButton(self.ButtonHolderRenamePage)
        self.OpenFolderDir.setObjectName(u"OpenFolderDir")
        self.OpenFolderDir.setMaximumSize(QSize(360, 16777215))
        self.OpenFolderDir.setFont(font6)
        self.OpenFolderDir.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.horizontalLayout_6.addWidget(self.OpenFolderDir)

        self.OpenFolderHolder = QPushButton(self.ButtonHolderRenamePage)
        self.OpenFolderHolder.setObjectName(u"OpenFolderHolder")
        self.OpenFolderHolder.setFont(font6)
        self.OpenFolderHolder.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.horizontalLayout_6.addWidget(self.OpenFolderHolder)


        self.verticalLayout_11.addWidget(self.ButtonHolderRenamePage, 0, Qt.AlignLeft)

        self.ContentHolderRenamePage = QStackedWidget(self.BodyFrameRenamePage)
        self.ContentHolderRenamePage.setObjectName(u"ContentHolderRenamePage")
        self.ContentHolderRenamePage.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    height: 15px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: white;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.ContentHolderRenamePage.setFrameShape(QFrame.StyledPanel)
        self.ContentHolderRenamePage.setFrameShadow(QFrame.Raised)
        self.ContentHolderRenamePage1 = QWidget()
        self.ContentHolderRenamePage1.setObjectName(u"ContentHolderRenamePage1")
        self.horizontalLayout_10 = QHBoxLayout(self.ContentHolderRenamePage1)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.UserInputRenamePageFrame = QFrame(self.ContentHolderRenamePage1)
        self.UserInputRenamePageFrame.setObjectName(u"UserInputRenamePageFrame")
        self.UserInputRenamePageFrame.setMaximumSize(QSize(250, 16777215))
        self.UserInputRenamePageFrame.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: 0px solid white;\n"
"	color: white\n"
"}\n"
"\n"
"")
        self.UserInputRenamePageFrame.setFrameShape(QFrame.NoFrame)
        self.UserInputRenamePageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.UserInputRenamePageFrame)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_12.setContentsMargins(10, 25, 10, 5)
        self.RepalceValueRenamePage = QLabel(self.UserInputRenamePageFrame)
        self.RepalceValueRenamePage.setObjectName(u"RepalceValueRenamePage")
        self.RepalceValueRenamePage.setMaximumSize(QSize(16777215, 25))
        self.RepalceValueRenamePage.setFont(font3)
        self.RepalceValueRenamePage.setStyleSheet(u"border: none;\n"
"height: fit-content\n"
"")
        self.RepalceValueRenamePage.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_12.addWidget(self.RepalceValueRenamePage)

        self.RepalceValueInputRenamePage = QLineEdit(self.UserInputRenamePageFrame)
        self.RepalceValueInputRenamePage.setObjectName(u"RepalceValueInputRenamePage")
        self.RepalceValueInputRenamePage.setMaximumSize(QSize(16777215, 30))
        self.RepalceValueInputRenamePage.setFont(font1)
        self.RepalceValueInputRenamePage.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 2px solid white;\n"
"	border-radius: 0px;\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QLineEdit[text]{ color:white; }")
        self.RepalceValueInputRenamePage.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.RepalceValueInputRenamePage)

        self.NewValueRenamePage = QLabel(self.UserInputRenamePageFrame)
        self.NewValueRenamePage.setObjectName(u"NewValueRenamePage")
        self.NewValueRenamePage.setMaximumSize(QSize(16777215, 25))
        self.NewValueRenamePage.setFont(font3)
        self.NewValueRenamePage.setStyleSheet(u"border: none;\n"
"")
        self.NewValueRenamePage.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_12.addWidget(self.NewValueRenamePage)

        self.NewValueInputRenamePage = QLineEdit(self.UserInputRenamePageFrame)
        self.NewValueInputRenamePage.setObjectName(u"NewValueInputRenamePage")
        self.NewValueInputRenamePage.setMaximumSize(QSize(16777215, 30))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.NewValueInputRenamePage.setPalette(palette)
        self.NewValueInputRenamePage.setFont(font1)
        self.NewValueInputRenamePage.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 2px solid white;\n"
"	border-radius: 0px;\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QLineEdit[text]{ color:white; }")
        self.NewValueInputRenamePage.setClearButtonEnabled(True)

        self.verticalLayout_12.addWidget(self.NewValueInputRenamePage)

        self.OutMkdir = QRadioButton(self.UserInputRenamePageFrame)
        self.OutMkdir.setObjectName(u"OutMkdir")
        self.OutMkdir.setFont(font1)
        self.OutMkdir.setStyleSheet(u"background-color: transparent;\n"
"color: white")
        self.OutMkdir.setIconSize(QSize(20, 20))

        self.verticalLayout_12.addWidget(self.OutMkdir)

        self.OutFolderName = QLineEdit(self.UserInputRenamePageFrame)
        self.OutFolderName.setObjectName(u"OutFolderName")
        self.OutFolderName.setEnabled(True)
        self.OutFolderName.setMinimumSize(QSize(0, 0))
        self.OutFolderName.setMaximumSize(QSize(16777215, 0))
        self.OutFolderName.setFont(font1)
        self.OutFolderName.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 2px solid white;\n"
"	border-radius: 0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLineEdit[text]{ color:white; }")

        self.verticalLayout_12.addWidget(self.OutFolderName)

        self.OutputFolderButton = QPushButton(self.UserInputRenamePageFrame)
        self.OutputFolderButton.setObjectName(u"OutputFolderButton")
        self.OutputFolderButton.setMaximumSize(QSize(360, 16777215))
        self.OutputFolderButton.setFont(font6)
        self.OutputFolderButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_12.addWidget(self.OutputFolderButton)

        self.SubmitButtonRenamePage = QPushButton(self.UserInputRenamePageFrame)
        self.SubmitButtonRenamePage.setObjectName(u"SubmitButtonRenamePage")
        self.SubmitButtonRenamePage.setMaximumSize(QSize(360, 16777215))
        self.SubmitButtonRenamePage.setFont(font6)
        self.SubmitButtonRenamePage.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_12.addWidget(self.SubmitButtonRenamePage)

        self.DirDisplayContainerFrame = QFrame(self.UserInputRenamePageFrame)
        self.DirDisplayContainerFrame.setObjectName(u"DirDisplayContainerFrame")
        self.DirDisplayContainerFrame.setStyleSheet(u"border: 0px;\n"
"background-color: transparent")
        self.DirDisplayContainerFrame.setFrameShape(QFrame.StyledPanel)
        self.DirDisplayContainerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.DirDisplayContainerFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DirDisplayContainerLabel = QLabel(self.DirDisplayContainerFrame)
        self.DirDisplayContainerLabel.setObjectName(u"DirDisplayContainerLabel")
        self.DirDisplayContainerLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.DirDisplayContainerLabel.setWordWrap(True)

        self.gridLayout_2.addWidget(self.DirDisplayContainerLabel, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.DirDisplayContainerFrame)


        self.horizontalLayout_10.addWidget(self.UserInputRenamePageFrame)

        self.OutputDisplayContainerSideRenamePage = QFrame(self.ContentHolderRenamePage1)
        self.OutputDisplayContainerSideRenamePage.setObjectName(u"OutputDisplayContainerSideRenamePage")
        self.OutputDisplayContainerSideRenamePage.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: 0px solid white\n"
"}\n"
"")
        self.OutputDisplayContainerSideRenamePage.setFrameShape(QFrame.StyledPanel)
        self.OutputDisplayContainerSideRenamePage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.OutputDisplayContainerSideRenamePage)
        self.verticalLayout_13.setSpacing(1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.OutPutFrameRenamePage = QFrame(self.OutputDisplayContainerSideRenamePage)
        self.OutPutFrameRenamePage.setObjectName(u"OutPutFrameRenamePage")
        self.OutPutFrameRenamePage.setStyleSheet(u"	border: none;\n"
"	border-bottom: 0px solid white;\n"
"	border-radius: 0px;\n"
"	background-color: transparent")
        self.OutPutFrameRenamePage.setFrameShape(QFrame.StyledPanel)
        self.OutPutFrameRenamePage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.OutPutFrameRenamePage)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.OutPutFrameRenamePage)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setStyleSheet(u"border: none;\n"
"border-right: 2px solid white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 8, 0, 0)
        self.ItemsLabelRenamePAge = QLabel(self.frame)
        self.ItemsLabelRenamePAge.setObjectName(u"ItemsLabelRenamePAge")
        self.ItemsLabelRenamePAge.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setPointSize(16)
        self.ItemsLabelRenamePAge.setFont(font7)
        self.ItemsLabelRenamePAge.setStyleSheet(u"border:none;color:white;border-bottom: 2px solid white")
        self.ItemsLabelRenamePAge.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_14.addWidget(self.ItemsLabelRenamePAge)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border:none")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.FolderItemDisplay = QListWidget(self.frame_4)
        self.FolderItemDisplay.setObjectName(u"FolderItemDisplay")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.FolderItemDisplay.setPalette(palette1)
        self.FolderItemDisplay.setFont(font6)
        self.FolderItemDisplay.setStyleSheet(u"QListView{color: white}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: transparent;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}")
        self.FolderItemDisplay.setFrameShape(QFrame.NoFrame)
        self.FolderItemDisplay.setFrameShadow(QFrame.Plain)
        self.FolderItemDisplay.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.FolderItemDisplay.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.FolderItemDisplay.setTabKeyNavigation(True)
        self.FolderItemDisplay.setDragEnabled(False)
        self.FolderItemDisplay.setAlternatingRowColors(False)
        self.FolderItemDisplay.setSelectionMode(QAbstractItemView.NoSelection)
        self.FolderItemDisplay.setTextElideMode(Qt.ElideRight)
        self.FolderItemDisplay.setLayoutMode(QListView.SinglePass)
        self.FolderItemDisplay.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.FolderItemDisplay)


        self.verticalLayout_14.addWidget(self.frame_4)


        self.horizontalLayout_12.addWidget(self.frame)

        self.frame_2 = QFrame(self.OutPutFrameRenamePage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 8, 0, 0)
        self.OutPutRenamePAge = QLabel(self.frame_2)
        self.OutPutRenamePAge.setObjectName(u"OutPutRenamePAge")
        self.OutPutRenamePAge.setMaximumSize(QSize(16777215, 30))
        self.OutPutRenamePAge.setFont(font7)
        self.OutPutRenamePAge.setStyleSheet(u"border:none;color:white;border-bottom: 2px solid white")
        self.OutPutRenamePAge.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_15.addWidget(self.OutPutRenamePAge)

        self.OutPutDisplay = QListWidget(self.frame_2)
        self.OutPutDisplay.setObjectName(u"OutPutDisplay")
        self.OutPutDisplay.setFont(font6)
        self.OutPutDisplay.setAutoFillBackground(True)
        self.OutPutDisplay.setStyleSheet(u"QListView{color: white}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: transparent;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}")
        self.OutPutDisplay.setFrameShape(QFrame.NoFrame)
        self.OutPutDisplay.setFrameShadow(QFrame.Plain)
        self.OutPutDisplay.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OutPutDisplay.setTabKeyNavigation(True)
        self.OutPutDisplay.setDragEnabled(True)
        self.OutPutDisplay.setAlternatingRowColors(False)
        self.OutPutDisplay.setSelectionMode(QAbstractItemView.NoSelection)
        self.OutPutDisplay.setProperty("isWrapping", False)
        self.OutPutDisplay.setLayoutMode(QListView.SinglePass)
        self.OutPutDisplay.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.OutPutDisplay)


        self.horizontalLayout_12.addWidget(self.frame_2)


        self.verticalLayout_13.addWidget(self.OutPutFrameRenamePage)

        self.StatusBarFrameRenamePage = QFrame(self.OutputDisplayContainerSideRenamePage)
        self.StatusBarFrameRenamePage.setObjectName(u"StatusBarFrameRenamePage")
        self.StatusBarFrameRenamePage.setMaximumSize(QSize(16777215, 40))
        self.StatusBarFrameRenamePage.setStyleSheet(u"border: 0px;\n"
"background-color: transparent")
        self.StatusBarFrameRenamePage.setFrameShape(QFrame.StyledPanel)
        self.StatusBarFrameRenamePage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.StatusBarFrameRenamePage)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.StatusBarFrameRenamePage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.LenItemsRenamePage = QLabel(self.frame_3)
        self.LenItemsRenamePage.setObjectName(u"LenItemsRenamePage")
        font8 = QFont()
        font8.setPointSize(9)
        self.LenItemsRenamePage.setFont(font8)
        self.LenItemsRenamePage.setStyleSheet(u"color:white")
        self.LenItemsRenamePage.setAlignment(Qt.AlignCenter)
        self.LenItemsRenamePage.setWordWrap(True)

        self.gridLayout_3.addWidget(self.LenItemsRenamePage, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_3)

        self.StatusLAbelRenamePage = QLabel(self.StatusBarFrameRenamePage)
        self.StatusLAbelRenamePage.setObjectName(u"StatusLAbelRenamePage")
        self.StatusLAbelRenamePage.setFont(font3)
        self.StatusLAbelRenamePage.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.StatusLAbelRenamePage.setAlignment(Qt.AlignCenter)
        self.StatusLAbelRenamePage.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.StatusLAbelRenamePage)


        self.verticalLayout_13.addWidget(self.StatusBarFrameRenamePage)


        self.horizontalLayout_10.addWidget(self.OutputDisplayContainerSideRenamePage)

        self.ContentHolderRenamePage.addWidget(self.ContentHolderRenamePage1)
        self.ContentHolderRenamePage2 = QWidget()
        self.ContentHolderRenamePage2.setObjectName(u"ContentHolderRenamePage2")
        self.horizontalLayout_14 = QHBoxLayout(self.ContentHolderRenamePage2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.ContentHolderRenamePage2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: transparent")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 5, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"border: none;\n"
"height: fit-content;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_2)

        self.OutputListFolder = QListWidget(self.frame_6)
        self.OutputListFolder.setObjectName(u"OutputListFolder")
        self.OutputListFolder.setStyleSheet(u"QListView{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: transparent;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}")

        self.verticalLayout_17.addWidget(self.OutputListFolder)

        self.LenItemsRenamePage_2 = QLabel(self.frame_6)
        self.LenItemsRenamePage_2.setObjectName(u"LenItemsRenamePage_2")
        self.LenItemsRenamePage_2.setFont(font8)
        self.LenItemsRenamePage_2.setStyleSheet(u"color:white")
        self.LenItemsRenamePage_2.setAlignment(Qt.AlignCenter)
        self.LenItemsRenamePage_2.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.LenItemsRenamePage_2)


        self.horizontalLayout_15.addWidget(self.frame_6)

        self.UserInputRenamePageFrameFolder = QFrame(self.frame_5)
        self.UserInputRenamePageFrameFolder.setObjectName(u"UserInputRenamePageFrameFolder")
        self.UserInputRenamePageFrameFolder.setMaximumSize(QSize(450, 16777215))
        self.UserInputRenamePageFrameFolder.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: 0px solid white;\n"
"	color: white\n"
"}\n"
"\n"
"")
        self.UserInputRenamePageFrameFolder.setFrameShape(QFrame.NoFrame)
        self.UserInputRenamePageFrameFolder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.UserInputRenamePageFrameFolder)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_16.setContentsMargins(10, 25, 10, 5)
        self.PathButtonRenamePageFolder = QPushButton(self.UserInputRenamePageFrameFolder)
        self.PathButtonRenamePageFolder.setObjectName(u"PathButtonRenamePageFolder")
        self.PathButtonRenamePageFolder.setMaximumSize(QSize(430, 16777215))
        self.PathButtonRenamePageFolder.setFont(font6)
        self.PathButtonRenamePageFolder.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_16.addWidget(self.PathButtonRenamePageFolder)

        self.RepalceValueRenamePageFolder = QLabel(self.UserInputRenamePageFrameFolder)
        self.RepalceValueRenamePageFolder.setObjectName(u"RepalceValueRenamePageFolder")
        self.RepalceValueRenamePageFolder.setMaximumSize(QSize(16777215, 25))
        self.RepalceValueRenamePageFolder.setFont(font3)
        self.RepalceValueRenamePageFolder.setStyleSheet(u"border: none;\n"
"height: fit-content\n"
"")
        self.RepalceValueRenamePageFolder.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.RepalceValueRenamePageFolder)

        self.RepalceValueInputRenamePageFolder = QLineEdit(self.UserInputRenamePageFrameFolder)
        self.RepalceValueInputRenamePageFolder.setObjectName(u"RepalceValueInputRenamePageFolder")
        self.RepalceValueInputRenamePageFolder.setMaximumSize(QSize(16777215, 30))
        self.RepalceValueInputRenamePageFolder.setFont(font1)
        self.RepalceValueInputRenamePageFolder.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 2px solid white;\n"
"	border-radius: 0px;\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QLineEdit[text]{ color:white; }")
        self.RepalceValueInputRenamePageFolder.setClearButtonEnabled(True)

        self.verticalLayout_16.addWidget(self.RepalceValueInputRenamePageFolder)

        self.NewValueRenamePageFolder = QLabel(self.UserInputRenamePageFrameFolder)
        self.NewValueRenamePageFolder.setObjectName(u"NewValueRenamePageFolder")
        self.NewValueRenamePageFolder.setMaximumSize(QSize(16777215, 25))
        self.NewValueRenamePageFolder.setFont(font3)
        self.NewValueRenamePageFolder.setStyleSheet(u"border: none;\n"
"")
        self.NewValueRenamePageFolder.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.NewValueRenamePageFolder)

        self.NewValueInputRenamePageFolder = QLineEdit(self.UserInputRenamePageFrameFolder)
        self.NewValueInputRenamePageFolder.setObjectName(u"NewValueInputRenamePageFolder")
        self.NewValueInputRenamePageFolder.setMaximumSize(QSize(16777215, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.NewValueInputRenamePageFolder.setPalette(palette2)
        self.NewValueInputRenamePageFolder.setFont(font1)
        self.NewValueInputRenamePageFolder.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 2px solid white;\n"
"	border-radius: 0px;\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QLineEdit[text]{ color:white; }")
        self.NewValueInputRenamePageFolder.setClearButtonEnabled(True)

        self.verticalLayout_16.addWidget(self.NewValueInputRenamePageFolder)

        self.SubmitButtonRenamePageFolder = QPushButton(self.UserInputRenamePageFrameFolder)
        self.SubmitButtonRenamePageFolder.setObjectName(u"SubmitButtonRenamePageFolder")
        self.SubmitButtonRenamePageFolder.setMaximumSize(QSize(430, 16777215))
        self.SubmitButtonRenamePageFolder.setFont(font6)
        self.SubmitButtonRenamePageFolder.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_16.addWidget(self.SubmitButtonRenamePageFolder)

        self.DirDisplayContainerFrameFolder = QFrame(self.UserInputRenamePageFrameFolder)
        self.DirDisplayContainerFrameFolder.setObjectName(u"DirDisplayContainerFrameFolder")
        self.DirDisplayContainerFrameFolder.setStyleSheet(u"border: 0px;\n"
"background-color: transparent")
        self.DirDisplayContainerFrameFolder.setFrameShape(QFrame.StyledPanel)
        self.DirDisplayContainerFrameFolder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.DirDisplayContainerFrameFolder)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.DirDisplayContainerLabelFolder = QLabel(self.DirDisplayContainerFrameFolder)
        self.DirDisplayContainerLabelFolder.setObjectName(u"DirDisplayContainerLabelFolder")
        self.DirDisplayContainerLabelFolder.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.DirDisplayContainerLabelFolder.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.DirDisplayContainerLabelFolder)


        self.verticalLayout_16.addWidget(self.DirDisplayContainerFrameFolder)


        self.horizontalLayout_15.addWidget(self.UserInputRenamePageFrameFolder)


        self.horizontalLayout_14.addWidget(self.frame_5)

        self.ContentHolderRenamePage.addWidget(self.ContentHolderRenamePage2)

        self.verticalLayout_11.addWidget(self.ContentHolderRenamePage)


        self.verticalLayout_9.addWidget(self.BodyFrameRenamePage)

        self.PageHolder.addWidget(self.Rename)
        self.Convert = QWidget()
        self.Convert.setObjectName(u"Convert")
        self.verticalLayout_19 = QVBoxLayout(self.Convert)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_7 = QFrame(self.Convert)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 45))
        self.frame_7.setStyleSheet(u"background-color: transparent")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(475, 45))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.SingleFile = QPushButton(self.frame_7)
        self.SingleFile.setObjectName(u"SingleFile")
        self.SingleFile.setMaximumSize(QSize(150, 16777215))
        self.SingleFile.setFont(font6)
        self.SingleFile.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.horizontalLayout_7.addWidget(self.SingleFile)

        self.MultiFile = QPushButton(self.frame_7)
        self.MultiFile.setObjectName(u"MultiFile")
        self.MultiFile.setMaximumSize(QSize(150, 16777215))
        self.MultiFile.setFont(font6)
        self.MultiFile.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.horizontalLayout_7.addWidget(self.MultiFile)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.frame_7)

        self.ConvertToDocx = QStackedWidget(self.Convert)
        self.ConvertToDocx.setObjectName(u"ConvertToDocx")
        self.ConvertToDocx.setStyleSheet(u"background-color: transparent")
        self.ConvertToDocx.setFrameShape(QFrame.StyledPanel)
        self.ConvertToDocx.setFrameShadow(QFrame.Raised)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_18 = QHBoxLayout(self.page)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: white\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_8)

        self.ConvertToDocx.addWidget(self.page)
        self.ConvertSingle = QWidget()
        self.ConvertSingle.setObjectName(u"ConvertSingle")
        self.horizontalLayout_16 = QHBoxLayout(self.ConvertSingle)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_10 = QFrame(self.ConvertSingle)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(400, 16777215))
        self.frame_10.setStyleSheet(u"background-color: transparent;\n"
"color: white;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setSpacing(24)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Headlabel = QLabel(self.frame_10)
        self.Headlabel.setObjectName(u"Headlabel")
        self.Headlabel.setMaximumSize(QSize(16777215, 80))
        font9 = QFont()
        font9.setPointSize(20)
        self.Headlabel.setFont(font9)
        self.Headlabel.setAlignment(Qt.AlignCenter)
        self.Headlabel.setWordWrap(True)
        self.Headlabel.setMargin(0)

        self.verticalLayout_20.addWidget(self.Headlabel)

        self.comboBoxConvert = QComboBox(self.frame_10)
        self.comboBoxConvert.setObjectName(u"comboBoxConvert")
        self.comboBoxConvert.setMinimumSize(QSize(0, 30))
        self.comboBoxConvert.setFont(font6)
        self.comboBoxConvert.setStyleSheet(u"QComboBox{\n"
"border-radius: 10px;\n"
"border: 2px solid white;\n"
"padding: 8px;\n"
"color: white\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   color: white\n"
"}")
        self.comboBoxConvert.setEditable(False)
        self.comboBoxConvert.setInsertPolicy(QComboBox.InsertAtBottom)

        self.verticalLayout_20.addWidget(self.comboBoxConvert)

        self.OpenFileConvert = QPushButton(self.frame_10)
        self.OpenFileConvert.setObjectName(u"OpenFileConvert")
        self.OpenFileConvert.setFont(font6)
        self.OpenFileConvert.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_20.addWidget(self.OpenFileConvert)

        self.SubmitFileConvert = QPushButton(self.frame_10)
        self.SubmitFileConvert.setObjectName(u"SubmitFileConvert")
        self.SubmitFileConvert.setFont(font6)
        self.SubmitFileConvert.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_20.addWidget(self.SubmitFileConvert)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.dirInfo = QLabel(self.frame_11)
        self.dirInfo.setObjectName(u"dirInfo")
        self.dirInfo.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dirInfo.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.dirInfo.setWordWrap(True)
        self.dirInfo.setMargin(15)

        self.verticalLayout_22.addWidget(self.dirInfo)


        self.verticalLayout_20.addWidget(self.frame_11)


        self.horizontalLayout_16.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.ConvertSingle)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"color: white;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 50, -1, -1)
        self.outputLabelConvertSingle = QLabel(self.frame_8)
        self.outputLabelConvertSingle.setObjectName(u"outputLabelConvertSingle")
        self.outputLabelConvertSingle.setFont(font9)
        self.outputLabelConvertSingle.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.outputLabelConvertSingle)


        self.horizontalLayout_16.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.ConvertToDocx.addWidget(self.ConvertSingle)
        self.ConvertMulti = QWidget()
        self.ConvertMulti.setObjectName(u"ConvertMulti")
        self.horizontalLayout_17 = QHBoxLayout(self.ConvertMulti)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_12 = QFrame(self.ConvertMulti)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(400, 0))
        self.frame_12.setMaximumSize(QSize(400, 16777215))
        self.frame_12.setStyleSheet(u"color: white;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_12)
        self.verticalLayout_23.setSpacing(24)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 80))
        self.label_6.setFont(font9)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label_6)

        self.comboBoxMultiFile = QComboBox(self.frame_12)
        self.comboBoxMultiFile.setObjectName(u"comboBoxMultiFile")
        self.comboBoxMultiFile.setMinimumSize(QSize(0, 30))
        self.comboBoxMultiFile.setMaximumSize(QSize(16777215, 16777215))
        self.comboBoxMultiFile.setFont(font6)
        self.comboBoxMultiFile.setStyleSheet(u"QComboBox{\n"
"border-radius: 10px;\n"
"border: 2px solid white;\n"
"padding: 8px;\n"
"color: white\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"   color: white\n"
"}")

        self.verticalLayout_23.addWidget(self.comboBoxMultiFile)

        self.OpenFolderConvert = QPushButton(self.frame_12)
        self.OpenFolderConvert.setObjectName(u"OpenFolderConvert")
        self.OpenFolderConvert.setFont(font6)
        self.OpenFolderConvert.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_23.addWidget(self.OpenFolderConvert)

        self.SubmitMultiFile = QPushButton(self.frame_12)
        self.SubmitMultiFile.setObjectName(u"SubmitMultiFile")
        self.SubmitMultiFile.setFont(font6)
        self.SubmitMultiFile.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_23.addWidget(self.SubmitMultiFile)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_14)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.dirInfoMulti = QLabel(self.frame_14)
        self.dirInfoMulti.setObjectName(u"dirInfoMulti")
        self.dirInfoMulti.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.dirInfoMulti.setMargin(15)

        self.verticalLayout_24.addWidget(self.dirInfoMulti)


        self.verticalLayout_23.addWidget(self.frame_14)


        self.horizontalLayout_17.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.ConvertMulti)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"color: white;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font9)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_9)

        self.outPutConvertMultiFile = QListWidget(self.frame_13)
        self.outPutConvertMultiFile.setObjectName(u"outPutConvertMultiFile")
        self.outPutConvertMultiFile.setFont(font6)
        self.outPutConvertMultiFile.setStyleSheet(u"QListView{color: white;border:none; border-left: 2px solid white}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: none;\n"
"}\n"
"\n"
"QListView::item:alternate {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: transparent;\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(87, 0, 144);\n"
"	border: none\n"
"}")

        self.verticalLayout_25.addWidget(self.outPutConvertMultiFile)


        self.horizontalLayout_17.addWidget(self.frame_13)

        self.ConvertToDocx.addWidget(self.ConvertMulti)

        self.verticalLayout_19.addWidget(self.ConvertToDocx)

        self.PageHolder.addWidget(self.Convert)
        self.Upload = QWidget()
        self.Upload.setObjectName(u"Upload")
        self.horizontalLayout_8 = QHBoxLayout(self.Upload)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.Upload)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: white\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.PageHolder.addWidget(self.Upload)
        self.EditDocx = QWidget()
        self.EditDocx.setObjectName(u"EditDocx")
        self.verticalLayout_27 = QVBoxLayout(self.EditDocx)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_15 = QFrame(self.EditDocx)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_15)
        self.verticalLayout_28.setSpacing(10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 45))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_22.setSpacing(36)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(600, 16777215))
        font10 = QFont()
        font10.setPointSize(26)
        self.label_5.setFont(font10)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent")

        self.horizontalLayout_22.addWidget(self.label_5)

        self.EditDocContent = QPushButton(self.frame_16)
        self.EditDocContent.setObjectName(u"EditDocContent")
        self.EditDocContent.setMaximumSize(QSize(220, 16777215))
        self.EditDocContent.setFont(font6)
        self.EditDocContent.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.horizontalLayout_22.addWidget(self.EditDocContent)

        self.frame_24 = QFrame(self.frame_16)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: transparent\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_24)


        self.verticalLayout_28.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(400, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(400, 0))
        self.frame_19.setStyleSheet(u"background-color: transparent")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_19)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_21)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_20 = QFrame(self.frame_21)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 500))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_20)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 80))
        self.frame_22.setMaximumSize(QSize(16777215, 90))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_22)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(83)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_22)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 40))
        self.label_10.setFont(font9)
        self.label_10.setStyleSheet(u"color:white;\n"
"")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_10)

        self.notNested = QRadioButton(self.frame_22)
        self.notNested.setObjectName(u"notNested")
        self.notNested.setFont(font6)
        self.notNested.setStyleSheet(u"QRadioButton {\n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 20px;\n"
"	height: 20px\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    color: white\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    color: gray;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"   color: yellow\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    color: red\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"   color: pink\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.notNested)

        self.isNested = QRadioButton(self.frame_22)
        self.isNested.setObjectName(u"isNested")
        self.isNested.setFont(font6)
        self.isNested.setStyleSheet(u"QRadioButton {\n"
"	padding: 10px;\n"
"color:white\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"	width: 20px;\n"
"	height: 20px\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    color: white\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    color: gray;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"   color: yellow\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    color: red\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"   color: pink\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.isNested)


        self.verticalLayout_31.addWidget(self.frame_22)

        self.opendirEdit = QPushButton(self.frame_20)
        self.opendirEdit.setObjectName(u"opendirEdit")
        self.opendirEdit.setEnabled(False)
        self.opendirEdit.setFont(font6)
        self.opendirEdit.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_31.addWidget(self.opendirEdit)

        self.addImage = QPushButton(self.frame_20)
        self.addImage.setObjectName(u"addImage")
        self.addImage.setFont(font6)
        self.addImage.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_31.addWidget(self.addImage)

        self.ToggleDoc = QPushButton(self.frame_20)
        self.ToggleDoc.setObjectName(u"ToggleDoc")
        self.ToggleDoc.setFont(font6)
        self.ToggleDoc.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: white;\n"
"	color: black\n"
"}")

        self.verticalLayout_31.addWidget(self.ToggleDoc)


        self.verticalLayout_32.addWidget(self.frame_20)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_25)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(self.frame_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setMargin(7)

        self.gridLayout_4.addWidget(self.label_13, 2, 2, 1, 1)

        self.MarginEdit = QSlider(self.frame_25)
        self.MarginEdit.setObjectName(u"MarginEdit")
        self.MarginEdit.setMaximum(700)
        self.MarginEdit.setValue(500)
        self.MarginEdit.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.MarginEdit, 3, 0, 1, 3)

        self.XAxisPos = QDial(self.frame_25)
        self.XAxisPos.setObjectName(u"XAxisPos")
        self.XAxisPos.setMaximumSize(QSize(16777215, 50))
        self.XAxisPos.setMinimum(-99)
        self.XAxisPos.setPageStep(1)
        self.XAxisPos.setSliderPosition(0)
        self.XAxisPos.setOrientation(Qt.Horizontal)
        self.XAxisPos.setInvertedAppearance(True)
        self.XAxisPos.setWrapping(True)
        self.XAxisPos.setNotchTarget(3.700000000000000)

        self.gridLayout_4.addWidget(self.XAxisPos, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setMargin(7)

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.ScaleImg = QDial(self.frame_25)
        self.ScaleImg.setObjectName(u"ScaleImg")
        self.ScaleImg.setMaximumSize(QSize(16777215, 50))
        self.ScaleImg.setMinimum(0)
        self.ScaleImg.setMaximum(100)
        self.ScaleImg.setWrapping(True)

        self.gridLayout_4.addWidget(self.ScaleImg, 0, 2, 1, 1)

        self.label_12 = QLabel(self.frame_25)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setMargin(7)

        self.gridLayout_4.addWidget(self.label_12, 2, 1, 1, 1)

        self.YAxisPos = QDial(self.frame_25)
        self.YAxisPos.setObjectName(u"YAxisPos")
        self.YAxisPos.setMaximumSize(QSize(9999999, 50))
        self.YAxisPos.setMinimum(-99)
        self.YAxisPos.setPageStep(1)
        self.YAxisPos.setInvertedAppearance(True)
        self.YAxisPos.setWrapping(True)
        self.YAxisPos.setNotchTarget(0.699999999999999)
        self.YAxisPos.setNotchesVisible(False)

        self.gridLayout_4.addWidget(self.YAxisPos, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_25)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 4, 0, 1, 3)


        self.horizontalLayout_23.addWidget(self.frame_25, 0, Qt.AlignTop)


        self.verticalLayout_32.addWidget(self.frame_23)


        self.verticalLayout_30.addWidget(self.frame_21)


        self.horizontalLayout_21.addWidget(self.frame_19)

        self.tabWidget = QTabWidget(self.frame_18)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
""
                        "QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-top-color:red; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* make use of negative margins for overlapping tabs */\n"
"QTabBar::tab:selected {\n"
"    /* expand/overlap to the left and right by 4px */\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; /* if there is only one tab, we don't want overlapping margins */\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.Docpreview = QWidget()
        self.Docpreview.setObjectName(u"Docpreview")
        self.horizontalLayout_20 = QHBoxLayout(self.Docpreview)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.Docpreview)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMaximumSize(QSize(700, 2000))
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QFrame.Raised)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.Dense7Pattern)
        self.graphicsView.setBackgroundBrush(brush5)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setSceneRect(QRectF(0, 0, 0, 0))
        self.graphicsView.setRenderHints(QPainter.Antialiasing|QPainter.SmoothPixmapTransform|QPainter.TextAntialiasing)
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.graphicsView.setResizeAnchor(QGraphicsView.NoAnchor)
        self.graphicsView.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)
        self.graphicsView.setRubberBandSelectionMode(Qt.ContainsItemShape)

        self.horizontalLayout_20.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.Docpreview, "")
        self.OuPut = QWidget()
        self.OuPut.setObjectName(u"OuPut")
        self.horizontalLayout_19 = QHBoxLayout(self.OuPut)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.listOuputWidgetEdit = QListWidget(self.OuPut)
        self.listOuputWidgetEdit.setObjectName(u"listOuputWidgetEdit")

        self.horizontalLayout_19.addWidget(self.listOuputWidgetEdit)

        self.tabWidget.addTab(self.OuPut, "")
        self.RichText = QWidget()
        self.RichText.setObjectName(u"RichText")
        self.horizontalLayout_24 = QHBoxLayout(self.RichText)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.textBrowser = QTextBrowser(self.RichText)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_24.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.RichText, "")

        self.horizontalLayout_21.addWidget(self.tabWidget)


        self.horizontalLayout_9.addWidget(self.frame_18)


        self.verticalLayout_28.addWidget(self.frame_17)


        self.verticalLayout_27.addWidget(self.frame_15)

        self.PageHolder.addWidget(self.EditDocx)
        self.ReplaceText = QWidget()
        self.ReplaceText.setObjectName(u"ReplaceText")
        self.verticalLayout_26 = QVBoxLayout(self.ReplaceText)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_7 = QLabel(self.ReplaceText)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_7)

        self.PageHolder.addWidget(self.ReplaceText)

        self.verticalLayout_5.addWidget(self.PageHolder)


        self.horizontalLayout.addWidget(self.Content_right)


        self.verticalLayout.addWidget(self.MainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MenuButton.setDefault(False)
        self.PageHolder.setCurrentIndex(4)
        self.ContentHolderRenamePage.setCurrentIndex(0)
        self.ConvertToDocx.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MenuButton.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.PageInfo.setText(QCoreApplication.translate("MainWindow", u"Page Info", None))
        self.WindoName.setText(QCoreApplication.translate("MainWindow", u"Accreditation Engine", None))
        self.MainInfo.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.Minimize.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Minimize</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimize.setText("")
#if QT_CONFIG(tooltip)
        self.Maximize.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Maximize</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximize.setText("")
#if QT_CONFIG(tooltip)
        self.Exit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Exit</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Exit.setText("")
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.RenameButton.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.EditDocButton.setText(QCoreApplication.translate("MainWindow", u"Edit Docx", None))
        self.UploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.ConvertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.Replace.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.RenameFilesORFoldersLabel.setText(QCoreApplication.translate("MainWindow", u"Rename Files or Folders", None))
        self.OpenFileFolder.setText(QCoreApplication.translate("MainWindow", u"Select Doument folder", None))
        self.OpenFolderDir.setText(QCoreApplication.translate("MainWindow", u"Select Folder containing Target Folders", None))
        self.OpenFolderHolder.setText(QCoreApplication.translate("MainWindow", u"Rename Folders", None))
        self.RepalceValueRenamePage.setText(QCoreApplication.translate("MainWindow", u"Replace Value", None))
        self.RepalceValueInputRenamePage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here...", None))
        self.NewValueRenamePage.setText(QCoreApplication.translate("MainWindow", u"New Value", None))
        self.NewValueInputRenamePage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here...", None))
        self.OutMkdir.setText(QCoreApplication.translate("MainWindow", u"Create Output folder?", None))
        self.OutFolderName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Folder Name", None))
        self.OutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select the output path", None))
        self.SubmitButtonRenamePage.setText(QCoreApplication.translate("MainWindow", u"SUbmit", None))
        self.DirDisplayContainerLabel.setText("")
        self.ItemsLabelRenamePAge.setText(QCoreApplication.translate("MainWindow", u"Items", None))
        self.OutPutRenamePAge.setText(QCoreApplication.translate("MainWindow", u"OutPut", None))
        self.LenItemsRenamePage.setText(QCoreApplication.translate("MainWindow", u"0 Items", None))
        self.StatusLAbelRenamePage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.LenItemsRenamePage_2.setText(QCoreApplication.translate("MainWindow", u"0 Items", None))
        self.PathButtonRenamePageFolder.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.RepalceValueRenamePageFolder.setText(QCoreApplication.translate("MainWindow", u"Replace Value", None))
        self.RepalceValueInputRenamePageFolder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here...", None))
        self.NewValueRenamePageFolder.setText(QCoreApplication.translate("MainWindow", u"New Value", None))
        self.NewValueInputRenamePageFolder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here...", None))
        self.SubmitButtonRenamePageFolder.setText(QCoreApplication.translate("MainWindow", u"SUbmit", None))
        self.DirDisplayContainerLabelFolder.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Convert To Docx", None))
        self.SingleFile.setText(QCoreApplication.translate("MainWindow", u"Single File", None))
        self.MultiFile.setText(QCoreApplication.translate("MainWindow", u"Multi File", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Convert Fast and Quick", None))
        self.Headlabel.setText(QCoreApplication.translate("MainWindow", u"Select the format to be changed", None))
        self.comboBoxConvert.setCurrentText("")
        self.OpenFileConvert.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.SubmitFileConvert.setText(QCoreApplication.translate("MainWindow", u"Convert to docx", None))
        self.dirInfo.setText(QCoreApplication.translate("MainWindow", u"No file selected", None))
        self.outputLabelConvertSingle.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select the format to be changed", None))
        self.OpenFolderConvert.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.SubmitMultiFile.setText(QCoreApplication.translate("MainWindow", u"convert to docx", None))
        self.dirInfoMulti.setText(QCoreApplication.translate("MainWindow", u"No directory selected", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Edit Multiple docx at once", None))
        self.EditDocContent.setText(QCoreApplication.translate("MainWindow", u"Edit Doc Contents", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nested directory or not?", None))
        self.notNested.setText(QCoreApplication.translate("MainWindow", u"Not Nested", None))
        self.isNested.setText(QCoreApplication.translate("MainWindow", u"Nested", None))
        self.opendirEdit.setText(QCoreApplication.translate("MainWindow", u"Open directory", None))
        self.addImage.setText(QCoreApplication.translate("MainWindow", u"Add LetterHead", None))
        self.ToggleDoc.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Image Size", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Image Y axis", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Image X axis", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Edit Margins", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Docpreview), QCoreApplication.translate("MainWindow", u"Document Preview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OuPut), QCoreApplication.translate("MainWindow", u"Out Put: Status", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RichText), QCoreApplication.translate("MainWindow", u"Rich text", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
    # retranslateUi

