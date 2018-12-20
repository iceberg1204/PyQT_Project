import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QRadioButton, QInputDialog
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import pyqtgraph as pg
import numpy as np


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Графики функций'
        self.setWindowTitle(self.title)
        self.setGeometry(700, 250, 400, 400)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setMouseTracking(True)
        self.show()


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
        self.new = NewWindow()
        self.new.show()


class NewWindow(QWidget):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.setWindowName('График')
        self.setGeometry(700, 250, 600, 600)

        self.input_f = QPushButton(self)
        self.input_f.move(40, 40)

        self.view = pg.PlotWidget()
        self.curve = self.view.plot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
