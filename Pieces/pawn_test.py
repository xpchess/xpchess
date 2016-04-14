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
        board = [[None] * 8 for i in range(8)]

        board[1][3] = pawn("Black")
        testBlackPawn = board[1][3]

        self.assertEqual(True, testBlackPawn.pohyb((3, 1), (3, 3), board))
        self.assertEqual(True, testBlackPawn.pohyb((3, 1), (3, 2), board))
        self.assertEqual(False, testBlackPawn.pohyb((3, 3), (5, 3), board))
        self.assertEqual(False, testBlackPawn.pohyb((3, 1), (3, 4), board))
        self.assertEqual(False, testBlackPawn.pohyb((3, 1), (3, 0), board))

        board[2][3] = pawn("Black")
        testBlackPawn2 = board[2][3]

        self.assertEqual(True, testBlackPawn2.pohyb((3, 2), (3, 3), board))
        self.assertEqual(False, testBlackPawn2.pohyb((3, 2), (3, 4), board))

        self.assertEqual(False, testBlackPawn.pohyb((3, 1), (3, 3), board))

        board[6][3] = pawn("White")
        testWhitePawn = board[6][3]

        self.assertEqual(True, testWhitePawn.pohyb((3, 6), (3, 5), board))
        self.assertEqual(True, testWhitePawn.pohyb((3, 6), (3, 4), board))
        self.assertEqual(False, testWhitePawn.pohyb((3, 6), (3, 3), board))
        self.assertEqual(False, testWhitePawn.pohyb((3, 6), (4, 6), board))
        self.assertEqual(False, testWhitePawn.pohyb((3, 6), (3, 7), board))

        board[5][3] = pawn("White")
        testWhitePawn2 = board[5][3]

        self.assertEqual(True, testWhitePawn2.pohyb((3, 5), (3, 4), board))
        self.assertEqual(False, testWhitePawn2.pohyb((3, 5), (3, 3), board))

        self.assertEqual(False, testBlackPawn.pohyb((3, 6), (3, 4), board))


if __name__ == '__main__':
    unittest.main()
