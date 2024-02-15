def scosse(N: int):
    chests = [i for i in range(1, N+1)] # Generatore delle casse
    shock_map = {i: [] for i in range(1, N+1)} # Mappa degli scossoni
    ordered_chests = chests.sort() # Lista delle casse ordinate
   
    # Creazione della mappa delle scosse
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                shock_map[i].append(j)

    # Calcolo e ritorno la media delle scosse
    return sum([len(shock_map[i]) for i in range(1, N+1)]) / N

print(scosse(3))
