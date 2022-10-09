from lib import norm

class Light:
    def __init__(self, position, intensity, color):
        self.position = norm(position)
        self.intensity = intensity
        self.color = color
        