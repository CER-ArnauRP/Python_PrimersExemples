
class ColorRGB:

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = r
        self.g = g
        self.b = b

    def MostraColor(self):
        print("RGB(",self.r, ",", self.g, ",", self.b, ")")