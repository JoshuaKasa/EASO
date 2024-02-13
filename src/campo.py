import sys

sys.stdin = open('input/campo_input_1.txt', 'r')
sys.stdout = open('output/campo_output_1.txt', 'w')

def solve(t):
    input()  # prima riga vuota
    N = int(input().strip())
    S = list(map(int, input().strip().split()))

    # aggiungi codice...
    risposta = 0
    left = 0
    zero_count = 0

    # Cazzatona di sliding window
    for right in range(N):
        if S[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if S[left] == 0:
                zero_count -= 1
            left += 1
        risposta = max(risposta, right - left + 1)

    print(f"Case #{t}: {risposta}")

T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
