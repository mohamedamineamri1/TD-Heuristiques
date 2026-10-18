from collections import deque
def cout(s,couts):
    total = 0
    for i in range(len(s)):
        total = total+(couts[s[i]-1][i])
    return total
def valide(s,demandes,capacites):
    for d in range(len(capacites)):
        total = 0
        for i in range(len(s)):
            if s[i] == d+ 1:
                total =total+ demandes[i]
        if total > capacites[d]:
            return False
    return True
def tabou(initial,demandes,capacites,couts):
    solution = initial[:]
    liste_taboue = deque(maxlen=5)

    for _ in range(10):
        voisins =[]
        for i in range(len(solution)):
            for d in range(1, len(capacites)+1):
                voisin =solution[:]
                voisin[i] = d

                if voisin != solution and valide(voisin,demandes,capacites):
                    if voisin not in liste_taboue:
                        voisins.append(voisin)

        if not voisins:
            break
        meilleur = min(voisins, key=lambda x: cout(x,couts))
        liste_taboue.append(solution[:])

        if cout(meilleur,couts) < cout(solution,couts):
            solution = meilleur

    return solution
demandes =[4,5,8]
capacites = [8,9]
couts = [[5,3,4],[6,7,2]]
initial = [2,1,2]
s=tabou(initial,demandes,capacites,couts)

print("Solution :", s)
print("Le Cout total est  :", cout(s,couts))