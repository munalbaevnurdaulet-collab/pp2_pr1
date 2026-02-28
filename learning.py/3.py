class Coordinate(object):
    def __init__(self,xval,yval):
        self.x=xval
        self.y=yval
point=Coordinate(3,6)
print(point.x,end=' ')
print(point.y)