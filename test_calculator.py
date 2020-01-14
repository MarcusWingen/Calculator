import unittest
import calculator
import random as rd

rnd_num = rd.randint(-50,100)
rnd_op = rd.choice(["+","-","*","/","//","**"])

class TestStingCalc(unittest.TestCase):

    def test_evaluate(self):
        """test 1"""
        self.assertAlmostEqual(calculator.Calculator().evaluate("10 / 2 + 7.2"), eval("10 / 2 + 7.2"))
        self.assertAlmostEqual(calculator.Calculator().evaluate("10 / (2 + 3)"), eval("10 / (2 + 3)"))
        self.assertAlmostEqual(calculator.Calculator().evaluate("(10 / 2) + 7"), eval("(10 / 2) + 7"))
        self.assertAlmostEqual(calculator.Calculator().evaluate("10 / 2 + 7 - -19"), eval("10 / 2 + 7 - -19"))
        self.assertAlmostEqual(calculator.Calculator().evaluate("10 / 2 + 700"), 705)
        # advanced test:
        self.assertEqual(calculator.Calculator().evaluate("(-5 / (2 + 3.33) * 4) - -6"),
                                                    eval("(-5 / (2 + 3.33) * 4) - -6"))
        self.assertEqual(calculator.Calculator().evaluate("(2 / (2 + 3.33) ** 4) - -6"),
                                                     eval("(2 / (2 + 3.33) ** 4) - -6"))
        self.assertEqual(calculator.Calculator().evaluate("(2.02 / (2 + -3.33) * 0.4) * -6"),
                                                    eval("(2.02 / (2 + -3.33) * 0.4) * -6"))

        # random test
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 10)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.Calculator().evaluate(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))




test1=""
test2="2+4"
test3="2+4*5"
test4="(4/2)*(3-1)"

final_test = "(2 / (2 + 3.33) * 4) - -6"

if __name__ == "__main__":
    unittest.main()
