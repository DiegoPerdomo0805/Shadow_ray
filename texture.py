class Texture:
    def __init__(self, path):
        self.id = glGenTextures(1)
        self.type = GL_TEXTURE_2D
        self.path = path
        self.image = Image.open(path)
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.image_data = self.image.convert("RGBA").tobytes()

        self.width = self.image.width
        self.height = self.image.height

        self.bind()

        glTexParameteri(self.type, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(self.type, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(self.type, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(self.type, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexImage2D(self.type, 0, GL_RGBA, self.width, self.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.image_data)

    def bind(self):
        glBindTexture(self.type, self.id)