from lib import V3, sum, sub, mul, dot, cross, length, norm
from intersect import Intersect

class Plane(object):
    def __init__(self, position, material, normal = V3(0, 1, 0)):
        self.position = position
        self.normal = normal
        self.material = material

    def ray_intersect(self, origin, direction):
        denom = dot(direction, self.normal)
        if abs(denom) > 0.0001:
            t = dot(sub(self.position, origin), self.normal) / denom
            if t >= 0:
                hit = sum(origin, mul(direction, t))
                return Intersect(distance=t, point=hit, normal=self.normal)
        return None

class Plane2(object):
    def __init__(self, center, w, h, material):
        self.center = center
        self.w = w
        self.h = h
        self.material = material

    def ray_intersect(self, origin, direction):
        d = -(origin.y + self.center.y) / direction.y
        impact = sum(origin, mul(direction, d))
        normal = V3(0, -1, 0)
        # z with height
        # x with width

        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) \
            or impact.z > (self.center.z + self.h/2) or impact.z < (self.center.z - self.h/2):
            #impact.x < -self.w or impact.x > self.w \
            #or impact.z < -self.h or impact.z > self.h
            return None
        return Intersect(distance=d, point=impact, normal=normal)