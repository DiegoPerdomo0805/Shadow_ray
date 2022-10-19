from math import pi

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return pi * self.radius**2 * self.height
    
    def surface_area(self):
        return 2*pi*self.radius*self.height + 2*pi*self.radius**2

    def ray_intersect(self, origin, direction):
        # TODO
        return None