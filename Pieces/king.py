from piece import piece

# kral
class king(piece):

    def pohyb(self,c1,c2,field):
        fromX = c1[0]
        fromY = c1[1]
        toX = c2[0]
        toY = c2[1]

        #hocijaky pohyb v rozsahu 1
        if abs(fromX - toX) < 2 and abs(fromY - toY) < 2:
            return True
        else:
            return False
