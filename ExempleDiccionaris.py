
class ExempleDiccionaris:

    # Constructor de la classe ExempleDiccionaris
    def __init__(self):
        print("ExempleDiccionaris creat.")

    def ExecutarExempleDiccionaris(self):

        #pass # Si un mètode el volem deixar buit, hem de posar el "pass".
        print("Inici exemple diccionaris:\n")

        # Guarden les dades en format clau-valor. Segueixen format JSON.

        # Definim un diccionari:
        exempleDiccionari = { "clau1": 10, "clau2": 15 }
        print(exempleDiccionari["clau2"])

        del exempleDiccionari["clau2"]
        print(exempleDiccionari)

        diccionariModul = {

            "Nom": "Sistemes de Gestió Empresarial",
            "Abreviatura": "SGE",
            "Codi": "M10",
            "alumnes": [
                {
                    "nom": "Yury",
                    "nota": 5
                },
                {
                    "nom": "Víctor",
                    "nota": 10
                },
                {
                    "nom": "Xavi",
                    "nota": 10
                }
            ]
        }

        # Sumar les notes de tots els alumnes
        sumaNotes = 0

        for alumne in diccionariModul["alumnes"]:

            sumaNotes += alumne["nota"]

        print("Resultat de la suma de notes: " + str(sumaNotes))
