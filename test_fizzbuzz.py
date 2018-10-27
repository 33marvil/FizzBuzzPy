import unittest

from fizzbuzz import fizzbuzz

class FizzBuzzTestCase(unittest.TestCase):
    """Tests for `fizzbuzz.py`."""

    def test_is_multiple_of_3(self):
        """is multiple of three return Fizz"""
        self.assertTrue(fizzbuzz(27))

    def test_is_multiple_of_5(self):
        """is multiple of five return Buzz"""
        self.assertTrue(fizzbuzz(30))

    def test_is_multiple_both_of_them_3_and_5(self):
        """is multiple both of them 3 and 5 return FizzBuzz"""
        self.assertTrue(fizzbuzz(15))



if __name__ == '__main__':
    unittest.main()
