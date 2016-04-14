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
        board = [[None] * 8 for i in range(8)]

        board[3][3] = queen("Black")
        testQueen = board[3][3]

        self.assertEqual(True, testQueen.pohyb((3, 3), (3, 4), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (3, 2), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (5, 3), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (2, 4), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (2, 2), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (2, 4), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (5, 1), board))
        self.assertEqual(True, testQueen.pohyb((3, 3), (5, 5), board))

        self.assertEqual(False, testQueen.pohyb((3, 3), (0, 1), board))

        board[4][4] = queen("Black")
        self.assertEqual(True, testQueen.pohyb((3, 3), (4, 4), board))
        self.assertEqual(False, testQueen.pohyb((3, 3), (5, 5), board))


if __name__ == '__main__':
    unittest.main()
