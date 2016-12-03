import unittest
import greeter

class TestGreeter(unittest.TestCase):

    def test_name_inserted(self):
        self.assertEqual(greeter.greeter('Gergo'), 'Hello, Gergo!')

    def test_name_not_inserted(self):
        self.assertEqual(greeter.greeter(''), 'Hello, Mr Nobody!')

if __name__ == '__main__':
    unittest.main()
