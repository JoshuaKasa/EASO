import sys

sys.stdin = open('input/soldatini_input_1.txt', 'r')
sys.stdout = open('output/soldatini_output_1.txt', 'w')


def solve(t):
    input()  # prima riga vuota
    N = int(input().strip())
    S = input().strip()

    # aggiungi codice...
    max_length = 0
    cur_length = 0
    prev_length = -1

    for p in S: # per ogni soldatino
        if p == '1':
            cur_length += 1
        else:
            max_length = max(max_length, cur_length + prev_length + 1)
            prev_length, cur_length = cur_length, 0

    max_length = max(max_length, cur_length + prev_length + 1)

    print(f"Case #{t}: {max_length}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
