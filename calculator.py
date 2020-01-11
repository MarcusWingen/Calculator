import operator
class Calculator(object):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    operators = "()*/+-"

    def solve_part(self, arr):  # sample input: ['13', '*', '4']
        """solve one part of the equation, like brackets."""
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

    def evaluate(self, string):
        """handle string input with brackets and return result."""
        brackets = []
        # handle brackets; Note: does not work for multi-brackets
        while "(" in string:
            bracket = string[string.find("("):string.find(")")+1]
            brackets.append(bracket)
            string = string[:string.find("(")] + "bracket" + string[string.find(")")+1:]

        for i, bracket in enumerate(brackets):
            brackets[i] = bracket.lstrip("(").rstrip(")").split()
        for i, b in enumerate(brackets):
            brackets[i] = self.solve_part(b)
        while "bracket" in string:
            string = string.replace("bracket", str(brackets[0]), 1)
            brackets.remove(brackets[0])

        # when all brackets are solved:
        rest = string.split()
        result = self.solve_part(rest)

        return result
