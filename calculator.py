import operator
import locale
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        # timer to scale widgets to window size
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.adjust_sizes)
        self.timer.start(200)

    def show(self, expression):
        """show result of entered expression in lists."""
        locale.setlocale(locale.LC_ALL, '')
        result = self.calc(expression)
        output = f"{result:n}"
        self.in_list.insertItem(0, expression)
        self.out_list.insertItem(0, output)
        self.entry.setText(output)

    def clear_history(self):
        self.in_list.clear()
        self.out_list.clear()

    def calc(self, expression):
        """handle string input and return result."""

        def handle_whitespaces(string):
            """remove all present whitespaces, reduce double-operators
            and separate numbers and operators with spaces.
            """
            signs = "()*/+-"
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
                    if i > 0:  # for i=0 only "-" is math. valid and no sep. req.
                        if string[i + 1].isdigit() and not string[i - 1] in signs[2:]:
                            parts.append(" ")
                    if string[i + 1] in signs[2:]:
                        parts.append(" ")
                if x in signs[2:-1]:  # + * /
                    if string[i + 1].isdigit():
                        parts.append(" ")
                    if string[i + 1] in signs[:2]:  # string[i+1] in signs[4:] or
                        parts.append(" ")
                    if string[i + 1] in signs[4:]:
                        parts.append(" ")
                if x in signs[:2] and string[i + 1] in signs[2:]:
                    parts.append(" ")
            parts.append(string[-1])
            proc_string = "".join(parts)
            # print(proc_string)
            return proc_string

        def solve_part(arr):  # sample input: ['1.5009', '--', '6']
            """solve one part of the equation, like parentheses."""
            ops = {'+': operator.add, '+-': operator.sub, '-+': operator.sub,
                   '-': operator.sub, '--': operator.add,
                   '*': operator.mul, '**': operator.pow,
                   '/': operator.truediv, "//": operator.floordiv}
            # print(f"input: {arr}")
            first_ops = ["*", "/", "//"]  # "**" treated first
            second_ops = ["+", "+-", "-+", "-", "--"]
            if len(arr) > 1 and arr[0] == "-":  # handle negative first number
                arr[1] = str(float(arr[1]) * -1)
                arr.remove("-")
            if len(arr) > 1 and arr[0] == "+":  # handle negative first number
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
                        if x in first_ops:  # find first operand that is '*', '/', or '//'
                            sign = arr.index(x)
                            op_found = True
                            break
                            # at last handle '+' and '-'
                if not op_found:
                    for x in arr:
                        if x in second_ops:
                            sign = arr.index(x)
                            break
                # print(f"to solve{arr}, {arr[sign]}")
                op = arr[sign]
                try:
                    num_1 = float(arr[sign - 1])
                except ValueError:
                    print("Value Error num_1")
                    return -1
                try:
                    num_2 = float(arr[sign + 1])
                except ValueError:
                    print("Value Error num_2")
                    return -1
                try:
                    arr[sign] = ops[op](num_1, num_2)
                    arr[sign - 1] = None
                    arr[sign + 1] = None
                    arr.remove(None)
                    arr.remove(None)
                except ZeroDivisionError:
                    print("zero devision")
                    break
                # print(f" after ops: {arr}, {sign}")
            try:
                result = float(arr[0])
            except TypeError:
                print("Type Error")
                result = arr[0]
            return result

        def inner_parentheses(string):
            """find inner parentheses and return solved contents."""
            start = string.rfind("(")
            end = start + string[start:].find(")")
            par = string[start:end].lstrip("(").rstrip(")")
            par_list = par.split()  # split into list by " "
            result = solve_part(par_list)
            # modify string:
            string = string[:start] + str(result) + string[end + 1:]
            return string

        string = handle_whitespaces(expression)
        while "(" in string:
            string = inner_parentheses(string)
            string = handle_whitespaces(string)
        # when all parentheses are solved:
        result = solve_part(string.split())
        if int(result) == result:
            return int(result)
        return result

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 355)
        MainWindow.setMinimumSize(QtCore.QSize(630, 160))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(10, 10, 500, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.entry.setFont(font)
        self.entry.setDragEnabled(True)
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
        font.setPointSize(12)
        self.in_list.setFont(font)
        self.in_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.in_list.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.in_list.setObjectName("in_list")
        self.out_list = QtWidgets.QListWidget(self.centralwidget)
        self.out_list.setGeometry(QtCore.QRect(260, 110, 245, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.out_list.setFont(font)
        self.out_list.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.out_list.setObjectName("out_list")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(520, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.calc_button.clicked.connect(
             lambda: self.show(self.entry.text()))
        self.calc_button.setShortcut("Enter")

        self.clear_button.clicked.connect(
             lambda: self.clear_history())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.calc_button.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Input:"))
        self.label_2.setText(_translate("MainWindow", "Output:"))
        self.clear_button.setText(_translate("MainWindow", "Clear History"))

    def adjust_sizes(self):
        """updates the size of the results lists."""
        main_height = MainWindow.height()
        if self.out_list.height() != main_height - 60:
            self.out_list.setFixedHeight(main_height - 130)
            self.in_list.setFixedHeight(main_height - 130)


    #    self.calc_button.clicked.connect(
   #         lambda: self.show(self.entry.text()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())