from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

MOD = 10**9

# Возможные ходы коня
moves = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}

def phone_numbers(N):
    if N == 1:
        return 8  # Все цифры, кроме 0 и 8

    # DP таблица
    dp = [[0] * 10 for _ in range(N + 1)]

    # Начальная инициализация
    for d in range(10):
        dp[1][d] = 1 if d != 0 and d != 8 else 0

    # Заполнение DP
    for i in range(2, N + 1):
        for d in range(10):
            dp[i][d] = sum(dp[i - 1][prev] for prev in moves[d]) % MOD

    # Ответ — сумма всех допустимых окончаний
    return sum(dp[N][d] for d in range(10)) % MOD

def task17():
    N = read(PATH_INPUT, 17)
    result = phone_numbers(N)
    write(PATH_OUTPUT, result, 17)

if __name__ == "__main__":
    task17()