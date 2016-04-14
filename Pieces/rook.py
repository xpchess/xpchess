from piece import piece

# veza
class rook(piece):
    def pohyb(self,c1,c2,field):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]

        #pohyb hore - dole
        if fromX == toX and fromY != toY:
            for i in range(toY + piece.vratKrok(toY, fromY), fromY, piece.vratKrok(toY, fromY)):
                if field[i][fromX] is not None:
                    return False
            return True
        #pohyb dolava - doprava
        elif fromY == toY and fromX != toX:
            for i in range(toX + piece.vratKrok(toX, fromX), fromX, piece.vratKrok(toX, fromX)):
                if field[fromY][i] is not None:
                    return False
            return True

        else:
            return False
