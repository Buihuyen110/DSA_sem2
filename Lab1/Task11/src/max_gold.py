from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def max_gold(W, n, weights):
    if W == 0 or n == 0:
        return 0
    # Создаем двумерный массив dp размером (n+1) x (W+1)
    # dp[i][w] будет хранить максимальный вес золота, который можно набрать
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        # Перебираем все возможные вместимости сумки от 1 до W
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max( dp[i-1][w], dp[i-1][w-weights[i-1]] + weights[i-1])

            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]

def task11():
    W, n, weights = read(PATH_INPUT, 11)
    result = max_gold(W, n, weights)
    write(PATH_OUTPUT, result, 11)

if __name__ == "__main__":
    task11()