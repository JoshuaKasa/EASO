import sys

sys.stdin = open('input/calcio_input_1.txt', 'r')
sys.stdout = open('output/calcio_output_1.txt', 'w')

def solve(t):
    input() # prima riga vuota

    N, M, K, A, B = map(int, input().strip().split())
    alberi = [[0 for _ in range(M)] for _ in range(N)]

    # Riempimento della matrice con la presenza degli alberi
    for _ in range(K):
        x, y = map(int, input().strip().split())
        alberi[x][y] += 1

    # Calcolo del minimo numero di alberi da abbattere
    min_alberi = float('inf')
    for i in range(N-A+1):
        for j in range(M-B+1):
            # Contiamo gli alberi nella posizione attuale del campo
            alberi_da_abbattere = 0
            for a in range(A):
                for b in range(B):
                    alberi_da_abbattere += alberi[i+a][j+b]
            min_alberi = min(min_alberi, alberi_da_abbattere)

    print(f"Case #{t}: {min_alberi}")

T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
