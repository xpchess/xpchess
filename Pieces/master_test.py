import unittest
p = ["bishop","king","knight","pawn","piece","queen","rook"]
com = ["from {}_test import {}_test".format(v,v) for v in p]
for v in com:
    exec(v)



if __name__ == "__main__":
    unittest.main()
