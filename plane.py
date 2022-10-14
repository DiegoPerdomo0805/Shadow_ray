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


#plano a lo largo del eje y
class Plane2(object):
    def __init__(self, center, w, h, material, under=True):
        self.center = center
        self.w = w
        self.h = h
        self.under = under
        self.material = material

    def ray_intersect(self, origin, direction):
        d = -(origin.y + self.center.y) / direction.y
        impact = sum(origin, mul(direction, d))
        normal = V3(0, -1, 0)
        #if self.under:
         #   normal = V3(0, -1, 0)
        #else:
         #   normal = V3(0, 1, 0)
        # z with height
        # x with width

        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) \
            or impact.z > (self.center.z + self.h/2) or impact.z < (self.center.z - self.h/2):
            #impact.x < -self.w or impact.x > self.w \
            #or impact.z < -self.h or impact.z > self.h
            return None
        return Intersect(distance=d, point=impact, normal=normal)


#plano a lo largo del eje x
class Plane3(object):
    def __init__(self, center, w, h, material, left=True):
        self.center = center
        self.w = w
        self.h = h
        self.left = left
        self.material = material

    def ray_intersect(self, origin, direction):
        d = -(origin.x + self.center.x) / direction.x
        impact = sum(origin, mul(direction, d))
        #normal = V3(-1, 0, 0)
        normal = V3(0, 0, 0)
        if self.left:
            normal = V3(-1, 0, 0)
        else:
            normal = V3(1, 0, 0)
        # z with height
        # x with width

        if d <= 0 or \
            impact.y > (self.center.y + self.w/2) or impact.y < (self.center.y - self.w/2) \
            or impact.z > (self.center.z + self.h/2) or impact.z < (self.center.z - self.h/2):
            #impact.x < -self.w or impact.x > self.w \
            #or impact.z < -self.h or impact.z > self.h
            return None
        return Intersect(distance=d, point=impact, normal=normal)



#plano a lo largo del eje z
class Plane4(object):
    def __init__(self, center, w, h, material, front=True):
        self.center = center
        self.w = w
        self.h = h
        self.front = front
        self.material = material

    def ray_intersect(self, origin, direction):
        d = -(origin.z + self.center.z) / direction.z
        impact = sum(origin, mul(direction, d))
        normal = V3(0, 0, 1)
        #if self.front:
        #    normal = V3(0, 0, 1)
        #else:
        #    normal = V3(0, 0, -1)
        # z with height
        # x with width

        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) \
            or impact.y > (self.center.y + self.h/2) or impact.y < (self.center.y - self.h/2):
            #impact.x < -self.w or impact.x > self.w \
            #or impact.z < -self.h or impact.z > self.h
            return None
        return Intersect(distance=d, point=impact, normal=normal)

def Cube(size, pos, material, scene):
    c = [
        Plane2(V3(0+pos.x, (size/2)+pos.y, pos.z), size, size, material),
        Plane2(V3(0+pos.x, -(size/2)+pos.y, pos.z), size, size, material),
        Plane3(V3((size/2)-pos.x, 0-pos.y, pos.z), size, size, material),
        Plane3(V3(-(size/2)-pos.x, 0-pos.y, pos.z), size, size, material),
        Plane4(V3(0+pos.x, 0-pos.y, -(pos.z)-(size/2)), size, size, material),
    ]
    for e in c:
        scene.append(e)