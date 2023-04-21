
class ExercicisPractiques:

    def __init__(self):
        print("Classe ExercicisPractiques creada.")


    def Exercici1DosNumsEnters(self):

        '''
        1) Demana dos enters a l'usuari, mostrant, per demanar-los, el text:
            "Primer enter: " i "Segon enter: "

        2) Mostra per pantalla el text:
            "La suma és: x i el seu producte és: y"
        '''
        inputUsuariPrimerEnter = int(input("Primer enter: "))
        inputUsuariSegonEnter = int(input("Segon enter: "))

        resultatSuma = inputUsuariPrimerEnter + inputUsuariSegonEnter
        resultatMultiplicacio = inputUsuariPrimerEnter * inputUsuariSegonEnter

        print("La suma és: " + str(resultatSuma) + " i el seu producte és: " + str(resultatMultiplicacio))

    def Exercici2DosNumsDecimals(self):

        # Fer el mateix que l'exercici 1, però els números poden ser decimals.
        inputUsuariPrimerEnter = float(input("Primer enter: "))
        inputUsuariSegonEnter = float(input("Segon enter: "))

        resultatSuma = inputUsuariPrimerEnter + inputUsuariSegonEnter
        resultatMultiplicacio = inputUsuariPrimerEnter * inputUsuariSegonEnter

        print("La suma és: " + str(resultatSuma) + " i el seu producte és: " + str(resultatMultiplicacio))

    def Exercici3DosNumsBucleInfinit(self):

        # Fer el mateix que en l'exercici 2, però en búcle infinit.
        while True:
            self.Exercici2DosNumsDecimals()

    def Exercici4DosNumsBucleXVegadesAmbWhile(self, numIteracions: int):

        # Fer el mateix que l'exercici 3, però només numIteracions vegades.
        # Si el numIteracions és més petit que 0, fer que valgui 1.
        # Si el numIteracions és float, convertir-lo a int.

        numIteracions = int(numIteracions)

        if numIteracions < 0:
            numIteracions = 1

        iteracioActual = 0
        while iteracioActual < numIteracions:
            self.Exercici2DosNumsDecimals()
            iteracioActual += 1

    def Exercici5DosNumsBucleXVegadesAmbFor(self, numIteracions: int):

        # Fer el mateix que l'exercici 4, però amb un for en comptes d'un while.

        print("Això és un range(4): ")
        print(range(4))

        numIteracions = int(numIteracions)
        if numIteracions < 0:
            numIteracions = 1

        for i in range(numIteracions):
            print("Iteració: " + str(i))
            self.Exercici2DosNumsDecimals()

    def Exercici6SwitchCase(self, opcioTriada: int = 1) -> str:

        stringARetornar = ""
        match opcioTriada:
            case 1:
                print("Opció1")
                stringARetornar = "Opció escollida: 1"

            case 2:
                print("Opció2")
                stringARetornar = "Opció escollida: 2"

            case _:
                print("OpcióDefault")
                stringARetornar = "Opció no contemplada (default)."

        return stringARetornar

    def Exercici7TaulaMultiplicar(self):

        '''
        1) Preguntar a l'usuari un número enter, del qual volem que ens mostri la taula
            de multiplicar del 0 al 10.
        2) Mostrar la taula en el següent format:
            (exemple si diguessin 5):
            5 x 0 = 0
            5 x 1 = 5
            5 x 2 = 10
            ...
        (fem servir un for)
        '''
        taulaDel = int(input("De quin número vos saber-ne la taula de multiplicar? "))

        for i in range(11):
            #print(str(taulaDel) + " x " + str(i) + " = " + str(taulaDel * i))
            # Altra manera de fer el print sense els casts.
            print(taulaDel, " x ", i, " = ", (taulaDel * i))
        else:
            print("Taula feta.")
