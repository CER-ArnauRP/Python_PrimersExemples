from ExempleClasses.Carnivor import Carnivor
from ExempleClasses.Hervibor import Hervibor

class Omnivor(Hervibor, Carnivor):

    def __init__(self, nom: str = "OmnivorGeneric"):
        self.nom = nom
        self.quantitatMenjada = 0

    def Menjar(self, quantitat: int = 1):
        Carnivor.Menjar(self, quantitat)
        Hervibor.Menjar(self, quantitat)

