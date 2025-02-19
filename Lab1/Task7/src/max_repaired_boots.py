from Lab1.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def max_repaired_boots(K, repair_time):
    repair_time.sort()

    if sum(repair_time) <= K:
        return len(repair_time)

    total_time = 0
    repaired = 0

    for time in repair_time:
        if total_time + time <= K:
            total_time += time
            repaired += 1

        else:
            break

    return repaired

def task7():
     K, repair_time = read(PATH_INPUT, 7)
     result = max_repaired_boots(K, repair_time)
     write(PATH_OUTPUT, result, 7)

if __name__ == "__main__":
    task7()