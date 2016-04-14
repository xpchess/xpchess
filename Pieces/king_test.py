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
        board = [[None] * 8 for i in range(8)]

        board[3][3] = king("Black")
        testKing = board[3][3]

        self.assertEqual(True, testKing.pohyb((3, 3), (3, 4), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (3, 2), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (4, 3), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (2, 3), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (2, 2), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (2, 4), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (4, 2), board))
        self.assertEqual(True, testKing.pohyb((3, 3), (4, 4), board))

        self.assertEqual(False, testKing.pohyb((3, 3), (3, 5), board))

        board[4][4] = king("Black")
        self.assertEqual(True, testKing.pohyb((3, 3), (4, 4), board))


if __name__ == '__main__':
    unittest.main()
