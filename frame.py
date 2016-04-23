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
    def __init__(self,field):
        self.field = field
        self.ref = [[None] * 8 for i in range(8)]
        self.c = tkinter.Canvas(width=850,height=850,background='white')
        self.c.pack()
        self.plocha()
        self.update(field)
        
    def plocha(self):
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
    
    def update(self,field):
        #self.c.create_text(200,50,text="♛",font = "arial 66 bold")
        for i in range(8):
            for j in range(8):
                if field[i][j] is not None:
                    self.ref[i][j] = self.c.create_text((j+1)*100,50+i*100,
                                                        text=icons[field[i][j]],
                                                        font = "arial 66 bold")
    def move(self,c1,c2):
        print(c1,c2)
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]
        if self.ref[toY][toX] is not None:
            self.c.delete(self.ref[toY][toX])
            self.ref[toY][toX] = None
        self.c.move(self.ref[fromY][fromX],(toX-fromX)*100,(toY-fromY)*100)
        self.ref[toY][toX] = self.ref[fromY][fromX]
        self.ref[fromY][fromX] = None


