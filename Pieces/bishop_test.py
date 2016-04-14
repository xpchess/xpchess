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
        board = [[None] * 8 for i in range(8)]

        board[3][3] = bishop("Black")
        testBishop = board[3][3]

        self.assertEqual(True, testBishop.pohyb((3, 3), (2, 2), board))
        self.assertEqual(True, testBishop.pohyb((3, 3), (2, 4), board))
        self.assertEqual(True, testBishop.pohyb((3, 3), (5, 1), board))
        self.assertEqual(True, testBishop.pohyb((3, 3), (5, 5), board))

        self.assertEqual(False, testBishop.pohyb((3, 3), (3, 4), board))

        board[4][4] = bishop("Black")
        self.assertEqual(True, testBishop.pohyb((3, 3), (4, 4), board))
        self.assertEqual(False, testBishop.pohyb((3, 3), (5, 5), board))


if __name__ == '__main__':
    unittest.main()
