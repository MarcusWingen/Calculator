import unittest
from decimal import Decimal
import calculator


class TestCalculator(unittest.TestCase):
    """Tests for the calculator."""

    def test_simple(self):
        """Test for basic operations."""
        calc_function = calculator.CalculatorMainWindow.calc
        self.assertEqual(calc_function("10+2"), 12)
        self.assertEqual(calc_function("10--2"), 12)
        self.assertEqual(calc_function("10++2"), 12)
        self.assertEqual(calc_function("10*2"), 20)
        self.assertEqual(calc_function("10/2"), 5)
        self.assertEqual(calc_function("9//2"), 4)
        self.assertEqual(calc_function("10/-2"), -5)
        self.assertEqual(calc_function("10+-2"), 8)
        self.assertEqual(calc_function("10-+2"), 8)
        self.assertEqual(calc_function("-10--2"), -8)
        self.assertEqual(calc_function("-10/2"), -5)
        self.assertEqual(calc_function("-10*-2"), 20)
        self.assertEqual(calc_function("-9//2"), -5)
        self.assertEqual(calc_function("-9//2"), -5)
        self.assertEqual(calc_function("10%2"), 0)
        self.assertEqual(calc_function("-10%3"), 2)
        self.assertEqual(calc_function("0*13"), 0)
        self.assertEqual(calc_function("13**0"), 1)
        self.assertEqual(calc_function("2^3"), 8)
        self.assertEqual(calc_function("5---3"), 2)
        self.assertEqual(calc_function("5----3"), 8)
        self.assertEqual(calc_function("1/10**100"), Decimal("1e-100"))
        self.assertEqual(calc_function("10**100"), 10**100)

    def test_complex(self):
        """Test for more complex operations."""
        calc_function = calculator.CalculatorMainWindow.calc
        self.assertEqual(calc_function("10,2 + 2 / (12 / -3)"), Decimal("9.7"))
        self.assertEqual(calc_function("10,2 + 2**3 / (12 / -3)"), Decimal("8.2"))
        self.assertEqual(calc_function("10**3 + -2**3 / (2 / 3)"), 988)
        self.assertEqual(calc_function("(10**3 + 2**3) / (6 / 3)"), 504)
        self.assertEqual(calc_function("((10**3 + 2**3) / (6 / 3))/-2"), -252)
        self.assertEqual(calc_function("((10**3 + 2**3) / (6 / 3))/-2+15,13"), Decimal("-236.87"))
        self.assertEqual(calc_function("((10**3 + 2**3) / (6 / 3))/-2+(15,13*-2)"), Decimal("-282.26"))
        self.assertEqual(calc_function("(100**2-5+(2*2,5))"), 10000)

    def test_adv_ops(self):
        """Test for sqrt, log, ln functions."""
        calc_function = calculator.CalculatorMainWindow.calc
        self.assertEqual(calc_function("sqrt(4)"), 2)
        self.assertEqual(calc_function("sqrt((4+5)*10+10)"), 10)
        self.assertEqual(calc_function("sqrt(-4*-4)"), 4)
        self.assertEqual(calc_function("sqrt(100**2-5+(2*2,5)+0)"), 100)
        self.assertEqual(calc_function("log(100)"), 2)
        self.assertEqual(calc_function("log(10123)"), Decimal("4.005309236848516"))
        self.assertEqual(calc_function("ln(10123)"), Decimal("9.222565341598752"))
        self.assertEqual(calc_function("log(101,23)"), Decimal("2.005309236848517"))
        self.assertEqual(calc_function("ln(101,23)"), Decimal("4.6173951556106605"))
        self.assertEqual(calc_function("ln(e)"), 1)
        self.assertEqual(calc_function("fact(5)"), 120)
        self.assertEqual(calc_function("fact(0)"), 1)
        self.assertEqual(calc_function("ln(4+9*2)"), Decimal("3.091042453358316"))


    def test_special_values(self):
        """Test pi and e."""
        calc_function = calculator.CalculatorMainWindow.calc
        self.assertEqual(calc_function("2pi"), Decimal("6.283185307179586"))
        self.assertEqual(calc_function("2e"), Decimal("5.436563656918090"))
        self.assertAlmostEqual(calc_function("2e*(3+2)"), Decimal("27.182818284590450"))
        self.assertAlmostEqual(calc_function("e*pi"), Decimal("8.539734222673566"))

    def test_errors(self):
        """Test error handling."""
        calc_function = calculator.CalculatorMainWindow.calc
        self.assertEqual(calc_function("10/0"), "Zero Division Error")
        self.assertEqual(calc_function("10//0"), "Zero Division Error")
        self.assertEqual(calc_function("10%0"), "Zero Division Error")
        self.assertEqual(calc_function("10///2"), "Invalid operation")
        self.assertEqual(calc_function("10***2"), "Invalid operation")
        self.assertEqual(calc_function("10//*2"), "Invalid operation")
        self.assertEqual(calc_function("10+-*3"), "Invalid operation")
        self.assertEqual(calc_function("10*/3"), "Invalid operation")
        self.assertEqual(calc_function("10+/3"), "Invalid operation")
        self.assertEqual(calc_function("10+^3"), "Invalid operation")
        self.assertEqual(calc_function("10+++3"), "Invalid operation")
        self.assertEqual(calc_function("sqrt(-100)"), "Invalid operation")
        self.assertEqual(calc_function("log(-100)"), "Invalid operation")
        self.assertEqual(calc_function("ln(-10)"), "Invalid operation")
        self.assertEqual(calc_function("fact(-10)"), "Invalid operation")
        self.assertEqual(calc_function("log(0)"), "Invalid operation")
        self.assertEqual(calc_function("ln(0)"), "Invalid operation")
        self.assertEqual(calc_function("fact(1,2)"), "Invalid operation")  # math.fact only supports integers

if __name__ == "__main__":
    unittest.main()
