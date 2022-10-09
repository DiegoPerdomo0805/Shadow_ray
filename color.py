class Color(object):
    def __init__(this, r, g, b):
        this.r = r
        this.g = g
        this.b = b
    
    def __add__(this, other):
        if type(other) is Color:
            return Color(
                this.r + other.r,
                this.g + other.g,
                this.b + other.b
            )
        else:
            return Color(
                this.r + other,
                this.g + other,
                this.b + other
            )

    def __mul__(this, other):
        if type(other) is Color:
            return Color(
                this.r * other.r,
                this.g * other.g,
                this.b * other.b
            )
        else:
            return Color(
                this.r * other,
                this.g * other,
                this.b * other
            )

    def __repr__(self):
        return "Color(%s, %s, %s)" % (self.r, self.g, self.b)
    
    def toBytes(self) -> bytes:
        #bytes([int(self.r * 255), int(self.g * 255), int(self.b * 255) ])
        #print(bytes([int(self.r * 255), int(self.g * 255), int(self.b * 255) ]))
        r = 255 if int(self.r) > 255 else int(self.r) if int(self.r) > 0 else 0
        g = 255 if int(self.g) > 255 else int(self.g) if int(self.g) > 0 else 0
        b = 255 if int(self.b) > 255 else int(self.b) if int(self.b) > 0 else 0

        return bytes([b, g, r])

