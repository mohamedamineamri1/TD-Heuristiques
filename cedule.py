# ordonnancement de la maintenance de 7 centrales (4 intervalles)
import random
CAPACITE = [20, 15, 35, 40, 15, 15, 10]       # MW de chaque unité
DEMANDE  = [80, 90, 65, 70]                   # MW demandés par intervalle
TOTAL    = sum(CAPACITE)                      # 150 MW
# Motifs de maintenance possibles (1 = en maintenance)
DEUX = ["1100", "0110", "0011"]               # unités 1 et 2 (2 intervalles)
UN   = ["1000", "0100", "0010", "0001"]       # unités 3 à 7 (1 intervalle)
CHOIX = [DEUX, DEUX, UN, UN, UN, UN, UN]
# ---- 1. Chromosome : liste de 7 gènes (un par unité)
def creer_individu():
    return [random.choice(CHOIX[i]) for i in range(7)]

# ---- 2. Fonction objectif : plus petite réserve (0 si négative)
def fitness(ind):
    plus_petite = 1000
    for t in range(4):
        perdue = sum(CAPACITE[i] for i in range(7) if ind[i][t] == "1")
        reserve = TOTAL - perdue - DEMANDE[t]
        plus_petite = min(plus_petite, reserve)
    return max(plus_petite, 0)

# ---- 3. Sélection par (roulette)
def loterie(pop, fits):
    if sum(fits) == 0:
        return random.choice(pop)
    return random.choices(pop, weights=fits, k=1)[0]

# ---- 4. Croisement à 1 point (entre deux gènes)
def croisement(p1, p2):
    pt = random.randint(1, 6)
    return p1[:pt] + p2[pt:], p2[:pt] + p1[pt:]

# ---- 5. Mutation par inversion : on inverse les bits d'un gène (1100 -> 0011)
def mutation(ind, pm=0.1):
    ind = ind[:]
    for i in range(7):
        if random.random() < pm:
            ind[i] = ind[i][::-1]
    return ind

# ---- 6. Boucle principale
random.seed(1)
pop = [creer_individu() for _ in range(30)]
for gen in range(40):
    fits = [fitness(c) for c in pop]
    meilleur = pop[fits.index(max(fits))]
    print("Génération", gen, "- meilleure fitness :", max(fits))
    nouvelle = [meilleur]                                  # élitisme
    while len(nouvelle) < 30:
        e1, e2 = croisement(loterie(pop, fits), loterie(pop, fits))
        nouvelle += [mutation(e1), mutation(e2)]
    pop = nouvelle[:30]

fits = [fitness(c) for c in pop]
best = pop[fits.index(max(fits))]
print("\nMeilleure cédule :", best, "-> réserve minimale =", max(fits), "MW")