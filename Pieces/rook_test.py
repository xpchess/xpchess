import unittest
from rook import rook

class rook_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = rook("orange")
        x = rook("White")
        y = rook("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White rook")
        self.assertEqual(str(y),"Black rook")
        
    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
