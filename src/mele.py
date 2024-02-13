import sys

sys.stdin = open('input/mele_input_1.txt', 'r')
sys.stdout = open('output/mele_output_1.txt', 'w')

def solve(t):
    input() # prima riga vuota

    N, M, C = map(int, input().strip().split())

    # aggiungi codice...
    risposta = min(N * M, C)

    print(f"Case #{t}: {risposta}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
