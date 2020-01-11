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

    def find_parentheses(self, string):
        """handle parentheses and return list of parentheses and string with placeholders for them."""
        parentheses = []
        # handle parentheses; Note: does not work for multi-parentheses yet
        while "(" in string:
            par = string[string.find("("):string.find(")")+1]
            parentheses.append(par)
            string = string[:string.find("(")] + "parent" + string[string.find(")")+1:]
        par_string = string
        for i, par in enumerate(parentheses):
            parentheses[i] = par.lstrip("(").rstrip(")").split()
        print(parentheses)
        return par_string, parentheses

    def evaluate(self, string):
        """handle string input and return result."""
        par_string, parentheses = self.find_parentheses(string)

        for i, b in enumerate(parentheses):
            print(b)
            parentheses[i] = self.solve_part(b)
        while "parent" in par_string:
            par_string = par_string.replace("parent", str(parentheses[0]), 1)
            parentheses.remove(parentheses[0])

        # when all parentheses are solved:
        rest = par_string.split()
        result = self.solve_part(rest)

        return result

#tests:
print(Calculator().evaluate("2 + 5 - (4 + 2)"))