import unittest
import calculator

class TestStingCalc(unittest.TestCase):

    # all test methods must start with "test_" or they will not run
    def test_solve_part(self):
        """one test containing five conditions"""
        self.assertEqual(calculator.Calculator().solve_part(["10", "/", "2", "+", "7"]), 12)
        self.assertEqual(calculator.Calculator().solve_part(["10", "+", "2", "+", "7"]), 19)
        self.assertEqual(calculator.Calculator().solve_part(["10", "-", "2", "/", "2"]), 9)
        self.assertEqual(calculator.Calculator().solve_part(["10", "*", "2", "*", "7"]), 140)
        self.assertEqual(calculator.Calculator().solve_part(["10", "-", "2", "+", "7"]), 15)

    def test_evaluate(self):
        """one test containing five conditions"""
        self.assertEqual(calculator.Calculator().evaluate("10 / 2 + 7"), eval("10 / 2 + 7"))
        self.assertEqual(calculator.Calculator().evaluate("10 / (2 + 3)"), eval("10 / (2 + 3)"))
        self.assertEqual(calculator.Calculator().evaluate("(10 / 2) + 7"), eval("(10 / 2) + 7"))
        self.assertEqual(calculator.Calculator().evaluate("10 / 2 + 7 - -19"), eval("10 / 2 + 7 - -19"))
        self.assertEqual(calculator.Calculator().evaluate("10 / 2 + 700"), 705)

test1=""
test2="2+4"
test3="2+4*5"
test4="(4/2)*(3-1)"

final_test = "(2 / (2 + 3.33) * 4) - -6"

if __name__ == "__main__":
    unittest.main()
