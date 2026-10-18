from collections import deque
def cout(chemin,villes):
    total = 0
    for i in range(len(chemin)):
        a = chemin[i] - 1
        b = chemin[(i + 1) % len(chemin)] - 1
        total += villes[a][b]
    return total
def valide(chemin,villes):
    for i in range(len(chemin)):
        a = chemin[i]-1
        b = chemin[(i+1) % len(chemin)] - 1
        if villes[a][b] ==-1:
            return False
    return True
def tabou(initial,villes):
    solution = initial[:]
    meilleure = initial[:]
    liste_taboue = deque(maxlen=5)
    for _ in range(5):
        voisins = []
        for i in range(1, len(solution)-1):
            for j in range(i + 1, len(solution)):
                voisin = solution[:]
                voisin[i],voisin[j] = voisin[j],voisin[i]

                if valide(voisin,villes) and voisin not in liste_taboue:
                    voisins.append(voisin)
        if not voisins:
            break
        meilleur_voisin = min(voisins, key=lambda x: cout(x, villes))
        liste_taboue.append(solution[:])
        solution = meilleur_voisin
        if cout(solution,villes) < cout(meilleure,villes):
            meilleure = solution[:]

    return meilleure
villes = [
    [-1, 14, 15, -1, -1, -1, -1, 17],
    [14, -1, 13, 14, 20, -1, -1, 21],
    [15, 13, -1, 11, 21, 17, 9, 9],
    [-1, 14, 11, -1, 11, 10, 8, 20],
    [-1, 20, 21, 11, -1, 15, 18, -1],
    [-1, -1, 17, 10, 15, -1, 9, -1],
    [-1, -1, 9, 8, 18, 9, -1, 21],
    [17, 21, 9, 20, -1, -1, 13, -1]
]

initial = [1, 2, 3, 4, 5, 6, 7, 8]
s = tabou(initial, villes)

print("Chemin :",s)
print("Cout :",cout(s,villes))