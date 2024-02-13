import sys

sys.stdin = open('input/muro_input_1.txt', 'r')
sys.stdout = open('output/muro_output_1.txt', 'w')

def solve(t):
    input()  # Ignora la prima riga vuota

    N, Q = map(int, input().split())  # Legge la lunghezza del muro e il numero di colori
    L = list(map(int, input().split()))  # Legge le larghezze dei rettangoli per ogni colore

    # Inizializza un array che tiene traccia delle parti del muro dipinte
    # 0 indica non dipinto, 1 indica dipinto
    muro_dipinto = [0] * N

    colori_visibili = 0

    for larghezza in L:
        visibile = False
        # Prova a dipingere il rettangolo per ogni posizione possibile
        for start in range(N - larghezza + 1):
            # Controlla se almeno parte del rettangolo sarebbe visibile
            if not all(muro_dipinto[start:start+larghezza]):
                visibile = True
                # Dipinge il rettangolo
                for i in range(start, start + larghezza):
                    muro_dipinto[i] = 1
        # Se il colore è visibile in almeno una parte, incrementa il contatore
        if visibile:
            colori_visibili += 1

    print(f"Case #{t}: {colori_visibili}")

T = int(input().strip())

for t in range(1, T + 1):
    solve(t)

