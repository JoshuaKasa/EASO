import sys
from math import gcd

sys.stdin = open('input/territoriali_input_2.txt', 'r')
sys.stdout = open('output/territoriali_output_2.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())
    R = list(map(int, input().strip().split()))

    x = 0
    indistinguishable = 0
    for K in range(1, N + 1):
        if N % K == 0:
            is_indistinguishable = True
            for i in range(N):
                if R[i] != R[(i + K) % N]:
                    is_indistinguishable = False
                    break
            if is_indistinguishable:
                indistinguishable += 1
    x = indistinguishable

    print(f"Case #{test}: {x}")

sys.stdout.close()

