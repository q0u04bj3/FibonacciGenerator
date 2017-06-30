import unittest
from Fib import fib

class FibonacciTest(unittest.TestCase):
    
    def test_fid(self):
        c=fib()
        self.assertEqual(c.next(), 1)
        self.assertEqual(c.next(), 2)
        self.assertEqual(c.next(), 3)
        self.assertEqual(c.next(), 5)
        self.assertEqual(c.next(), 8)

if __name__ == '__main__':
    unittest.main()