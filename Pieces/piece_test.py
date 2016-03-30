import unittest
from piece import piece

class piece_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = piece("orange")
        x = piece("White")
        y = piece("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White piece")
        self.assertEqual(str(y),"Black piece")
        
    def test_pohybu(self):
        pass

if __name__ == '__main__':
    unittest.main()
