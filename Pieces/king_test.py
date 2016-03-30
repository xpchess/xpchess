import unittest
from king import king

class king_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = king("orange")
        x = king("White")
        y = king("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White king")
        self.assertEqual(str(y),"Black king")
        
    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
