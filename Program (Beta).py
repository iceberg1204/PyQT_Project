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


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()

    def initUI(self):

        col = QColor(255, 255, 255)

        # Параметры окна
        self.setWindowTitle('Графикс и ко')
        self.setGeometry(700, 250, 400, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
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

        empty = QAction(QIcon('Картинки\Яйцо.png'), 'Пасхальное яйцо', self)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('& ')
        fileMenu.addAction(empty)

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


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)
        # Add tabs
        self.tabs.addTab(self.tab1, "Построение графика")
        self.tabs.addTab(self.tab2, "Преобразование")
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        # buttons
        self.tab1.layout = QVBoxLayout(self)
        self.rb1 = QRadioButton('Линейная функция')
        self.rb2 = QRadioButton('Квадратичная функция')
        self.rb3 = QRadioButton('Функция обратной пропорциональности')
        self.rb4 = QRadioButton('Формула окружности')
        self.rb5 = QRadioButton('Модуль')
        self.rb6 = QRadioButton('Степенная')
        self.rb7 = QRadioButton('Синус')
        self.rb8 = QRadioButton('Косинус')
        self.rb9 = QRadioButton('Тангенс')
        self.rb10 = QRadioButton('Котангенс')
        self.rb11 = QRadioButton('Логарифмическая')
        self.rb12 = QRadioButton('Квадратный корень')
        self.tab1.layout.addWidget(self.rb1)
        self.tab1.layout.addWidget(self.rb2)
        self.tab1.layout.addWidget(self.rb3)
        self.tab1.layout.addWidget(self.rb4)
        self.tab1.layout.addWidget(self.rb5)
        self.tab1.layout.addWidget(self.rb6)
        self.tab1.layout.addWidget(self.rb7)
        self.tab1.layout.addWidget(self.rb8)
        self.tab1.layout.addWidget(self.rb9)
        self.tab1.layout.addWidget(self.rb10)
        self.tab1.layout.addWidget(self.rb11)
        self.tab1.layout.addWidget(self.rb12)
        self.button = QPushButton('Подтвердить')
        self.tab1.layout.addWidget(self.button)
        self.button.clicked.connect(self.func)
        self.tab1.setLayout(self.tab1.layout)
        self.show()

    def func(self):
        self.new = Graph()
        self.new.show()


class Graph(QWidget):
    def __init__(self):
        super(Graph, self).__init__()
        self.initUI()

    def initUI(self):
        col = QColor(255, 255, 255)

        # Параметры окна
        self.setWindowTitle('График')
        self.setGeometry(1000, 200, 450, 300)
        self.setObjectName('Grap')
        self.setStyleSheet("#Grap {background-color: %s;}" % col.name())


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
    ex = App()
    ex.show()
    sys.exit(app.exec())