import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def solve(t):
    input() # Prima riga vuota

    N, M, Q = map(int, input().strip().split())
    S = input().strip()

    # Aggiungi codice se vuoi

    risposta = []
    for i in range(Q):
        w, *args = input().strip().split()
        a, b = map(int, args)

        if w == 's':
            # Aggiungi codice...
            pass

        elif w == 'c':
            # Aggiungi altro codice...
            risposta.append('A')


    print(f"Case #{t}:", ''.join(risposta))


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
