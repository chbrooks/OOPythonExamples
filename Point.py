class Point :
    ## here is a constructor.
    def __init__(self, x=0,y=0) :
        self.xval = x
        self.yval = y

# this is how we define methods. Note that the def is inside the scope of the class
    def isOrigin(self):
        return self.xval == 0 and self.yval == 0

    ## This is how we overload operators
    def __add__(self, other):
        return Point(self.xval + other.xval, self.yval + other.yval)

    def __sub__(self, other):
        return Point(self.xval - other.xval, self.yval - other.yval)

    def __eq__(self, other):
        return self.xval == other.xval and self.yval == other.yval

    ## This is how we overload the display method
    def __repr__(self):
       return f"x: {self.xval}, y: {self.yval}"



if __name__  =="__main__" :
    p = Point(2,2)
    p2 = Point(1,1)
    print(p + p2)
    print(p2 - p)
    print(p2.isOrigin())
