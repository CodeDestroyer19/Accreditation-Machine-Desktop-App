import sys
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import mammoth

# ==> SPLASH SCREEN
from ui_SplashScreen import Ui_Splash

# ==> MAIN WINDOW
from ui_MainWindowui import Ui_MainWindow

# ==> ui_Functions
from ui_Functions import UIFunctions
from BackendFunctions.rename import Rename
from BackendFunctions.popTest import PopulateDocs

# ==> GLOBALS
counter = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.uiDefinitions(self)
        UIFunctions.buttonControl(self)
        UIFunctions.ComboBoxItems(self)
        self.ui.XAxisPos.valueChanged.connect(self.moveXaxis)
        self.ui.YAxisPos.valueChanged.connect(self.moveYaxis)
        self.ui.ScaleImg.valueChanged.connect(self.scaleImg)
        self.ui.MarginEdit.valueChanged.connect(self.Margin)

    def Margin(self, value):
        self.line1.setRect(-100, 10, value, self.gH - 50)

    def scaleImg(self, value):
        self.img.setScale(value)
        self.img.setX(value)

    def moveYaxis(self, value):
        self.img.setPos(self.img.pos().x(), value)

    def moveXaxis(self, value):
        self.img.setPos(value, self.img.pos().y())

    def QtGaphicsElem(self, item):
        self.gH = self.ui.graphicsView.height()
        self.gW = self.ui.graphicsView.width()
        self.ui.graphicsView.AdjustIgnored = True
        self.ui.graphicsView.NoDrag = True
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView
        self.pen1 = QPen(Qt.black)
        self.pen1.setWidth(2)
        self.line1 = self.scene.addRect(-100,
                                        10, self.gW-25, self.gH - 50, self.pen1)

        if item:
            self.img = self.scene.addPixmap(item)
            self.img.setFlag(QGraphicsWidget.ItemIsMovable, True)
        else:
            pass

        self.ui.graphicsView.setScene(self.scene)

    def AddImageToGraphic(self):
        self.pathtoImage = QFileDialog.getOpenFileName(
            self, 'Select Your letterHead', 'C:/Users/mikek/Documents/doc23/docs/Docs/AFRI-Umalusi/Case 3/QuickRun')
        self.path = self.pathtoImage[0]
        self.QtGaphicsElem(self.path)

        file = 'C:/Users/mikek/Desktop/She rep course .docx'

        with open(file, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            self.ui.textBrowser.setHtml(result.value)

    def OpenDir(self, isNested):

        if isNested == True:
            self.dir_path_edit = QFileDialog.getExistingDirectory(
                self, "Choose Directory", "C:/Users/mikek/Downloads/Documents")
            self.path_edit = self.dir_path_edit
            PopulateDocs.ParseToplevelDir(self, self.path_edit)
        else:
            self.dir_path_edit = QFileDialog.getExistingDirectory(
                self, "Choose Directory", "C:/Users/mikek/Downloads/Documents")
            self.path_edit = self.dir_path_edit
            PopulateDocs.ParseNestedDir(self, self.path_edit)

    def OutputFolder(self):
        self.outdir_path = QFileDialog.getExistingDirectory(
            self, "Choose Directory", self.path)
        self.outpath = self.outdir_path

        self.ui.DirDisplayContainerLabel.setText(self.ui.DirDisplayContainerLabel.text() + '\n\n'
                                                 'You\'re output folder: ' + self.outpath)
        self.ui.DirDisplayContainerLabel.adjustSize()

    def FileDiloguePoper(self, Multi):

        self.dir_path = QFileDialog.getExistingDirectory(
            self, "Choose Directory", "C:/Users/mikek/Downloads/Documents")
        self.path = self.dir_path
        self.ui.DirDisplayContainerLabel.setText(
            'You have selected: '+self.path)
        self.ui.DirDisplayContainerLabel.adjustSize()
        self.ui.FolderItemDisplay.clear()
        self.ui.OutPutDisplay.clear()
        self.stateType = Multi

        if Multi == False:
            Rename.ItemsBoxFiles(self, self.path)
            self.ui.SubmitButtonRenamePage.clicked.connect(
                lambda: Rename.SumitPath(self, True))
        else:
            Rename.ItemsBoxFolders(self, self.path)
            self.ui.SubmitButtonRenamePage.clicked.connect(
                lambda: Rename.SumitPath(self, False))

    def OpenFile(self, file_type, isMulti):

        if isMulti == False:
            self.file_path = QFileDialog.getOpenFileName(
                self, "Select File", 'C:/Users/mikek/Downloads/Documents', '*'+file_type)
            self.pathToFile = self.file_path[0]
            self.docValue = file_type
            self.ui.dirInfo.setText(self.pathToFile)
        else:
            self.file_path = QFileDialog.getOpenFileNames(
                self, 'Select Files', 'C:/Users/mikek/Downloads/Documents', '*'+file_type)
            self.pathToFile = self.file_path[0]
            print(self.pathToFile)
            self.docValue = file_type
            self.ui.dirInfoMulti.setText(
                len(self.pathToFile).__str__() + ' Files selected')

    def moveWindow(self, event):
        if UIFunctions.returnStatus == 1:
            UIFunctions.maximize(self)

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()

    def progress(self):
        global counter

        self.ui.MainProgressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

        counter += float(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
