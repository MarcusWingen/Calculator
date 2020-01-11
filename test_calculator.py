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
        self.assertEqual(calculator.Calculator().evaluate("10 / 2 + 7"), 12)
        self.assertEqual(calculator.Calculator().evaluate("10 / (2 + 3)"), 2)
        self.assertEqual(calculator.Calculator().evaluate("(10 / 2) + 7"), 12)
        self.assertEqual(calculator.Calculator().evaluate("10 / 2 + 7 - -19"), 31)
        self.assertEqual(calculator.Calculator().evaluate("10 / 2 + 700"), 705)

if __name__ == "__main__":
    unittest.main()
