"""
A simple calculator that takes a mathematical expression as input
and returns the result.

Supported operations:
Addition (+)
Subtraction (-)
Multiplication (*)
True Division (/)
Floor Division (//)
Exponentiation (^ or **)
Modulus (%)
Square root (sqrt)*
Natural logarithm (base e) (ln)*
Common logarithm (base 10) (log)*
Factorial (fact)* **
Absolute value (abs)*

Other features:
- Multiple levels of round parentheses are supported ( (...(...)...) ).
- To use e or pi simply type "e" or "pi". (e.g. 2pi = 6,2831...).
- Results are displayed with thousands-separators and commas, specific
  to the users location.
- Click on list items to add them to the entry field.
- Double click on list items to overwrite the entry field.

* these operations are written with the number in parentheses:
sqrt(4) = 2; log(10^2) = 2; fact(sqrt(25)) = 120; abs(-10)**3 == 1000
** fact only supports positive integers.
"""

import operator
import math
import locale
import decimal
from decimal import Decimal
from PyQt5 import QtCore, QtGui, QtWidgets
locale.setlocale(locale.LC_ALL, '')


class CalculatorMainWindow(object):
    """Class for the PyQt5 UI,  and methods to update the UI.
    Also contains function for the calculation.
    """
    def __init__(self):
        super().__init__()
        # timer to scale widgets to window size
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.adjust_sizes)
        self.timer.start(200)

    def show(self, expression):
        """show result of entered expression in lists."""
        result = self.calc(expression)
        if not isinstance(result, str):
            output = f"{result:n}"
        else:
            output = result
        self.in_list.insertItem(0, expression)
        self.out_list.insertItem(0, output)
        self.entry.setText(output)
        self.entry.setFocus()

    def clear_history(self):
        """clear previously computed results."""
        self.in_list.clear()
        self.out_list.clear()
        self.entry.setFocus()

    @staticmethod
    def calc(expression):
        """handle string input and return result."""

        def format_input(string):
            """remove thousands separators from input string."""
            separators = locale.localeconv()
            thousands = separators["thousands_sep"]
            string = string.replace(thousands, "")  # thousand sep only for visuals
            string = string.replace(",", ".")  # handle different commas
            string = string.replace("^", "**")  # convert exponent symbol
            while "e" in string:
                ind_e = string.find("e")
                if string[ind_e-1].isdigit():
                    string = string.replace("e", f"*{math.e}", 1)  # x * convert e
                else:
                    string = string.replace("e", f"{math.e}", 1)  # convert e
            while "pi" in string:
                ind_pi = string.find("pi")
                if string[ind_pi-1].isdigit():
                    string = string.replace("pi", f"*{math.pi}", 1)  # convert x * pi
                else:
                    string = string.replace("pi", f"{math.pi}")  # convert pi
            return string

        def handle_spaces(string):
            """remove all present spaces, reduce double-operators
            and separate numbers and operators with spaces.
            """
            signs = "()*/%+-"
            string = string.replace(" ", "")  # first remove all spaces
            string = string.replace("+-", "-").replace("--", "+") \
                .replace("++", "+").replace("-+", "-") \
                .replace("*+", "*").replace("/+", "/")
            parts = []
            for i, x in enumerate(string[:-1]):  # place " " for clean separation
                parts.append(x)
                if x.isdigit() and string[i + 1] in signs[2:]:
                    parts.append(" ")
                if x == "-":  # +-*/
                    if i > 0:  # for i=0 only "-" and "+" are valid and no sep. req.
                        if string[i + 1].isdigit() and not string[i - 1] in signs[2:]:
                            parts.append(" ")
                    if string[i + 1] in signs[2:]:
                        parts.append(" ")
                if x in signs[2:-1]:  # + * / %
                    if string[i + 1].isdigit():
                        parts.append(" ")
                    if string[i + 1] in signs[:2]:
                        parts.append(" ")
                    if string[i + 1] in signs[5:]:
                        parts.append(" ")
                if x in signs[:2] and string[i + 1] in signs[2:]:
                    parts.append(" ")
            parts.append(string[-1])
            proc_string = "".join(parts)
            # print(proc_string)
            return proc_string

        def solve_part(arr):
            """solve one part of the equation, like parentheses."""
            ops = {'+': operator.add, '+-': operator.sub, '-+': operator.sub,
                   '-': operator.sub, '--': operator.add,
                   '*': operator.mul, '**': operator.pow,
                   '/': operator.truediv, "//": operator.floordiv,
                   "%": operator.mod}
            # print(f"input: {arr}")
            first_ops = ["*", "/", "//", "%"]  # "**" is handled separately
            second_ops = ["+", "+-", "-+", "-", "--"]
            if len(arr) > 1 and arr[0] == "-":  # handle negative first number
                arr[1] = str(Decimal(arr[1]) * -1)
                arr.remove("-")
            if len(arr) > 1 and arr[0] == "+":  # handle unnecessary but valid op
                arr.remove("+")
            while len(arr) > 2:
                op_found = False
                for x in arr:
                    if x == "**":  # first check for pow op
                        sign = arr.index(x)
                        op_found = True
                        break
                if not op_found:
                    for x in arr:
                        if x in first_ops:
                            sign = arr.index(x)
                            op_found = True
                            break
                            # at last handle '+' and '-'
                if not op_found:
                    for x in arr:
                        if x in second_ops:
                            sign = arr.index(x)
                            op_found = True
                            break
                if not op_found:
                    return "Invalid operation"
                # print(f"to solve{arr}, {arr[sign]}")
                op = arr[sign]
                try:
                    num_1 = Decimal(arr[sign - 1])
                except decimal.InvalidOperation:
                    return "Invalid operation"
                try:
                    num_2 = Decimal(arr[sign + 1])
                except decimal.InvalidOperation:
                    return "Invalid operation"
                try:  # calculation
                    if op == "//" or op == "%":  # decimal does not handle // and % of num_1 < 0 correctly
                        arr[sign] = ops[op](float(num_1), float(num_2))
                    else:
                        arr[sign] = ops[op](num_1, num_2)
                    arr[sign - 1] = None
                    arr[sign + 1] = None
                    arr.remove(None)
                    arr.remove(None)
                except ZeroDivisionError:
                    return "Zero Division Error"
                # print(f" after ops: {arr}, {sign}")
            try:
                result = Decimal(arr[0])
            except decimal.InvalidOperation:
                return "Invalid operation"
            return result

        def adv_ops(number, adv_op):
            """solve advanced operations like 'sqrt', 'log' etc."""
            try:
                if adv_op == "sqrt":
                    result = math.sqrt(number)
                elif adv_op == "log":
                    result = math.log10(number)
                elif adv_op == "ln":
                    result = math.log(number)
                elif adv_op == "fact":
                    if number == int(number):
                        result = math.factorial(number)
                    else:
                        return "Invalid operation"
                elif adv_op == "abs":
                    result = abs(number)
                else:
                    result = "Invalid operation"
            except ValueError:
                return "Invalid operation"
            return result

        def inner_parentheses(string):
            """find inner parentheses and return solved contents."""
            start = string.rfind("(")
            end = start + string[start:].find(")")
            par = string[start:end].lstrip("(").rstrip(")")
            par_list = par.split()  # split into list by " "
            result = solve_part(par_list)

            advanced_operators = ("sqrt", "log", "ln", "fact", "abs")

            if not isinstance(result, str):  # if str -> Error
                for adv_op in advanced_operators:
                    if string[:start].endswith(adv_op):
                        result = adv_ops(result, adv_op)
                        if not isinstance(result, str):
                            string = string[:start - len(adv_op)] + str(result) + string[end + 1:]
                            return string
                        else:
                            return "Invalid operation"

                string = string[:start] + str(result) + string[end + 1:]
                return string

            return result

        # steps for the calculation:
        expression = format_input(expression)
        string = handle_spaces(expression)
        while "(" in string:
            string = inner_parentheses(string)
            string = handle_spaces(string)
        # when all parentheses are solved:
        result = solve_part(string.split())
        if not isinstance(result, str):
            if int(result) == result:
                return int(result)
            return result

        return result

    def setup_ui(self, main_window):
        """Initialize user interface."""
        main_window.setObjectName("MainWindow")
        main_window.resize(630, 355)
        main_window.setMinimumSize(QtCore.QSize(630, 160))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(10, 10, 500, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.entry.setFont(font)
        self.entry.setDragEnabled(True)
        self.entry.setAcceptDrops(True)
        self.entry.setObjectName("entry")
        self.calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_button.setGeometry(QtCore.QRect(520, 10, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calc_button.setFont(font)
        self.calc_button.setObjectName("calc_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.in_list = QtWidgets.QListWidget(self.centralwidget)
        self.in_list.setGeometry(QtCore.QRect(10, 110, 245, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.in_list.setFont(font)
        #self.in_list.setLayoutDirection(QtCore.Qt.RightToLeft) # may flip part of expression.
        self.in_list.setAutoScroll(False)
        self.in_list.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.in_list.setObjectName("in_list")
        self.in_list.setAlternatingRowColors(True)
        self.out_list = QtWidgets.QListWidget(self.centralwidget)
        self.out_list.setGeometry(QtCore.QRect(260, 110, 245, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.out_list.setFont(font)
        self.out_list.setAutoScroll(False)
        self.out_list.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.out_list.setObjectName("out_list")
        self.out_list.setAlternatingRowColors(True)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(520, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # Add two shortcuts to calc_button:
        for sequence in ("Enter", "Return",):
            shorcut = QtWidgets.QShortcut(sequence, self.calc_button)
            shorcut.activated.connect(self.calc_button.animateClick)

        self.calc_button.clicked.connect(
            lambda: self.show(self.entry.text()))
        self.clear_button.clicked.connect(
            lambda: self.clear_history())

        # Click events for lists:
        self.in_list.itemClicked.connect(
            lambda: self.in_list_clicked())
        self.out_list.itemClicked.connect(
            lambda: self.out_list_clicked())

        self.in_list.itemDoubleClicked.connect(
            lambda: self.in_list_double_clicked())
        self.out_list.itemDoubleClicked.connect(
            lambda: self.out_list_double_clicked())

    def retranslate_ui(self, main_window):
        """Set title of widgets and window"""
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Input:"))
        self.label_2.setText(_translate("MainWindow", "Output:"))
        self.clear_button.setText(_translate("MainWindow", "Clear History"))

    def in_list_double_clicked(self):
        """Set the entry to the value of the
        clicked item in the in_list.
        """
        clicked_item = self.in_list.currentItem().text()
        self.entry.setText(f"{clicked_item}")
        self.entry.setFocus()

    def out_list_double_clicked(self):
        """Set the entry to the value of the
        clicked item in the out_list.
        """
        clicked_item = self.out_list.currentItem().text()
        self.entry.setText(f"{clicked_item}")
        self.entry.setFocus()

    def in_list_clicked(self):
        """Add the clicked input to the entry field."""
        current_entry = self.entry.text()
        clicked_item = self.in_list.currentItem().text()
        self.entry.setText(current_entry + f"{clicked_item}")
        self.entry.setFocus()

    def out_list_clicked(self):
        """Add the clicked output to the entry field."""
        current_entry = self.entry.text()
        clicked_item = self.out_list.currentItem().text()
        self.entry.setText(current_entry + f"{clicked_item}")
        self.entry.setFocus()

    def adjust_sizes(self):
        """update size and position of the window elements."""
        main_height = MainWindow.height()
        main_width = MainWindow.width()
        if self.out_list.height() != main_height - 60 or\
                self.entry.width() != main_width - 130:     # only resize if necessary

            self.entry.setFixedWidth(main_width - 130)
            self.calc_button.setGeometry(QtCore.QRect(main_width - 110, 10, 101, 61))
            self.clear_button.setGeometry(QtCore.QRect(main_width - 110, 110, 101, 41))
            in_list_x = self.in_list.x()
            list_width = (main_width - 130) // 2
            list_height = main_height - 130
            out_list_x = in_list_x + list_width + 5
            self.in_list.setGeometry(QtCore.QRect(10, 110, list_width, list_height))
            self.out_list.setGeometry(QtCore.QRect(out_list_x, 110, list_width, list_height))
            label_x = in_list_x + list_width // 2 - self.label.width() // 2
            label_2x = out_list_x + list_width // 2 - self.label_2.width() // 2
            self.label.setGeometry(QtCore.QRect(label_x, 80, 51, 21))
            self.label_2.setGeometry(QtCore.QRect(label_2x, 80, 51, 21))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CalculatorMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
