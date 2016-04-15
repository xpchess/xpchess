from piece import piece

# strelec
class bishop(piece):
    def pohyb(self,c1,c2,field):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]

        #pohyb po diagonale

        print(fromX - toX)
        print(fromY - toY)

        if abs(fromX - toX) == abs(fromY - toY):
            x_cor = list(range(toX, fromX, piece.vratKrok(toX, fromX)))
            y_cor = list(range(toY, fromY, piece.vratKrok(toY, fromY)))

            for x in range(1, len(x_cor)):
                if field[y_cor[x]][x_cor[x]] is not None:
                    return False
            return True
        else:
            return False
