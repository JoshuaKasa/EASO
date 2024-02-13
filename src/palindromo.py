import sys

sys.stdin = open('input/palindromo_input_1.txt', 'r')
sys.stdout = open('output/palindromo_output_1.txt', 'w')

def solve(t):
    input()

    N, M = map(int, input().strip().split())
    X, Y = map(int, input().strip().split())

    A = [0] * M
    B = [0] * M
    L = [''] * M

    for i in range(M):
        line = input().strip().split()
        A[i], B[i] = map(int, line[:2])
        L[i] = line[2]

    # aggiungi codice...
    risposta = 42


    print(f"Case #{t}: {risposta}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
