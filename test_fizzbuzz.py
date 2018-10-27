import unittest

from fizzbuzz import fizzbuzz

class FizzBuzzTestCase(unittest.TestCase):
    """Tests for `fizzbuzz.py`."""

    def test_is_multiple_of_3(self):
        """is multiple of three return Fizz"""
        self.assertTrue(fizzbuzz(27))

    def test_is_multiple_of_5(self):
        """is multiple of five return Buzz"""
        self.assertTrue(fizzbuzz(45))

    def test_is_multiple_both_of_them_3_and_5(self):
        """is multiple both of them 3 and 5 return FizzBuzz"""
        self.assertTrue(fizzbuzz(15))

    def test_is_not_multiple_of_3_and_5(self):
        """is not multiple of 3 and 5 return you value"""
        self.assertTrue(fizzbuzz(7))

    def test_negative_numbers(self):
        """Is a negative number correctly determined not to be multiple"""
        for index in range(-1, -10, -1):
            self.assertFalse(fizzbuzz(index), msg='{} Negative numbers no accepted'.format(index))





if __name__ == '__main__':
    unittest.main()
