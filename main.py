from ExempleLlistes import ExempleLlistes
from ExempleDiccionaris import ExempleDiccionaris
from ExempleClasses.Animal import Animal
from ExempleClasses.Carnivor import Carnivor
from ExempleClasses.Hervibor import Hervibor
from ExempleClasses.Omnivor import Omnivor
from ExempleExercicis.ExercicisPractiques import ExercicisPractiques
from ExerciciPractica.Vertex import Vertex
# from <nom_arxiu (+ carpeta o ruta)> import <nom_classe>

# Creem un objecte de la classe ExempleLlistes
#exempleLlistes = ExempleLlistes()
#exempleLlistes.ExecutarExempleLlistes()

# Creem un objecte de la classe ExempleDiccionaris
#exempleDiccionaris = ExempleDiccionaris()
#exempleDiccionaris.ExecutarExempleDiccionaris()

# Exemple classes
# ===============
'''
animal1 = Animal("Animal1")
animal1.Menjar("galetes", 50)
print(animal1.Passejar(2.5))
print("Passeig de l'animal " + animal1.nom + "sense indicar valor: " + str(animal1.Passejar()))

carnivor1 = Carnivor("Tigre")
carnivor1.Menjar(100)

hervibor1 = Hervibor("Diplodocus")
hervibor1.Menjar(2)

omnivor1 = Omnivor()
omnivor1.MetodeEspecialCarnivor()
omnivor1.MetodeEspecialHervibor()
omnivor1.Menjar(2)
'''

'''
objecteExercicis = ExercicisPractiques()

#objecteExercicis.Exercici1DosNumsEnters()
#objecteExercicis.Exercici2DosNumsDecimals()
#objecteExercicis.Exercici3DosNumsBucleInfinit()
#objecteExercicis.Exercici4DosNumsBucleXVegadesAmbWhile(1.9)
#objecteExercicis.Exercici5DosNumsBucleXVegadesAmbFor(3)
#print(objecteExercicis.Exercici6SwitchCase(4))
objecteExercicis.Exercici7TaulaMultiplicar()
'''
# ====================================================================
'''
1) Creeu la classe vèrtex (Vertex). 
    - Ha de contenir 3 floats: "x", "y" i "z".
    - Ha de contenir un mètode MostraVertex, que mostra els 3 floats 
        en el format (x, y, z) (amb els parèntesis i les comes)(exemple: (1.0, 2.0, 1.0)).

2) En el main, creeu una llista i guardeu-hi 3 vèrtex que formin un triangle.

3) Mostreu en un print, els vèrtex de la llista.
'''
'''
vertex1 = Vertex(1.0, 1.0, 1.0)
llistaVertex = []
llistaVertex.append(vertex1)
llistaVertex.append(Vertex(2.0, 1.0, 1.0))
llistaVertex.append(Vertex(1.5, 2.0, 1.0))

for i in range(len(llistaVertex)):
    llistaVertex[i].MostraVertex()

for vertex in llistaVertex:
    vertex.MostraVertex()
'''
'''
1) Fer la classe ColorRGB:
    - Rep 3 enters en els atributs: r, g i b de tipus enter.

2) Fer que la classe Vertex heredi de ColorRGB.

3) Fes un mètode a ColorRGB per mostrar el color.

4) Crea un Vertex i mostra la posició i el color.
'''
v2 = Vertex()
v2.MostraVertex()
v2.MostraColor()

v3 = Vertex(1.0, 2.2, 2.2, 100, 200, 255)
