import sys

sys.stdin = open('input/partita_input_1.txt', 'r')
sys.stdout = open('output/partita_output_1.txt', 'w')

def solve(t):
    input()  # Legge la riga vuota
    N, K = map(int, input().strip().split())  # Numero di caselle e soldatini iniziali
    R = list(map(int, input().strip().split()))  # Rinforzi disponibili per ogni casella

    soldatini = K  # Soldatini disponibili all'inizio
    rinforzi_utilizzati = 0  # Rinforzi utilizzati

    for i in range(N):
        if soldatini - 1 + R[i] >= N - i or soldatini >= N - i:
            # Se i soldatini (escluso il sacrificio) più i rinforzi sono sufficienti
            # per raggiungere la fine, o se i soldatini attuali sono già sufficienti
            if R[i] > 0 and soldatini - 1 < N - i:  # Se il rinforzo è necessario
                soldatini += R[i]  # Usa il rinforzo
                rinforzi_utilizzati += 1  # Incrementa i rinforzi utilizzati
        soldatini -= 1  # Sacrifica un soldatino per avanzare
        if soldatini < 1:  # Se non ci sono più soldatini, interrompe il ciclo
            break

    risposta = rinforzi_utilizzati if soldatini >= 1 else -1  # Determina la risposta

    print(f"Case #{t}: {risposta}")

T = int(input().strip())

for t in range(1, T + 1):
    solve(t)

sys.stdout.close()

