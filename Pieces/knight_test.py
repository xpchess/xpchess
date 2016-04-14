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
        board = [[None] * 8 for i in range(8)]

        board[3][3] = knight("Black")
        testKnight = board[3][3]

        self.assertEqual(True, testKnight.pohyb((3, 3), (4, 1), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (4, 5), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (5, 2), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (5, 4), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (1, 2), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (1, 4), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (2, 1), board))
        self.assertEqual(True, testKnight.pohyb((3, 3), (2, 5), board))

        self.assertEqual(False, testKnight.pohyb((3, 3), (0, 1), board))

        board[4][1] = knight("Black")
        self.assertEqual(True, testKnight.pohyb((3, 3), (1, 4), board))
        self.assertEqual(False, testKnight.pohyb((3, 3), (2, 3), board))


if __name__ == '__main__':
    unittest.main()
