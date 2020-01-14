import unittest
import calculator
import random as rd

class TestStingCalc(unittest.TestCase):

    def test_positive(self):
        """test for positive integers"""
        self.assertAlmostEqual(calculator.calc("10 / 2 + 7.2"), eval("10 / 2 + 7.2"))
        self.assertAlmostEqual(calculator.calc("10 / (2 + 3)"), eval("10 / (2 + 3)"))
        self.assertAlmostEqual(calculator.calc("(10 / 2) + 7"), eval("(10 / 2) + 7"))
        self.assertAlmostEqual(calculator.calc("10 / 2 + 7 - -19"), eval("10 / 2 + 7 - -19"))
        self.assertAlmostEqual(calculator.calc("10 / 2 + 700"), eval("10 / 2 + 700"))


        ##### Zero Divisin errory may occur -> ignore
        # random test positive int:
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} ({rnd_num} {rnd_op} {rnd_num}) {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} ({rnd_num} {rnd_op} {rnd_num}) {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} (({rnd_num} {rnd_op} {rnd_num}) {rnd_op} {rnd_num}) {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} (({rnd_num} {rnd_op} {rnd_num}) {rnd_op} {rnd_num}) {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(1, 100)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
                         eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))

        # random test negative int:
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))
        rnd_num = rd.randint(-100, -1)
        rnd_op = rd.choice(["+", "-", "*", "/", "//"])
        self.assertEqual(
            calculator.calc(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"),
            eval(f"{rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num} {rnd_op} {rnd_num}"))


if __name__ == "__main__":
    unittest.main()
