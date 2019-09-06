import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QSpinBox
from PyQt5.QtGui import QIcon


class Rus(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Русский')
        self.vbox = QVBoxLayout()
        self.chekbox_tema1 = QCheckBox('Тема1')
        self.chekbox_tema2 = QCheckBox('Тема2')
        self.chekbox_tema3 = QCheckBox('Тема3')
        self.chekbox_tema4 = QCheckBox('Тема4')
        self.spin = QSpinBox()
        self.but_rus_open = QPushButton('Открыть')
        self.vbox.addWidget(self.chekbox_tema1)
        self.vbox.addWidget(self.chekbox_tema2)
        self.vbox.addWidget(self.chekbox_tema3)
        self.vbox.addWidget(self.chekbox_tema4)
        self.vbox.addWidget(self.spin)
        self.vbox.addWidget(self.but_rus_open)

        self.setLayout(self.vbox)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())