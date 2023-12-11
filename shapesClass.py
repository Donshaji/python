class shape:
    def __init__(self,no_side):
        self.no_side=no_side
class circle:
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2*3.14*(self.radius)
    def diameter(self):
        return 2*(self.radius)
    def area(self):
        return 3.14*(self.radius)*(self.radius)
class rectangle:
    def __init__(self):
        pass
# c1=circle(4)
# print(c1.diameter())