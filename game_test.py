import sys
import os
sys.path[0:0] = [os.path.join(sys.path[0], './pieces')]

p = ["bishop","king","knight","pawn","queen","rook",
     "bishop_test","king_test","knight_test","pawn_test","queen_test","rook_test"]
com = ["from {} import {}".format(v,v) for v in p]
for c in com:
    exec(c)

from game import game
import unittest

class game_test(unittest.TestCase):

    def set_up(self):
        pass

    def test_init(self):
        g = game()
        self.assertEqual(str(g.field[0][0]),str(rook("Black")))
        self.assertEqual(str(g.field[0][1]),str(knight("Black")))
        self.assertEqual(str(g.field[0][2]),str(bishop("Black")))
        self.assertEqual(str(g.field[0][3]),str(queen("Black")))
        self.assertEqual(str(g.field[0][4]),str(king("Black")))
        self.assertEqual(str(g.field[0][5]),str(bishop("Black")))
        self.assertEqual(str(g.field[0][6]),str(knight("Black")))
        self.assertEqual(str(g.field[0][7]),str(rook("Black")))
        for x in range(8):
            self.assertEqual(str(g.field[1][x]),str(pawn("Black")))
        for y in range(2,6):
            for x in range(8):
                self.assertEqual(str(g.field[y][x]), str(None))
        for x in range(8):
            self.assertEqual(str(g.field[6][x]),str(pawn("White")))
        self.assertEqual(str(g.field[7][0]),str(rook("White")))
        self.assertEqual(str(g.field[7][1]),str(knight("White")))
        self.assertEqual(str(g.field[7][2]),str(bishop("White")))
        self.assertEqual(str(g.field[7][3]),str(queen("White")))
        self.assertEqual(str(g.field[7][4]),str(king("White")))
        self.assertEqual(str(g.field[7][5]),str(bishop("White")))
        self.assertEqual(str(g.field[7][6]),str(knight("White")))
        self.assertEqual(str(g.field[7][7]),str(rook("White")))

    def test_reset(self):
        g = game()
        for y in range(8):
            for x in range(8):
                g.field[y][x] = -1
        g.set_up()
        for y in range(8):
            for x in range(8):
                self.assertNotEqual(g.field[y][x], -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
