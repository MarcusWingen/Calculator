# todo:
# handle absence of whitespaces

import operator
class Calculator(object):

    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    operators = "()*/+-"

    def solve_part(self, arr):  # sample input: ['13', '*', '4']
        """solve one part of the equation, like parentheses."""
        while len(arr) > 1:
            # find first operand that is '*' or '/'
            if "*" in arr or "/" in arr:
                for x in arr:
                    if x == "*" or x == "/":
                        op = arr.index(x)
                        break
            else:  # afterwards handle '+' and '-'
                if "+" in arr or "-" in arr:
                    for x in arr:  # gives '/' or '*' first operand
                        if x == "+" or x == "-":
                            op = arr.index(x)
                            break

            arr[op] = self.ops[arr[op]](float(arr[op - 1]), float(arr[op + 1]))
            arr[op - 1] = None
            arr[op + 1] = None
            arr.remove(None)
            arr.remove(None)
        return float(arr[0])

    def inner_parentheses(self, string):
        """find inner parentheses and return solved contents."""
        start = string.rfind("(")
        end = start + string[start:].find(")")
        par = string[start:end].lstrip("(").rstrip(")")
        #print(f"par: {par}")
        # todo handle whitespaces
        par_list = par.split()  # split into list by " "
        #print(f"par_list: {par_list}")
        result = self.solve_part(par_list)
        # modify string:
        string = string[:start] + str(result) + string[end+1:]
        return string

    def evaluate(self, string):
        """handle string input and return result."""

        while "(" in string:
            string = self.inner_parentheses(string)
        # when all parentheses are solved:
        #print(f"string: {string}")
        rest = string.split()
        #print(f"rest: {rest}")
        result = self.solve_part(rest)

        return result

#tests:
print(Calculator().evaluate("2.2 * (5.5 * 2)"))

print(Calculator().inner_parentheses("2.2 * (5.5 * 2)"))

print(Calculator().evaluate("(10 / 2) + 7"))