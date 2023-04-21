from ExempleClasses.Animal import Animal

class Hervibor(Animal):

    def __init__(self, nom:str = "HerviborGeneric"):

        self.nom = nom
        self.quantitatMenjada = 0
        print("Hervibor creat.")

    def MetodeEspecialHervibor(self):
        print("Mètode especial de l'hervibor.")

    def Menjar(self, quantitat: int = 1):

        self.quantitatMenjada = quantitat

        print("L'hervibor " + self.nom + " ha menjat.")