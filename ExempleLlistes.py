
class ExempleLlistes:

    def __init__(self):
        print("ExempleLlistes creat.")

    def ExecutarExempleLlistes(self):
        # Comentari d'una línia.

        '''
        Comentari
        multilinia fet amb 3 apòstrofs.
        '''

        print("Hola" + str(2))
        resultat = 2 + 2
        print(str(resultat) + "Hola")

        # Llistes en Python
        llistaNums = [0, 1, 2, 3]
        print(str(llistaNums) + " de longitud " + str(len(llistaNums)))
        print("Posició 2 de la llista " + str(llistaNums) + " = " + str(llistaNums[1]))

        llistaVariada = [0, 1, "Hola", 2.3, 2, ["Subllista a la pos 6", 0, 2]]
        print(llistaVariada)

        print(llistaVariada[1])
        print("Útima posició de la llistaVariada: " + str(llistaVariada[len(llistaVariada) - 1]))

        llistaPerModificar = [2, 2, 3, 4]
        llistaPerModificar.append("Hola")
        llistaPerModificar.insert(1, "nou valor")
        print(llistaPerModificar)

        llistaPerModificar.pop(1)
        print(llistaPerModificar)

        # slicing de llistes
        llistaPerSlicing = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print(llistaPerSlicing[8:0:-1])
        print(llistaPerSlicing[:0:-1])# No cal fer el len()
