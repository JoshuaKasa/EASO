import sys

sys.stdin = open('input/fossili_input_1.txt', 'r')
sys.stdout = open('output/fossili_output_1.txt', 'w')

def solve(t):
    input()
    a1, a2 = map(int, input().strip().split())
    b1, b2 = map(int, input().strip().split())
    c1, c2 = map(int, input().strip().split())

    # aggiungi codice...
    risposta = 0

    # Trovo il numero di numeri in comune tra i 3 intervalli
    if a2 < b1 or b2 < a1:
        risposta = 0
    else:
        risposta = min(a2, b2) - max(a1, b1) + 1
        if c2 < max(a1, b1) or c1 > min(a2, b2):
            risposta = 0
        else:
            risposta = min(risposta, min(c2, min(a2, b2)) - max(c1, max(a1, b1)) + 1)

    print(f"Case #{t}: {risposta-1}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
