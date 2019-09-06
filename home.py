import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from fiz.fiz import Fiz
from mat.mat import Mat
from rus.rus import Rus
from inf.inf import Inf


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Tests')
        self.setWindowIcon(QIcon('web.png'))
        self.vbox = QVBoxLayout()
        self.but_fiz = QPushButton('Физика')
        self.but_mat = QPushButton('Математика')
        self.but_rus = QPushButton('Русский')
        self.but_inf = QPushButton('Информатика')
        self.vbox.addWidget(self.but_fiz)
        self.vbox.addWidget(self.but_mat)
        self.vbox.addWidget(self.but_rus)
        self.vbox.addWidget(self.but_inf)
        self.but_fiz.clicked.connect(self.pushfiz)
        self.but_mat.clicked.connect(self.pushmat)
        self.but_rus.clicked.connect(self.pushrus)
        self.but_inf.clicked.connect(self.pushinf)
        self.setLayout(self.vbox)
        self.show()

    def pushfiz(self):
        self.fiz = Fiz()

    def pushmat(self):
        self.mat = Mat()

    def pushrus(self):
        self.rus = Rus()

    def pushinf(self):
        self.inf = Inf()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())