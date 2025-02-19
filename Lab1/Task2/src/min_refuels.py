from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def min_refuels(d, m, stops):
    # Добавляем начальную и конечную точки
    stops = [0] + stops + [d]
    refuels = 0
    last_refuel_position = 0

    for i in range(1, len(stops)):
        # Проверяем расстояние до следующей остановки
        if stops[i] - stops[i - 1] > m:
            return -1

        if stops[i] - last_refuel_position > m:
            last_refuel_position = stops[i - 1]
            refuels += 1

            # Проверяем снова возможность добраться до следующей остановки
            if stops[i] - last_refuel_position > m:
                return -1

    return refuels

def task2():
    d, m, stops = read(PATH_INPUT, 2)
    result = min_refuels(d, m, stops)
    write(PATH_OUTPUT, result, 2)

if __name__ == "__main__":
    task2()