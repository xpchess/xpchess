# -*- coding: utf-8 -*-
import tkinter
import sys
import os
sys.path[0:0] = [os.path.join(sys.path[0], './pieces')]

p = ["bishop","king","knight","pawn","queen","rook"]
com = ["from {} import {}".format(v,v) for v in p]
for c in com:
    exec(c)


icons = {"White pawn":"♙","White rook":"♖","White knight":"♘",
        "White bishop":"♗","White queen":"♕","White king":"♔",
        "Black pawn":"♟","Black rook":"♜","Black knight":"♞",
        "Black bishop":"♝","Black queen":"♛","Black king":"♚",
        "None":"　"}
class frame:
    def __init__(self,field,col):
        self.field = field
        self.ref = [[None] * 8 for i in range(8)]
        self.c = tkinter.Canvas(width=1050,height=950,background='white')
        self.c.pack()
        self.plocha(col)
        self.update(field)
        self.na_vyhodenie = None
        self.taken_white, self.taken_black = [], []
        
    def plocha(self,col):
        self.c.create_rectangle(50,2,850,800,outline="black",fill="white")
        for i in range(8):
            self.c.create_text(25,50+i*100,text=8-i,font="arial 25 bold")
            for j in range(8):
                x = 50 + j*100
                y = i * 100
                if i%2 == 0 and j % 2 == 1:
                    self.c.create_rectangle(x,y,x+100,y+100,fill = "#555555")
                elif i%2 == 1 and j % 2 == 0:
                    self.c.create_rectangle(x,y,x+100,y+100,fill = "#555555")
        for i in range(8):
            self.c.create_text(100+i*100,825,text=chr(ord('A')+i),font="arial 25 bold")
        self.c.create_rectangle(850,2,950,800,fill='#555555')
        self.c.create_rectangle(950,2,1050,800)
        self.c.create_text(950,830,text="Vyhodené",font="arial 25 bold")
        self.c.create_text(950,870,text="Figúrky",font="arial 25 bold")
        self.status = self.c.create_text(450,875,text="Na ťahu je {}".format(col),
                                         font = "arial 30 bold")


    def update(self,field):
        #self.c.create_text(200,50,text="♛",font = "arial 66 bold")
        for i in range(8):
            for j in range(8):
                if field[i][j] is not None:
                    self.ref[i][j] = self.c.create_text((j+1)*100,50+i*100,
                                                        text=icons[field[i][j]],
                                                        font = "arial 66 bold")
    def move(self,c1,c2):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]
        print(fromX,fromY,toX,toY)
        s = self.na_vyhodenie
        if self.ref[toY][toX] is not None and s is not None:
            if 'White' in s:
                l = len(self.taken_white)
                #print("Vyhadzujem o ", (8-toX),(l-toY), " z ",
                #      fromX, fromY)
                self.taken_white.append((self.ref[toY][toX],s))
                self.ref[toY][toX], self.na_vyhodenie = None,None
                self.c.move(self.taken_white[l][0],100*(8-toX),(l-toY)*100)
            elif 'Black' in s:
                l = len(self.taken_black)
                #print("Vyhadzujem o ", (9-toX),(l-toY), " z ",
                #      fromX, fromY)
                self.taken_black.append((self.ref[toY][toX],s))
                self.ref[toY][toX], self.na_vyhodenie = None,None
                self.c.move(self.taken_black[l][0],100*(9-toX),(l-toY)*100)
        elif self.ref[toY][toX] is not None:
            self.c.delete(self.ref[toY][toX])
            self.ref[toY][toX] = None
        self.c.move(self.ref[fromY][fromX],(toX-fromX)*100,(toY-fromY)*100)
        self.ref[toY][toX] = self.ref[fromY][fromX]
        self.ref[fromY][fromX] = None


    def statusupdate(self,col):
        self.c.itemconfig(self.status,text="Na ťahu je {}".format(col))

    def get_piece_name(self,p):
        for key in icons:
            if icons[key] == p and not "pawn" in key:
                return key

    def vyhod(self,p):
        self.na_vyhodenie = p

    def taken(self,c):
        if c == 'w':
            return len(self.taken_white)
        elif c == 'b':
            return len(self.taken_black)
    def ret(self,c,col,y):
        toX,toY = c
        if col == 'White':
            self.ref[toY][toX] = self.taken_white[y][0]
            ret = self.taken_white[y][1]
            self.c.move(self.ref[toY][toX],(toX-8)*100,(toY-y)*100)
            self.taken_white.remove(self.taken_white[y])
            return ret.split(' ')[1]
        elif col == 'Black':
            self.ref[toY][toX] = self.taken_black[y][0]
            ret = self.taken_black[y][1]
            self.c.move(self.ref[toY][toX],(toX-9)*100,(toY-y)*100)
            self.taken_black.remove(self.taken_black[y])
            return ret.split(' ')[1]








