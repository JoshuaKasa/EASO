import sys

sys.stdin = open('input/territoriali_input_3.txt', 'r')
sys.stdout = open('output/territoriali_output_3.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())

    A = list(map(int, input().strip().split()))

    B = list(map(int, input().strip().split()))

    x = 0

    pointer_A = 0
    pointer_B = 0

    while pointer_A < N and pointer_B < N:
        if A[pointer_A] == B[pointer_B]:
            x += 1
            pointer_A += 1
            pointer_B += 1
        elif A[pointer_A] < B[pointer_B]:
            pointer_A += 1
        else:
            pointer_B += 1


    print("Case #%d: " % test, end='')
    print(x)

sys.stdout.close()
