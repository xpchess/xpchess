from piece import piece

# kon
class knight(piece):
    def pohyb(self,c1,c2,field):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]


        # if abs(fromX - fromY) == 1 and abs(toX - toY) == 2 and field[toY][toX] is None
        if abs(fromX - toX) == 1 and abs(fromY - toY) == 2:
            return True
            #elif abs(fromX - fromY) == 2 and abs(toX - toY) == 1 and field[toY][toX] is None:
        elif abs(fromX - toX) == 2 and abs(fromY - toY) == 1:
            return True
        else:
            return False