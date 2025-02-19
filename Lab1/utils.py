import time
import tracemalloc
import functools

def time_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(2):
            tracemalloc.start()
            start = time.perf_counter()

            result = func(*args, **kwargs)

            exec_time = time.perf_counter() - start
            _, peak_mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            if i == 1:
                print(f'\nTest Case: {func.__name__}')
                print(f'Execution Time = {exec_time:.8f} s, Memory Usage = {peak_mem / 1024:.4f} KB')

        return result

    return wrapper

def read(file_path, task):
    with open(file_path, 'r') as f:
        if task == 2:
            d = int(f.readline().strip())
            m = int(f.readline().strip())
            n = int(f.readline().strip())
            stops = list(map(int, f.readline().strip().split()))
            return d, m, stops

        elif task == 7:
           K, n = list(map(int, f.readline().strip(). split()))
           repair_time = list(map(int, f.readline().strip(). split()))
           return K, repair_time

        elif task == 11:
            W, n = list(map(int, f.readline().strip().split()))
            weight_golds = list(map(int, f.readline().strip().split()))
            return W, n, weight_golds

        elif task == 14:
            exp = f.readline()
            return exp

        elif task == 20:
            N, K = list(map(int, f.readline().strip().split()))
            S = f.readline()
            return N, K, S

        elif task == 17:
            N = int(f.readline())
            return N

        elif task == 15:
            s = f.readline()
            return s

        else:
            n = int(f.readline().strip())
            souvenirs = list(map(int, f.readline().strip().split()))
            return souvenirs


def write(file_path, result, task):
    with open(file_path, 'w', encoding='utf-8') as f:
        number = [2, 13, 15]
        if task in number:
            f.write(str(result) + '\n')

        else:
            f.write(str(result))




