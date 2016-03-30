import unittest
from queen import queen

class queen_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = queen("orange")
        x = queen("White")
        y = queen("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White queen")
        self.assertEqual(str(y),"Black queen")
        
    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
