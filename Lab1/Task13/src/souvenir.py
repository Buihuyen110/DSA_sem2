from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def partition_subsets(souvenirs):
    total = sum(souvenirs)
    if total % 3 != 0:
        return 0

    target = total // 3
    n = len(souvenirs)

    # Создать таблицу DP
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True  # Можно получить сумму 0, ничего не выбирая

    # Просмотр каждого элемента
    for i in range(1, n + 1):
        for j in range(target, souvenirs[i - 1] - 1, -1):  # Итерация в обратном порядке, чтобы избежать перезаписи
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - souvenirs[i - 1]]

    # Можно ли разделить тест на 3 части?
    return 1 if dp[n][target] else 0

def task13():
    souvenirs = read(PATH_INPUT, 13)
    result = partition_subsets(souvenirs)
    write(PATH_OUTPUT, result, 13)

if __name__ == "__main__":
    task13()