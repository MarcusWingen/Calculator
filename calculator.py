
import operator
class Calculator(object):

    def handle_whitespaces(self, string):
        """remove all present whitespaces
        and separate numbers and operators with spaces.
        """
        signs = "()*/+-"
        string = string.replace(" ", "")  # first remove all spaces
        string = string.replace("+-", "-").replace("--", "+").\
            replace("++", "+").replace("*+", "*").replace("/+", "/")  # simplify
        parts = []
        for i, x in enumerate(string[:-1]):  # place " " for clean separation
            parts.append(x)
            if x.isdigit() and string[i+1] in signs[2:]:
                parts.append(" ")

            if x == "-":  # +-*/
                if i > 0:  # for i=0 only "-" is math. valid and no sep. req.
                    if string[i+1].isdigit() and not string[i-1] in signs[2:]:
                        parts.append(" ")
                if string[i+1] in signs[2:]:
                    parts.append(" ")
            if x in signs[2:-1]:  # + * /
                if string[i+1].isdigit():
                        parts.append(" ")
                if string[i+1] in signs[:2]: # string[i+1] in signs[4:] or
                    parts.append(" ")
                if string[i+1] in signs[4:]:
                    parts.append(" ")

            if x in signs[:2] and string[i+1] in signs[2:]:
                parts.append(" ")

        parts.append(string[-1])
        proc_string = "".join(parts)
        print(proc_string)
        return proc_string

    def solve_part(self, arr):  # sample input: ['1.5009', '--', '6']
        """solve one part of the equation, like parentheses."""
        ops = {'+': operator.add, '+-': operator.sub, '-+': operator.sub,
               '-': operator.sub, '--': operator.add,
               '*': operator.mul, '**': operator.pow,
               '/': operator.truediv, "//": operator.floordiv}
        print(f"input: {arr}")
        first_ops = ["*", "/", "//"]
        second_ops = ["+", "+-", "-+", "-", "--"]
        if len(arr) > 1 and arr[0] == "-":  # handle negative first number
            arr[1] = str(float(arr[1]) * -1)
            arr.remove("-")
        if len(arr) > 1 and arr[0] == "+":  # handle negative first number
            arr.remove("+")
        print(f"- removed: {arr}")
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
            print(f"to solve{arr}, {arr[sign]}")
            op = arr[sign]
            num_1 = float(arr[sign - 1])
            num_2 = float(arr[sign + 1])
            arr[sign] = ops[op](num_1, num_2)
            print(f" after ops: {arr}, {sign}")
            arr[sign - 1] = None
            arr[sign + 1] = None
            arr.remove(None)
            arr.remove(None)
            #print(f"after cleanup {arr}, {sign}")
        return float(arr[0])

    def inner_parentheses(self, string):
        """find inner parentheses and return solved contents."""
        start = string.rfind("(")
        end = start + string[start:].find(")")
        par = string[start:end].lstrip("(").rstrip(")")
        #print(f"par: {par}")
        par_list = par.split()  # split into list by " "
        #print(f"par_list: {par_list}")
        result = self.solve_part(par_list)
        # modify string:
        string = string[:start] + str(result) + string[end+1:]
        return string

    def evaluate(self, string):
        """handle string input and return result."""
        string = self.handle_whitespaces(string)
        while "(" in string:
            string = self.inner_parentheses(string)
            string = self.handle_whitespaces(string)
        # when all parentheses are solved:
        print(string)
        result = self.solve_part(string.split())

        return result


#tests:
test1 = "(2.02 / (-2 + (-3.33) * 0.4)) * -6"
test2 = "+5 + +5"
test3 = "(2.02 / (-2 + (-3.33) * 0.4)) * -6"
test4 = "2**2 / -2 + 3.33 * 0.4 * 5"
test5 = "(2.02 / -2 + -3.33 ** 1.4) * -6"

#print(Calculator().evaluate(test1))
#print(eval(test1))
print(Calculator().evaluate(test2))
print(eval(test2))
#print(Calculator().evaluate(test2))
#print(eval(test2))
#print(Calculator().evaluate(test2))
#print(eval(test2))

