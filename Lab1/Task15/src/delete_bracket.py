from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def delete_bracket(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    pair = {')': '(', ']': '[', '}': '{'}

    # Заполняем DP
    for length in range(2, n + 1):  # Длина подстроки
        for i in range(n - length + 1):
            j = i + length - 1
            if s[j] in pair and i < j and s[i] == pair[s[j]]:  # Если s[i] и s[j] образуют пару
                dp[i][j] = dp[i + 1][j - 1] + 2
            for k in range(i, j):  # Разбиение на две части
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])

    # Восстановление ответа
    def get_sequence(i, j):
        if i > j:
            return ""
        if dp[i][j] == 0:
            return ""
        if s[j] in pair and i < j and s[i] == pair[s[j]] and dp[i][j] == dp[i + 1][j - 1] + 2:
            return s[i] + get_sequence(i + 1, j - 1) + s[j]
        for k in range(i, j):
            if dp[i][j] == dp[i][k] + dp[k + 1][j]:
                return get_sequence(i, k) + get_sequence(k + 1, j)
        return ""

    return get_sequence(0, n - 1)

def task15():
    s = read(PATH_INPUT, 15)
    result = delete_bracket(s)
    write(PATH_OUTPUT, result, 15)

if __name__ == "__main__":
    task15()