import sys
from PyQt5.QtWidgets import QAction, qApp, QColorDialog, QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QRadioButton, QInputDialog
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore
from qtpy import QtGui
import pyqtgraph as pg
import numpy as np


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.initUI()

    def initUI(self):

        col = QColor(255, 255, 255)

        # Параметры окна
        self.setWindowTitle('Графикс и ко')
        self.setGeometry(650, 200, 400, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setObjectName('MainWidget')
        self.setStyleSheet("#MainWidget {background-color: %s;}" % col.name())
        # self.setStyleSheet("#MainWidget {background-image: url(H:/7EJHMh5lBUU.jpg);}")
        self.old_pos = None

        # Вставка кнопки настройки цвета фона в тулбар
        ChangeAction = QAction(QIcon('Картинки\Палитра.png'), 'Выбор цвета фона', self)
        ChangeAction.setShortcut('Ctrl+I')
        ChangeAction.triggered.connect(self.color)

        # Вставка кнопки справки в тулбар
        Image = QAction(QIcon('Картинки\Справка.png'), 'О программе', self)
        Image.setShortcut('Ctrl+O')
        Image.triggered.connect(self.show_spr)

        # Вставка кнопки выход в тулбар
        exitAction = QAction(QIcon('Картинки\Дверь 4.png'), 'Выход', self)
        exitAction.setShortcut('Ctrl+P')
        exitAction.triggered.connect(qApp.quit)

        # Создание тулбара
        self.change = self.addToolBar('Панель инструментов')
        self.change.setObjectName('ToolBar')
        self.change.addAction(ChangeAction)
        self.change.addAction(Image)
        self.change.addAction(exitAction)

        self.show()

    # Создатим функцию, отвечающую за палитру и изменение цвета фона окна
    def color(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.setStyleSheet("#MainWidget { background-color:  %s;}" % col.name())
            self.change.setStyleSheet("#ToolBar { background-color:  #ffffff;}")

    # Создатим функцию, открывающую окно справки
    def show_spr(self):
        self.spr = AboutPr()
        self.spr.show()

    # Создатим функцию, котороя сможет перемещать окно
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    # Создатим функциюб которая вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)


# Класс нового справочного окна
class AboutPr(QWidget):
    def __init__(self):
        super(AboutPr, self).__init__()
        self.initUI()

    def initUI(self):
        col = QColor(255, 255, 255)

        # Параметры окна
        self.setWindowTitle('Справка')
        self.setGeometry(1058, 227, 450, 300)
        self.setObjectName('About')
        self.setStyleSheet("#About {background-color: %s;}" % col.name())

        # Текст, который будет содержать справка
        self.plot = QLabel(self)
        self.plot.setText("Справка")
        self.plot.move(125, 15)

        self.text = QLabel(self)
        self.text.setText("  Приветствую вас! Если у вас не получается чертить графики, \n"
                          "то я могу помочь тебе!"
                          )
        self.text.move(20, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWin()
    ex.show()
    sys.exit(app.exec())
