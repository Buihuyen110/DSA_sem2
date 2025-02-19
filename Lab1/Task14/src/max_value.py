import re
from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    return 0

def max_value(exp):

    # Используем регулярное выражение для разделения чисел и операторов
    tokens = re.findall(r'\-?\d+|\+|\-|\*|\/|\(|\)', exp)

    #Проверяем корректность выражения
    if not tokens:
        raise ValueError("Invalid expression: empty or no valid tokens")

    # Если выражение содержит только одно число
    if len(tokens) == 1 and tokens[0].lstrip('-').isdigit():
        return int(tokens[0])

    # Преобразовать токены в список чисел и операторов
    digits = []
    operators = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            digits.append(int(token))
        elif token in "+-*/":
            operators.append(token)

    if len(operators) != len(digits) - 1:
        raise ValueError("Invalid expression: mismatch between numbers and operators")

    n = len(digits)
    # Инициализируем таблицу для хранения максимальных и минимальных значений
    min_val = [[0] * n for _ in range(n)]
    max_val = [[0] * n for _ in range(n)]

    for i in range(n):
        min_val[i][i] = digits[i]
        max_val[i][i] = digits[i]

    # Перебрать все подпоследовательности
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val[i][j], max_val[i][j] = float('inf'), float('-inf')

            for k in range(i, j):
                if k >= len(operators):  # Избегаем доступа к ошибкам вне массива
                    continue

                op = operators[k]
                a = evaluate(max_val[i][k], max_val[k + 1][j], op)
                b = evaluate(max_val[i][k], min_val[k + 1][j], op)
                c = evaluate(min_val[i][k], max_val[k + 1][j], op)
                d = evaluate(min_val[i][k], min_val[k + 1][j], op)

                # Обновить минимальные и максимальные значения
                min_val[i][j] = min(min_val[i][j], a, b, c, d)
                max_val[i][j] = max(max_val[i][j], a, b, c, d)

    return max_val[0][n - 1]

def task14():
    expression = read(PATH_INPUT, 14)
    result = max_value(expression)
    write(PATH_OUTPUT, result, 14)

if __name__ == "__main__":
    task14()