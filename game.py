# -*- coding: utf-8 -*-
import sys
import os
from frame import *
sys.path[0:0] = [os.path.join(sys.path[0], './pieces')]

p = ["bishop","king","knight","pawn","queen","rook"]
com = ["from {} import {}".format(v,v) for v in p]
for c in com:
    exec(c)
    

class game():
    def __init__(self):
        self.field = [[None] * 8 for i in range(8)]
        self.set_up()
        self.g = frame(self.preloz())
        #sluzi na debug

        # pawn - pesiak
        # rook - veza
        # bishop - strelec
        # knight - kon
        # king - kral
        # queen - kralovna

        self.icons = {"White pawn":"♙","White rook":"♖","White knight":"♘",
                      "White bishop":"♗","White queen":"♕","White king":"♔",
                      "Black pawn":"♟","Black rook":"♜","Black knight":"♞",
                      "Black bishop":"♝","Black queen":"♛","Black king":"♚",
                      "None":"　"} # pozor, toto nie je obycajna medzera
        self.coord1,self.coord2 = None,None
        self.g.c.bind('<Button-1>',self.klik)
        
    def set_up(self):
        self.field[0] = [rook("Black"),knight("Black"),bishop("Black"),queen("Black"),
                         king("Black"),bishop("Black"),knight("Black"),rook("Black")]
        self.field[7] = [rook("White"),knight("White"),bishop("White"),queen("White"),
                         king("White"),bishop("White"),knight("White"),rook("White")]
        self.field[1] = [pawn("Black") for i in range(8)]
        self.field[6] = [pawn("White") for i in range(8)]
        for i in range(2,6):
            self.field[i] = [None] * 8

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
    
    def pohni(self, c1 = ("A",1), c2 = ("H",8)):
        c1 = (ord(c1[0])-ord("A"), 8-c1[1])
        c2 = (ord(c2[0])-ord("A"), 8-c2[1])

        inBounds = c1[0] in range(0,8) and c1[1] in range(0,8) and c2[0] in range(0,8) and c2[1] in range(0,8)
        if self.field[c1[1]][c1[0]] is not None and inBounds:
            if self.field[c1[1]][c1[0]].pohyb(c1,c2,self.field):
                self.field[c2[1]][c2[0]] = self.field[c1[1]][c1[0]]
                self.field[c1[1]][c1[0]] = None
                self.g.move(c1,c2)
                return True
            else:
                return False
        return False

    def g_pohni(self, c1, c2):
        c1,c2 = c1,c2

        inBounds = c1[0] in range(0,8) and c1[1] in range(0,8) and c2[0] in range(0,8) and c2[1] in range(0,8)
        if self.field[c1[1]][c1[0]] is not None and inBounds:
            if self.field[c1[1]][c1[0]].pohyb(c1,c2,self.field):
                self.field[c2[1]][c2[0]] = self.field[c1[1]][c1[0]]
                self.field[c1[1]][c1[0]] = None
                self.g.move(c1,c2)
                return True
            else:
                return False
        return False

    def preloz(self):
        # sluzi na vytvorenie pola na vykreslovanie cez klassu frame
        ret = [[None] * 8 for i in range(8)]
        for i in range(8):
            for j in range(8):
                if self.field[i][j] is not None:
                    ret[i][j] = str(self.field[i][j])
        return ret
    def klik(self,e):
        x,y = (e.x-50)//100,e.y//100
        print(x,y,str(self.field[y][x]))
        if self.coord1 is None:
            if self.field[y][x] is not None:
                print("Setting coord 1")
                self.coord1 = (x,y)
        elif self.coord1 is not None and self.coord2 is None:
            self.coord2 = (x,y)
            print("Setting coord 2")
        if self.coord1 is not None and self.coord2 is not None:
            print("Hybem z {} na {}... Vysledok je {}".format(self.coord1,self.coord2,
                                                              self.g_pohni(self.coord1,self.coord2)))
            self.coord1,self.coord2 = None,None
                







g = game()




