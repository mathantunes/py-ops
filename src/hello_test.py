from server import hello

import unittest

class TestHello(unittest.TestCase):
    def test_hello(self):
        result = hello()
        self.assertEqual(result, "Hello World!")
        
if __name__ == '__main__':
    unittest.main()