import sys
from PyQt5.QtWidgets import QAction, qApp, QColorDialog, QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QRadioButton, QInputDialog, QLineEdit
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
        # Add tabs.
        self.tabs.addTab(self.tab1, "Построение графика")
        self.tabs.addTab(self.tab2, "Преобразование")
        # Add tabs to widget.
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        # Buttons.
        self.tab1.layout = QVBoxLayout(self)
        self.tab2.layout = QVBoxLayout(self)
        # Create objects in tab1.
        self.func_label = QLabel(self)
        self.func_label.setText('Введите функцию:')
        self.func_label.move(120, 50)
        self.tab1.layout.addWidget(self.func_label)

        self.beginning = QLabel(self)
        self.beginning.setText('y = ')
        self.beginning.move(20, 80)
        self.tab1.layout.addWidget(self.beginning)

        self.func_input = QLineEdit(self)
        self.func_input.move(50, 80)
        self.tab1.layout.addWidget(self.func_input)
        self.f = self.func_input.text()

        self.button = QPushButton('Построить график', self)
        self.button.clicked.connect(self.func)
        self.tab1.layout.addWidget(self.button)


        self.tab1.setLayout(self.tab1.layout)
        # Create objects in tab2.
        self.text = QLabel(self)
        self.text.setText('Здесь Вы можете преобразовать Ваше равенство в функцию вида \'y = функция\'')
        self.text.move(20, 40)
        self.tab2.layout.addWidget(self.text)

        self.text2 = QLabel(self)
        self.text2.setText('Введите равенство:')
        self.text2.move(20, 60)
        self.tab2.layout.addWidget(self.text2)

        self.eq_input = QLineEdit(self)
        self.eq_input.move(20, 80)
        self.tab2.layout.addWidget(self.eq_input)
        self.equal = self.eq_input.text()

        self.remake = QPushButton('Преобразовать', self)
        self.remake.clicked.connect(self.from_eq_to_func)
        self.tab2.layout.addWidget(self.remake)

        self.answer = QLabel(self)
        self.answer.setText('')
        self.answer.move(20, 150)
        self.tab2.layout.addWidget(self.answer)

        self.tab2.setLayout(self.tab2.layout)

        self.show()

    def func(self):
        '''self.fx = sp.sympify(self.f)
        self.absciss = np.linspace(-100, 100, 1000)
        self.ordinate = self.fx.sympy.subs(self.fx.x, self.absciss)'''

        self.gr = Graph()
        self.gr.show()

    def from_eq_to_func(self):
        '''self.equal = self.equal.split(' = ')
        self.equal_after = sp.sympify(self.equal[0]) - sp.sympify(self.equal[1])
        self.remade = sp.solve(self.equal_after, self.equal_after.x)'''

        '''self.ready_func = QLabel(self)
        self.ready_func.setText('y = {}'.format(str(self.remade)))
        self.ready_func.move(20, 180)
        self.tab2.layout.addWidget(self.ready_func)'''

        self.re = Remake()
        self.re.show()


class Remake(QWidget):
    def __init__(self):
        super(Remake, self).__init__()
        self.initUI()

    def initUI(self):
        col = QColor(255, 255, 255)

        # Параметры окна
        self.setWindowTitle('Преобразование')
        self.setGeometry(1000, 200, 450, 300)
        self.setObjectName('Rem')
        self.setStyleSheet("#Rem {background-color: %s;}" % col.name())


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
                          "то я могу помочь тебе! \nОбразец записи: \n"
                          "x^2 - x**2; \n√x - 1) sqrt(x); 2) x**(1/2); \n "
                          )
        self.text.move(20, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())