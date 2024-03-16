import sys

sys.stdin = open('input/territoriali_input_4.txt', 'r')
sys.stdout = open('output/territoriali_output_4.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    A, B = map(int, input().strip().split())

    X = 0
    S = A + B
    n = int((2 * S) ** 0.5)
    while n * (n + 1) // 2 < S:
        n += 1

    # Verifica se è possibile trovare una soluzione
    if n * (n + 1) // 2 != S:
        X = "IMPOSSIBLE"
    else:
        sequence = []
        for day in range(n, 0, -1):
            if A >= day:
                sequence.append('1')
                A -= day
            else:
                sequence.append('2')
        X = ''.join(reversed(sequence))

    print(f"Case #{test}: {X}")

sys.stdout.close()
