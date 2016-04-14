class piece(object):
    def __init__(self,col):
        if col in ["Black","White"]:
            self.color = col
        else:
            raise TypeError
    def __str__(self):
        typ = str(type(self)).split(".")[1][:-2]
        return "{} {}".format(self.color,typ)
    def __repr__(self):
        typ = str(type(self)).split(".")[1][:-2]
        return "{} {}".format(self.color,typ)
    def pohyb(self,c1,c2,field):
        pass
    def vratKrok(a, b):
        if a < b:
            return 1
        else:
            return -1
    pass

