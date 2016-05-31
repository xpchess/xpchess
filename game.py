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
        self.ktoHra = "White"
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
        self.g.c.mainloop()

    def set_up(self):
        self.field[0] = [rook("Black"),knight("Black"),bishop("Black"),queen("Black"),
                         king("Black"),bishop("Black"),knight("Black"),rook("Black")]
        self.field[7] = [rook("White"),knight("White"),bishop("White"),queen("White"),
                         king("White"),bishop("White"),knight("White"),rook("White")]
        self.field[1] = [pawn("Black") for i in range(8)]
        self.field[6] = [pawn("White") for i in range(8)]
        for i in range(2,6):
            self.field[i] = [None] * 8

        self.ktoHra = "White"

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
        print(self.moj_kral())
        c1,c2 = c1,c2
        fig1 = self.field[c1[1]][c1[0]]
        fig2 = self.field[c2[1]][c2[0]]

        color1 = ""
        color2 = ""

        type1 = ""
        type2 = ""

        if fig1 is not None:
            color1 = str(fig1).split(' ')[0]
        if fig2 is not None:
            color2 = str(fig2).split(' ')[0]

        if fig1 is not None:
            type1 = str(fig1).split(' ')[1]
        if fig2 is not None:
            type2 = str(fig2).split(' ')[1]

        if color1 != self.ktoHra:
            return False
        
        inBounds = c1[0] in range(0,8) and c1[1] in range(0,8) and c2[0] in range(0,8) and c2[1] in range(0,8)
        if fig1 is not None and inBounds:

            if fig1.pohyb(c1,c2,self.field) and color1 != color2:
                if type1 == "king" and self.som_sach(c2):
                    return False
                else:
                    povodna1 = self.field[c2[1]][c2[0]]
                    povodna2 = self.field[c1[1]][c1[0]]

                    self.hyb_sa(c1, c2)
                    if self.som_sach(self.moj_kral()):
                        self.field[c2[1]][c2[0]] = povodna1
                        self.field[c1[1]][c1[0]] = povodna2
                        return False
                    else:
                        self.vymen_farbu_hraca()
                        return True

            elif str(fig1).split(' ')[1] == "pawn" and color1 != color2 and fig2 is not None:
                if fig1.vyhadzujem(c1,c2,self.field):
                    self.hyb_sa(c1, c2)
                    self.vymen_farbu_hraca()
                    return True
                else:
                    return False

            elif fig2 is not None and color1 == color2 and ((type1 == "king" and type2 == "rook") or (type2 == "king" and type1 == "rook")):

                if type1 == "king" and self.som_sach(c1):
                    return False

                if type2 == "king" and self.som_sach(c2):
                    return False

                if type1 == "rook":
                    c1, c2 = c2, c1

                return self.rosada(c1, c2, color1)

            else:
                return False
        return False

    def hyb_sa(self, c1, c2):
        self.field[c2[1]][c2[0]] = self.field[c1[1]][c1[0]]
        self.field[c2[1]][c2[0]].pohni_sa()
        self.field[c1[1]][c1[0]] = None
        self.g.move(c1, c2)

    def vymen_farbu_hraca(self):
        if self.ktoHra == "White":
            self.ktoHra = "Black"
        else:
            self.ktoHra = "White"

    def rosada(self, c1, c2, col):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]

        king = self.field[c1[1]][c1[0]]
        rook = self.field[c2[1]][c2[0]]

        if col=="Black":
            Ycor = 0
        else:
            Ycor = 7

        if fromY == toY and fromY == Ycor and not king.pohol_som_sa() and not rook.pohol_som_sa():
            if abs(fromX - toX) == 3 and rook.pohyb(c2, (fromX + 1, fromY), self.field):
                self.mala_rosada(c1, c2)
                return True
            elif abs(fromX - toX) == 4 and rook.pohyb(c2, (fromX - 1, fromY), self.field):
                print("VELKA")
                self.velka_rosada(c1, c2)
                return True
            else:
                return False

        else:
            return False



    def som_sach(self, c):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.field[i][j] is not None:
                    if self.field[i][j].color != self.ktoHra:
                        if self.field[i][j].pohyb((j,i), c, self.field):
                            return True

        return False

    def moj_kral(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if str(self.field[i][j]) == (self.ktoHra + " king"):
                    return (j,i)

    def mala_rosada(self, c1, c2):
        self.field[c2[1]][c2[0]-2] = self.field[c2[1]][c2[0]]
        self.field[c1[1]][c1[0]+2] = self.field[c1[1]][c1[0]]

        self.field[c2[1]][c2[0]] = None
        self.field[c1[1]][c1[0]] = None

        self.g.move(c2, (c2[0] - 2, c2[1]))
        self.g.move(c1, (c1[0] + 2, c1[1]))
        self.vymen_farbu_hraca()

    def velka_rosada(self, c1, c2):
        self.field[c2[1]][c2[0] + 3] = self.field[c2[1]][c2[0]]
        self.field[c1[1]][c1[0] - 2] = self.field[c1[1]][c1[0]]

        self.field[c2[1]][c2[0]] = None
        self.field[c1[1]][c1[0]] = None

        self.g.move(c2, (c2[0] + 3, c2[1]))
        self.g.move(c1, (c1[0] - 2, c1[1]))
        self.vymen_farbu_hraca()



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




