import unittest
from bishop import bishop

class bishop_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = bishop("orange")
        x = bishop("White")
        y = bishop("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White bishop")
        self.assertEqual(str(y),"Black bishop")
        
    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
