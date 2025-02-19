from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def count_palindromes(N, K, S):
    count = 0
    changes = [[0] * N for _ in range(N)]

    for length in range(1, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1

            if i == j:
                changes[i][j] = 0

            elif i + 1 == j:
                changes[i][j] = 0 if S[i] == S[j] else 1

            else:
                changes[i][j] = changes[i + 1][j - 1] + (0 if S[i] == S[j] else 1)

            if changes[i][j] <= K:
                count += 1

    return count

def task20():
    N, K, S = read(PATH_INPUT, 20)
    result = count_palindromes(N, K, S)
    write(PATH_OUTPUT, result, 20)

if __name__ == "__main__":
    task20()