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

        with self.assertRaises(Exception) as ctx: # rais Exception custum, ctx es una variable
            for index in range(-1, -10, -1): # evaluacion
                fizzbuzz(index)
        self.assertEqual("Negative numbers no accepted" , str(ctx.exception))

    def test_zero_not_multiple(self):
        """Is not zero number determined to be multiple"""
        with self.assertRaises(TypeError):
            fizzbuzz(0)
            #self.asserTrue(fizzbuzz(0))

if __name__ == '__main__':
    unittest.main()
