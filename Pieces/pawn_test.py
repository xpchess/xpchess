import unittest
from pawn import pawn

class pawn_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = pawn("orange")
        x = pawn("White")
        y = pawn("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White pawn")
        self.assertEqual(str(y),"Black pawn")
        
    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
