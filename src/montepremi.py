import sys
from math import gcd as mcd

sys.stdin = open('input/montepremi_input_1.txt', 'r')
sys.stdout = open('output/montepremi_output_1.txt', 'w')

def mcm(a, b):
    return a * b // mcd(a, b)

def solve(t):
    input()
    N = int(input().strip())
    V = list(map(int, input().strip().split()))

    # aggiungi codice...
    risposta = 0
    for i in range(N):
        if i == 0:
            risposta = V[i]
        else:
            risposta = mcm(risposta, V[i])

    print(f"Case #{t}: {risposta}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
