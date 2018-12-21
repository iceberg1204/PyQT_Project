import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit
import pyqtgraph as pg
import numpy as np
import sympy as sp


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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
        self.remake.resize(self.remake.sizeHint())
        self.resize.move(20, 120)
        self.remake.clicked.connect(self.from_eq_to_func)
        self.tab2.layout.addWidget(self.remake)

        self.answer = QLabel(self)
        self.answer.setText('')
        self.answer.moove(20, 150)
        self.tab2.layout.addWidget(self.answer)

        self.tab2.setLayout(self.tab2.layout)

        self.show()

    def func(self):
        self.fx = sp.sympify(self.f)
        self.absciss = np.linspace(-100, 100, 1000)
        self.ordinate = self.fx.sympy.subs(self.fx.x, self.absciss)

        self.new = NewWindow()
        self.new.show()

    def from_eq_to_func(self):
        self.equal = self.equal.split(' = ')
        self.equal_after = sp.sympify(self.equal[0]) - sp.sympify(self.equal[1])
        self.remade = sp.solve(self.equal_after, self.equal_after.x)

        self.ready_func = QLabel(self)
        self.ready_func.setText('y = {}'.format(str(self.remade)))
        self.ready_func.move(20, 180)
        self.tab2.layout.addWidget(self.ready_func)


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowName('График')
        self.setGeometry(700, 250, 600, 600)

        self.label = QLabel(self)
        self.label.setText('График функции y = {}'.format(str(self.fx)))

        self.plot = pg.PlotWidget()
        self.curve = self.plot.plot(self.absciss, self.ordinate, pen='g')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
