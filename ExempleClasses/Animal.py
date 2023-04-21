
class Animal:

    def __init__(self, nom: str):

        self.nom = nom
        self.kmRecurreguts = 0
        self.velocitat = 10
        print("Animal creat.")

    def Menjar(self, tipusAliment: str, quantitat: int):
        print("Menjant " + str(quantitat) + " de " + tipusAliment)

    def Passejar(self, ganesPassejar: float = 1.0) -> float:

        return ganesPassejar * self.velocitat