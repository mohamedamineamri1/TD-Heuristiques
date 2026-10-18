from random import randint,random
from math import exp
def cout(chemin,villes):
    total = 0
    for i in range(len(chemin)):
        a = chemin[i] - 1
        b = chemin[(i+1) % len(chemin)] -1
        total =total+ villes[a][b]
    return total
def valide(chemin, villes):
    for i in range(len(chemin)):
        a = chemin[i] - 1
        b = chemin[(i+1) % len(chemin)] - 1
        if villes[a][b] == -1:
            return False
    return True
def recuit(chemin,villes):
    solution =chemin[:]
    temperature = 100

    for _ in range(5):
        voisin = solution[:]
        i =randint(1,6)
        j =randint(1,6)
        voisin[i],voisin[j] = voisin[j],voisin[i]

        if valide(voisin,villes):
            delta = cout(voisin,villes) -cout(solution,villes)

            if delta < 0 or random() < exp(-delta / temperature):
                solution = voisin
        temperature = temperature / 2
    return solution
villes = [
    [-1, 14, 15, -1, -1, -1, -1, 17],
    [14, -1, 13, 14, 20, -1, -1, 21],
    [15, 13, -1, 11, 21, 17, 9, 9],
    [-1, 14, 11, -1, 11, 10, 8, 20],
    [-1, 20, 21, 11, -1, 15, 18, -1],
    [-1, -1, 17, 10, 15, -1, 9, -1],
    [-1, -1, 9, 8, 18, 9, -1, 13],
    [17, 21, 9, 20, -1, -1, 13, -1]
]

initial = [1, 2, 3, 4, 5, 6, 7, 8]
s = recuit(initial,villes)
print("Chemin :",s)
print("Cout :",cout(s,villes))