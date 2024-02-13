import sys

sys.stdin = open('input/logo_input_1.txt', 'r')
sys.stdout = open('output/logo_output_1.txt', 'w')

def solve(t):
    input()  # Legge la riga vuota
    N, M = map(int, input().strip().split())
    I = []  # Logo iniziale
    F = []  # Logo finale
    for i in range(N):
        I.append(input().strip())
    for i in range(N):
        F.append(input().strip())

    # Inizializza le variabili per trovare l'adesivo minimo
    min_x, min_y, max_x, max_y = M, N, -1, -1

    for i in range(N):
        for j in range(M):
            if I[i][j] != F[i][j] and F[i][j] == 'N':
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                min_y = min(min_y, i)
                max_y = max(max_y, i)

    # Calcola l'area dell'adesivo
    if min_x <= max_x and min_y <= max_y:
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
    else:
        area = 0  # Nessuna modifica necessaria

    print(f"Case #{t}: {area}")

T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()

