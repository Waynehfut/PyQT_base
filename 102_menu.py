# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        exitAct = QAction(QIcon('asset/img/exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        newAct = QAction(QIcon('asset/img/new.png'), '&New', self)
        newAct.setShortcut('Ctrl+N')


        # tool bar
        self.toolbar = self.addToolBar('Tool')
        self.toolbar.addAction(newAct)
        self.toolbar.addAction(exitAct)

        # file menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        newAct.setStatusTip('New file')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import file', self)
        impAct.setShortcut('Ctrl+I')
        impAct.setStatusTip('Import your file')
        impMenu.addAction(impAct)

        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)


        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)

        # view menu
        viewMenu = menubar.addMenu('&View')

        ## view action
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle('Editor')
        self.show()

    def toggleMenu(self, state):
        # should noticed that the statusBar control the menu display or not
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        copyAct = cmenu.addAction("Copy")
        pasteAct = cmenu.addAction("Paste")
        cutAct = cmenu.addAction("Cut")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
