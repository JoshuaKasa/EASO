import sys

sys.stdin = open('input/territoriali_input_1.txt', 'r')
sys.stdout = open('output/territoriali_output_1.txt', 'w')

def find_peak_with_max_prominence(N, H):
    max_prominence = -1
    index_of_max_prominence = -1
    for i in range(1, N - 1):
        if H[i] > H[i - 1] and H[i] > H[i + 1]:
            prominence = min(H[i] - H[i - 1], H[i] - H[i + 1])
            if prominence > max_prominence:
                max_prominence = prominence
                index_of_max_prominence = i
    return index_of_max_prominence

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())
    H = list(map(int, input().strip().split()))

    # Trova l'indice del picco con la prominenza maggiore
    x = find_peak_with_max_prominence(N, H)

    print("Case #%d: " % test, end='')
    print(x)

sys.stdout.close()
