import unittest
from rook import rook

class rook_test(unittest.TestCase):
    def set_up(self):
        pass
    def test_1(self):
        with self.assertRaises(TypeError):
            x = rook("orange")
        x = rook("White")
        y = rook("Black")
        self.assertEqual(x.color,"White")
        self.assertEqual(y.color,"Black")
        self.assertEqual(str(x),"White rook")
        self.assertEqual(str(y),"Black rook")
        
    def test_move(self):
        board = [[None] * 8 for i in range(8)]

        board[3][3] = rook("Black")
        testRook = board[3][3];

        self.assertEqual(True, testRook.pohyb((3, 3), (3, 4), board))
        self.assertEqual(True, testRook.pohyb((3, 3), (3, 2), board))
        self.assertEqual(True, testRook.pohyb((3, 3), (5, 3), board))
        self.assertEqual(True, testRook.pohyb((3, 3), (1, 3), board))

        self.assertEqual(False, testRook.pohyb((3, 3), (4, 4), board))

        board[3][4] = rook("Black")
        self.assertEqual(True, testRook.pohyb((3, 3), (4, 3), board))
        self.assertEqual(False, testRook.pohyb((3, 3), (5, 3), board))

if __name__ == '__main__':
    unittest.main()
