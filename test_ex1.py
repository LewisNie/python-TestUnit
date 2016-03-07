import unittest
from function_examples import fib

class TestFibonacci(unittest.TestCase):

    def test_fib_base(self):
        ''' Check base case for Fibonacci function
        '''
        self.assertEquals(1, fib(2))

    def test_fib_larger(self):
        ''' Check Fibonacci function when you really have to do sums
        '''
        self.assertEquals(8, fib(6))

    def test_fib_invalid(self):
        ''' Check Fibonacci function when argument is not in valid range
        '''
        self.assertIsNone(fib(0), 'On invalid integer argument, return None')

        
if __name__ == '__main__':
    unittest.main()
