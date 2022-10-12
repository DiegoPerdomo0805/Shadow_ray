import struct
import numpy
import mmap
import math
from color import Color

class Envmap:
    def __init__(self, path):
        self.path = path
        self.read()
    
    def read(self):
        with open(self.path) as img:
            m = mmap.mmap(img.fileno(), 0, access=mmap.ACCESS_READ)
            ba = bytearray(m)
            header_size = struct.unpack('=l', ba[10:14])[0]
            self.width = struct.unpack('=l', ba[18:22])[0]
            self.height = struct.unpack('=l', ba[22:26])[0]
            all_bytes = ba[header_size::]
            #self.pixels = numpy.array(all_bytes).reshape(self.height, self.width, 3)
            self.pixels = numpy.frombuffer(all_bytes, dtype=numpy.uint8).reshape(self.height, self.width, 3)

    def get_color(self, direction):
        #x = (1 + math.atan2(direction.z, direction.x) / math.pi) * 0.5
        x = math.atan2(direction.z, direction.x) / (2 * math.pi) + 0.5
        y = math.acos(direction.y) / math.pi
        #y = math.acos(direction[1]) / math.pi
        x = int(x * self.width)
        y = int(y * self.height)

        index = ((y * self.width + x) * 3) % len(self.pixels)

        c = self.pixels[index:index+3].astype(numpy.unit8)
        return Color(c[0], c[1], c[2])
        #return Color(*self.pixels[y][x])
        #self.data = numpy.array(Image.open(self.path))
        #self.width = self.data.shape[0]
        #self.height = self.data.shape[1]