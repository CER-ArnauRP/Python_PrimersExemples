from ExerciciPractica.ColorRGB import ColorRGB

class Vertex(ColorRGB):

    def __init__(self,
                 x: float = 0.0, y: float = 0.0, z: float = 0.0,
                 r: int = 0, g: int = 0, b: int = 0):
        ColorRGB.__init__(self, r, g, b)
        self.x = x
        self.y = y
        self.z = z

    def MostraVertex(self):

        print("v(", self.x, ",", self.y, ",", self.z, ")")
