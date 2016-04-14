from piece import piece

# pesiak
class pawn(piece):
    def pohyb(self,c1,c2,field):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]

        #kontrola pre cierny
        if self.color == "Black":
            #ked idem z prveho radu, mozem aj o dve
            if fromY == 1 and (toY - fromY) in range(1, 3) and fromX == toX:
                for i in range(toY - 1, fromY, -1):
                    if field[i][fromX] is not None:
                        return False
                return True
            #inak len o jedno
            elif (toY - fromY) == 1 and fromX == toX and field[toX][toY] is None:
                return True
            else:
                return False

        #kontrola pre biely
        else:
            # ked idem z prveho radu, mozem aj o dve
            if fromY == 6 and (fromY - toY) in range(1, 3) and fromX == toX:
                for i in range(toY + 1, fromY, 1):
                    if field[i][fromX] is not None:
                        return False
                return True
            # inak len o jedno
            elif (fromY - toY) == 1 and fromX == toX and field[toX][toY] is None:
                return True
            else:
                return False