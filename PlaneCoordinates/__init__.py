##Creating a class for coordinates in the plane.

class coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other): #calculate distance between to points in the plane
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    
    def module(self): #calculate the module of a 2D vector
        return ((self.x**2)+(self.y**2))**0.5
    
    def __str__(self): #print the coordinates as <x,y>
        return '<'+str(self.x)+','+str(self.y)+'>'
    
    def __add__(self, other): #method to add two coordinates
        i = self.x+other.x
        j = self.y+other.y
        return coordinate(i, j)
    
    def __sub__(self, other): #method to substract two coordinates
        i = self.x-other.x
        j = self.y-other.y
        return coordinate(i, j)
        