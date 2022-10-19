from sndhdr import SndHeaders
from ray import RayTracer
from material import Material
from sphere import Sphere
#from plane import Plane
from plane import PlaneY, PlaneX, PlaneZ, Cube, Cuboid, Tree
from color import Color
from light import Light
from lib import V3

rubber = Material(diffuse=Color(255, 0, 0), albedo = [1, 0, 0, 0], spec = 10 )
white_rubber = Material(diffuse=Color(255, 255, 255), albedo = [1, 0, 0, 0], spec = 10 )
#red_metal = Material(diffuse=Color(255, 0, 0), albedo = [0.8, 0.2], spec = 70)
ivory = Material(diffuse=Color(255, 255, 255), albedo = [0.7, 0.3, 0, 0], spec = 50)
wood = Material(diffuse=Color(255, 255, 255), albedo = [0.7, 0.3, 0, 0], spec = 50)

mirror = Material(diffuse=Color(255, 255, 255), albedo = [0.0, 1.0, 0.8, 0], spec = 1425)
glass = Material(diffuse=Color(255, 255, 255), albedo = [0.0, 0.5, 0.1, 0.8], spec = 125, refractive_index = 1.5)

sand = Material(diffuse=Color(244, 209, 107), albedo = [0.9, 0.1, 0, 0], spec = 50)
steel = Material(diffuse=Color(255, 255, 255), albedo = [0.8, 0.2, 0, 0], spec = 50)
#dummy = Material(diffuse=Color(255, 0, 0), albedo = [0, 0, 1, 0], spec = 50, refractive_index = 1)
#refractive index agua = 1.33
#refractive index vidrio = 1.5
#refractive index diamante = 2.42



#white_cotton = Material(diffuse=Color(255, 255, 255), albedo = [0.9, 0.1], spec = 0)
#dark_brown_cotton = Material(diffuse=Color(181, 101, 29), albedo = [0.9, 0.1], spec = 0)
#light_brown_cotton = Material(diffuse=Color(200, 157, 124), albedo = [0.9, 0.1], spec = 0)
#black_metal = Material(diffuse=Color(0, 0, 0), albedo = [0.8, 0.2], spec = 70)

r = RayTracer(500, 500)

r.light = Light(V3(20, 40, 60), 2, Color(255, 255, 255))
#r.scene =[
#    Sphere(V3(0, 0, -10), 1, glass), 
#    Sphere(V3(0, 0, -12), 1, rubber),
#]
pos = V3(0, -2, -7.5 )
######print(pos)
######print(pos.x)
######print(pos.y)
######print(pos.z)

size = 2
# r.scene =[ 
#     #Cube(2, V3(-2.25,-2.25,-7.5), ivory),
#     #Sphere(V3(0, -1.5, -10), 1, ivory),
#     #Sphere(V3(0, 0, -5), 0.5, mirror),
#     #Sphere(V3(1, 1, -8), 1, rubber),
#     #Sphere(V3(0.33, 0, -7), 0.5, glass),
#     ##Sphere(V3(-3, 3, -10), 2, mirror),
#     #Plane(V3(0, -3, 0), rubber),
#     PlaneY(V3(0+2.25, (size/2) +2.25, -7.5), size, size, rubber),
#     PlaneY(V3(0+2.25, -(size/2)+2.25, -7.5), size, size, rubber),

#     PlaneX(V3((size/2) -2.25, 0 -2.25, -7.5), size, size, rubber),
#     PlaneX(V3(-(size/2)-2.25, 0 -2.25, -7.5), size, size, rubber),
#     #PlaneX(V3(2, 3, -7.5), size, size, mirror, False),
#     #PlaneZ(V3(0, 0+1, -(-7.5)+(size/2)), size, size, rubber),
#     PlaneZ(V3(0+2.25, 0-2.25, -(-7.5)-(size/2)), size, size, rubber),
    
#     #PlaneZ(V3(0, 0, 7.5), size, size, mirror),
#     #PlaneZ(V3(0, 0, -(-7.5)-(size/2)), size, size, mirror),

#     #PlaneZ(V3(-1, 0, 1), 0.5, 2, rubber, False),
#     #PlaneY(V3(0, -3, 0), 5, 10, mirror),
# ]
#cube = Cube(2, V3(-2.25,-2.25,-7.5), ivory)
#for e in cube:
#    r.scene.append(e)

#Cube(1, V3(1.8,1.7,-4), glass, r.scene)
r.scene.append(PlaneY(V3(0, -3, -7.5), 15, 5, rubber))
#r.scene.append(PlaneZ(V3(0, 0, 7.5), 7, 1, rubber))
###Cuboid(2, 1.2, 5, V3(2,2,-9), rubber, r.scene)

Cuboid(0.5, 5, 0.5, V3(-2,-3,-9), wood, r.scene)
Cuboid(3, 0.5, 3,   V3(-2,-0.5,-9), rubber, r.scene)
Cuboid(2.5, 0.5, 2.5, V3(-2,0,-9), rubber, r.scene)
Cuboid(2, 0.5, 2,   V3(-2,0.5,-9), rubber, r.scene)
Cuboid(1.5, 0.5, 1.5, V3(-2,1,-9), rubber, r.scene)
Tree(4, r.scene, 3, -3, -10, wood, rubber)



# Cube(1, V3(1.8,1.7,-7), sand, r.scene)
# Cube(1, V3(0,1.7,-7), glass, r.scene)
# Cube(1, V3(-1.8,1.7,-7), steel, r.scene)
# Cube(1, V3(0.9,-1.7,-7), ivory, r.scene)
# Cube(1, V3(-0.9,-1.7,-7), rubber, r.scene)

#r.scene.append(Sphere(V3(-2, -1.7, -6), 0.33, rubber))

#Cuboid(1, 2, 1, V3(0.9,-1,-5), rubber, r.scene)
#Cube(1, V3(0.5,0.5,-3), glass, r.scene)
#r.scene.append(Sphere(V3(0, 0, -5), 0.5, rubber))


#PlaneY(V3(0+pos.x, (size/2)+pos.y, 0+pos.z), size, size, mirror),
#    PlaneY(V3(0+pos.x, -(size/2)+pos.y, 0+pos.z), size, size, mirror),
#
#    PlaneX(V3((size/2)+pos.x, 0+pos.y, 0+pos.z), size, size, mirror),
#    PlaneX(V3(-(size/2)+pos.x, 0+pos.y, 0+pos.z), size, size, rubber),
#    #PlaneX(V3(2, 3, 0+pos.z), size, size, mirror, False),
#    PlaneZ(V3(0+pos.x, 0+pos.y, -(pos.z)+(size/2)), size, size, mirror),

#r.scene = [
#    Sphere(V3(0, -1.5, -8), 0.5, ivory),
#    Sphere(V3(-1, 2, -7), 2, glass),
#    Sphere(V3(1, 1, -8), 1.7, rubber),
#    Sphere(V3(-2, 2, -9), 1, ivory),
#]

#r.light = Light(position=V3(0, 0, 0), intensity=1.4, color= Color(255, 255, 255))
#r.scene = [
#    #Sphere(V3(-2, 0, -10), 1, red_metal),
#    #Sphere(V3(-3, 1, -10), 0.5, dark_brown_cotton),
#    #Sphere(V3(-1, 1, -10), 0.5, dark_brown_cotton),
#    #Sphere(V3(-3.25, -0.5, -10), 0.5, dark_brown_cotton),
#    #Sphere(V3(-0.75, -0.5, -10), 0.5, dark_brown_cotton),
#
#    Sphere(V3(-2, -1.5, -10), 0.75, dark_brown_cotton),
#    Sphere(V3(-2.625, -2.125, -10), 0.375, dark_brown_cotton),
#    Sphere(V3(-1.375, -2.125, -10), 0.375, dark_brown_cotton),
#    Sphere(V3(-1.6, -1.2, -8), 0.25, light_brown_cotton),
#
#    Sphere(V3(-1.4, -1.1, -7), 0.05, black_metal),
#    Sphere(V3(-1.65, -1.2, -7), 0.05, black_metal),
#    Sphere(V3(-1.15, -1.2, -7), 0.05, black_metal),
#
#
#
#    #Sphere(V3(2, 0, -10), 1, ivory),
#    #Sphere(V3(3, 1, -10), 0.5, white_cotton),
#    #Sphere(V3(1, 1, -10), 0.5, white_cotton),
#    #Sphere(V3(3.25, -0.5, -10), 0.5, white_cotton),
#    #Sphere(V3(0.75, -0.5, -10), 0.5, white_cotton),
#    #Sphere(V3(2, -1.5, -10), 0.75, white_cotton),
#    #Sphere(V3(2.625, -2.125, -10), 0.375, white_cotton),
#    #Sphere(V3(1.375, -2.125, -10), 0.375, white_cotton),
#    #Sphere(V3(1.6, -1.2, -8), 0.25, white_cotton),
#    #Sphere(V3(1.4, -1.1, -7), 0.05, black_metal),
#    #Sphere(V3(1.65, -1.2, -7), 0.05, black_metal),
#    #Sphere(V3(1.15, -1.2, -7), 0.05, black_metal),
#    ##prueba de material
#]
r.dense = 1
r.render()