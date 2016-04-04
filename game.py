import sys
import os
sys.path[0:0] = [os.path.join(sys.path[0], './pieces')]

p = ["bishop","king","knight","pawn","queen","rook"]
com = ["from {} import {}".format(v,v) for v in p]
for c in com:
    exec(c)
    
class game():
    def __init__(self):
        self.field = []
        for i in range(8):
            self.field.append([None] * 8)
        self.set_up()
        #sluzi na debug
        self.icons = {"White pawn":"♙","White rook":"♖","White knight":"♘",
                      "White bishop":"♗","White queen":"♕","White king":"♔",
                      "Black pawn":"♟","Black rook":"♜","Black knight":"♞",
                      "Black bishop":"♝","Black queen":"♛","Black king":"♚",
                      "None":" "}
        
    def set_up(self):
        self.field[0] = [rook("Black"),knight("Black"),bishop("Black"),queen("Black"),
                         king("Black"),bishop("Black"),knight("Black"),rook("Black")]
        self.field[7] = [rook("White"),knight("White"),bishop("White"),queen("White"),
                         king("White"),bishop("White"),knight("White"),rook("White")]
        self.field[1] = [pawn("Black") for i in range(8)]
        self.field[6] = [pawn("White") for i in range(8)]
        for i in range(2,6):
            self.field[i] = [None for i in range(8)]
            
    def __repr__(self):
        ret = ""
        f = self.field
        for i in range(8):
            ind = 8-i
            ret += str(ind) + ' '
            for j in range(8):
                c = chr(ord("A")+j)
                ret += self.icons[str(f[i][j])]
            ret += "\n"
        ret += '  '
        for c in range(ord("A"),ord("H")+1):
            ret += chr(c) + ' '
        return ret
    
    def pohni(self,c1 = ("A",1),c2 = ("H",8)):
        c1 = (ord(c1[0])-ord("A"),8-c1[1])
        c2 = (ord(c2[0])-ord("A"),8-c2[1])
        if self.field[c1[1]][c1[0]] is not None:
            if self.field[c1[1]][c1[0]].pohni(c1,c2,self.field):
                self.field[c2[1]][c2[0]] = self.field[c1[1]][c1[0]]
                self.field[c1[1]][c1[0]] = None
                return True
            else:
                return False
        return False


g = game()
print(g)


















