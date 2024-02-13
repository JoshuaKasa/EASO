import sys

sys.stdin = open('input/dadi_input_1.txt', 'r')
sys.stdout = open('output/dadi_output_1.txt', 'w')

def solve(t):
    input()  # prima riga vuota
    K = int(input().strip())
    A, B, C, D = map(int, input().strip().split())

    # aggiungi codice...
    # Calcola il punteggio iniziale
    punteggio_iniziale = A*1 + B*2 + C*3 + D*4
    
    # Cerca di sostituire i dadi con punteggio più basso con 4, in ordine da 1 a 3
    while K > 0:
        if A > 0:
            # Sostituisci i dadi con 1 se possibile
            da_cambiare = min(A, K)
            A -= da_cambiare
            D += da_cambiare
            K -= da_cambiare
            punteggio_iniziale += 3 * da_cambiare  # Ogni dado da 1 a 4 aggiunge 3 al punteggio
        elif B > 0:
            # Sostituisci i dadi con 2 se possibile
            da_cambiare = min(B, K)
            B -= da_cambiare
            D += da_cambiare
            K -= da_cambiare
            punteggio_iniziale += 2 * da_cambiare  # Ogni dado da 2 a 4 aggiunge 2 al punteggio
        elif C > 0:
            # Sostituisci i dadi con 3 se possibile
            da_cambiare = min(C, K)
            C -= da_cambiare
            D += da_cambiare
            K -= da_cambiare
            punteggio_iniziale += 1 * da_cambiare  # Ogni dado da 3 a 4 aggiunge 1 al punteggio
        else:
            # Non ci sono più dadi da cambiare
            break

    risposta = punteggio_iniziale

    print(f"Case #{t}: {risposta}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()

