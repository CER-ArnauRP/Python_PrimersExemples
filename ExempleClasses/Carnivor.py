from ExempleClasses.Animal import Animal

class Carnivor(Animal):

    def __init__(self, nom: str = "CarnivorGeneric"):
        self.nom = nom
        self.quantitatMenjada = 0
        print("Carnivor creat.")

    def MetodeEspecialCarnivor(self):
        print("Metode especial del carnivor.")

    def Menjar(self, quantitat: int = 1):

        self.quantitatMenjada += quantitat

        if quantitat == 1:
            print("El carnivor " + self.nom + " ha menjat 1 animal.")

        elif quantitat > 100 or quantitat == 0:
            print("Ha menjat molt o molt poc.")

        elif quantitat > 1 and self.quantitatMenjada >= 100:
            print("De moment no pot menjar més.")
            self.quantitatMenjada -= quantitat

        else:
            print("El carnivor " + self.nom + " ha menjat: " + str(quantitat) + " altres animals.")

