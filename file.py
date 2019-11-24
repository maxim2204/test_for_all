import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QSpinBox, QMessageBox
from PyQt5.QtGui import QIcon
import xml.etree.ElementTree as ET
import random
import numpy
from fpdf import FPDF
import cgi

class File(QWidget):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        print(self.name)
        self.setWindowTitle(self.name[1:])
        self.vbox = QVBoxLayout()


        self.files = os.listdir(self.name)
        print(self.files)

        self.check = []
        for i in self.files:
            print(i)
            self.nazv = i.split('.')[0]
            self.nazv = QCheckBox(self.nazv)
            self.vbox.addWidget(self.nazv)
            self.check.append(self.nazv)


        self.spin = QSpinBox()
        self.spin.setValue(1)
        self.but_inf_open = QPushButton('Открыть')
        self.but_inf_open.clicked.connect(self.push)
        self.vbox.addWidget(self.spin)
        self.vbox.addWidget(self.but_inf_open)

        self.setLayout(self.vbox)
        self.show()

    def push(self):
        self.checkis = []
        for i in self.check:
            if i.isChecked():
                self.checkis.append(i.text())
        print(self.checkis)
        self.parse()

    def parse(self):
        self.all = []
        if self.checkis != []:
            for i in self.checkis:
                path = self.name + '/' + i + '.xml'
                print(path)
                try:
                    root = ET.parse(path).getroot()
                except:
                    buttonReply = QMessageBox.question(self, '', "xml с ошибками")
                    exit(0)
                    sys.exit
                    os.abort()

                for type_tag in root.findall('qwe'):
                    value = type_tag.get('text')
                    self.all.append(value)

            print(self.all)
            if len(self.all) >= self.spin.value():
                self.x = numpy.random.choice(self.all, size=self.spin.value(), replace=False)
                self.pdf()
                print(self.x)
            else:
                buttonReply = QMessageBox.question(self, '', "Всего {} вопросов".format(len(self.all)))
        else:
            buttonReply = QMessageBox.question(self, '', "Выбранно 0 тем")



    def pdf(self):
        test = ''
        for i in range(self.spin.value()):
            test += '<p>{})  {} </p>'.format(i+1,self.x[i])

        f = open('final.html', 'w')
        f.write('<!DOCTYPE html> <html> <head> <meta charset = "windows-1251"> <title> {} </title> </head> <body> <h1> Удачного теста </h1> {} </body> </html>'.format(self.name, test))
        f.close()
        n = os.path.join(os.getcwd())
        print(n)
        os.system(r'{}\final.html'.format(n))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = File('$физика')
    sys.exit(app.exec_())