class Point3D:
    """
    docstring444444
    """
    def __init__ (self, x, y, z):
        self.coord = (x, y, z)
    
    def __repr__ (self):
        return f"Point ({self.coord[0]}, {self.coord[1]}, {self.coord[2]})" 
    
P = Point3D(0.0, 1.0, 0.0)

# print(dir(Point3D))
# print(P.__dir__())  
# print(Point3D.__dict__)
# print(Point3D.__doc__)


