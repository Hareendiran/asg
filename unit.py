"""
Simple calculator class and corresponding unit tests.
"""

import unittest

class Calculator:
    """
    A basic calculator class.
    """

    def add(self, x, y):
        """Addition operation."""
        return x + y

    def subtract(self, x, y):
        """Subtraction operation."""
        return x - y

    def multiply(self, x, y):
        """Multiplication operation."""
        return x * y

    def divide(self, x, y):
        """Division operation."""
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

class CalculatorTest(unittest.TestCase):
    """
    Unit tests for the Calculator class.
    """

    def setUp(self):
        """Set up the Calculator instance for testing."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(10, self.calc.add(3, 7), "The addition is wrong")

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()
