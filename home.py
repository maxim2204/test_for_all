import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import os
from file import File

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(150, 150, 300, 220)
        self.setWindowTitle('Tests')
        self.file()
        self.vbox = QVBoxLayout()
        for i in self.files:
            self.i = QPushButton(i)
            self.vbox.addWidget(self.i)
            self.i.clicked.connect(self.push)
        self.setLayout(self.vbox)
        self.show()

    def file(self):
        files = os.listdir()
        self.files = [i for i in files if i[0] == '$']
        print(files)

    def push(self):
        name = self.sender().text()
        self.test = File(str(name))
        """print(self.sender().text())
        self.diri = os.listdir(self.sender().text())
        print(self.diri[0])
        catal = self.sender().text() + "." + self.diri[0]
        print(catal)"""

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())