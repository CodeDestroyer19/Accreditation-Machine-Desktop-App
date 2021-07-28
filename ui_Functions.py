from BackendFunctions.popTest import PopulateDocs
from PySide6 import QtCore
from BackendFunctions.rename import Rename


GLOBAL_STATE = 0


class UIFunctions(object):

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.Menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QtCore.QPropertyAnimation(
                self.ui.Menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
            self.animation.start()

    def maximize(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.ui.centralwidget.setContentsMargins(0, 0, 0, 0)
            self.ui.Maximize.setToolTip('Restore')
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.Maximize.setToolTip('Maximize')

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.MenuButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.Maximize.clicked.connect(lambda: UIFunctions.maximize(self))
        self.ui.Minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.Exit.clicked.connect(lambda: self.close())
        self.ui.OpenFolderDir.clicked.connect(
            lambda: self.FileDiloguePoper(True))
        self.ui.OpenFileFolder.clicked.connect(
            lambda: self.FileDiloguePoper(False))
        self.ui.WindoName.mouseMoveEvent = self.moveWindow
        self.ui.OutputFolderButton.clicked.connect(self.OutputFolder)
        self.ui.OutMkdir.clicked.connect(
            lambda: Rename.toggleMkdirOption(self, 25, True))
        self.ui.OpenFileConvert.clicked.connect(
            lambda: UIFunctions.find(self, False))
        self.ui.OpenFolderConvert.clicked.connect(
            lambda: UIFunctions.find(self, True))
        self.ui.SubmitFileConvert.clicked.connect(
            lambda: Rename.ConvertSingleFileToDoc(self, self.pathToFile, self.docValue))
        self.ui.SubmitMultiFile.clicked.connect(
            lambda: Rename.ConvertMultiFileToDoc(self, self.pathToFile, self.docValue))
        self.ui.ToggleDoc.clicked.connect(
            lambda: self.QtGaphicsElem(self.path))
        self.ui.isNested.clicked.connect(
            lambda: UIFunctions.Nested(self, False))
        self.ui.notNested.clicked.connect(
            lambda: UIFunctions.Nested(self, True))
        self.ui.addImage.clicked.connect(self.AddImageToGraphic)

    def buttonControl(self):
        self.ui.RenameButton.clicked.connect(
            lambda: self.ui.PageHolder.setCurrentIndex(1))
        self.ui.ConvertButton.clicked.connect(
            lambda: self.ui.PageHolder.setCurrentIndex(2))
        self.ui.UploadButton.clicked.connect(
            lambda: self.ui.PageHolder.setCurrentIndex(3))
        self.ui.EditDocButton.clicked.connect(
            lambda: self.ui.PageHolder.setCurrentIndex(4))
        self.ui.Replace.clicked.connect(
            lambda: self.ui.PageHolder.setCurrentIndex(5))
        self.ui.HomeButton.clicked.connect(
            lambda: self.ui.PageHolder.setCurrentIndex(0))
        self.ui.OpenFolderHolder.clicked.connect(
            lambda: self.ui.ContentHolderRenamePage.setCurrentIndex(1))
        self.ui.OpenFolderDir.clicked.connect(
            lambda: self.ui.ContentHolderRenamePage.setCurrentIndex(0))
        self.ui.OpenFileFolder.clicked.connect(
            lambda: self.ui.ContentHolderRenamePage.setCurrentIndex(0))
        self.ui.MultiFile.clicked.connect(
            lambda: self.ui.ConvertToDocx.setCurrentIndex(2))
        self.ui.SingleFile.clicked.connect(
            lambda: self.ui.ConvertToDocx.setCurrentIndex(1))

    def returnStatus():
        return GLOBAL_STATE

    def ComboBoxItems(self):
        items = ['.pdf', '.doc', '.txt']

        self.ui.comboBoxMultiFile.addItems(items)
        self.ui.comboBoxConvert.addItems(items)

    def find(self, isMulti):

        if isMulti == False:
            content = self.ui.comboBoxConvert.currentText()
        else:
            content = self.ui.comboBoxMultiFile.currentText()

        print(content)
        self.OpenFile(content, isMulti)

    def Nested(self, isNested):

        self.ui.opendirEdit.setEnabled(True)

        if isNested == True:
            self.ui.opendirEdit.clicked.connect(
                lambda: self.OpenDir(isNested))
        else:
            self.ui.opendirEdit.clicked.connect(
                lambda: self.OpenDir(isNested))
