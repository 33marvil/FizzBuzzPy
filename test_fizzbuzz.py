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
    #
    # def test_is_(arg):
    #     pass






if __name__ == '__main__':
    unittest.main()
