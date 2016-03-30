import unittest
from knight import knight

class knight_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = knight("orange")
        x = knight("White")
        y = knight("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White knight")
        self.assertEqual(str(y),"Black knight")
        
    def test_move(self):
        pass

if __name__ == '__main__':
    unittest.main()
