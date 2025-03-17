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
            n, m = map(int, f.readline().split())
            edges = [tuple(map(int, f.readline().split())) for _ in range(m)]
            return n, m, edges

        elif task == 4:
            n, m = map(int, f.readline().split())
            edges = [tuple(map(int, line.split())) for line in f]
            return n, edges

        elif task == 9:
           n, m = map(int, f.readline().split())
           edges = []
           for _ in range(m):
               u, v, w = map(int, f.readline().split())
               edges.append((u, v, w))
           print(edges)
           return n, edges

        else:
            N, M = map(int, f.readline().split())
            garden = [list(f.readline().strip()) for _ in range(N)]
            Qx, Qy, L = map(int, f.readline().split())
            musketteers = [tuple(map(int, f.readline().split())) for _ in range(4)]
            print(N, M, garden, (Qx, Qy, L), musketteers)
            return N, M, garden, (Qx, Qy, L), musketteers


def write(file_path, result, task):
    with open(file_path, 'w', encoding='utf-8') as f:
        if task == 4:
            f.write(" ".join(map(str, result)) + "\n")

        else:
            f.write(str(result) + '\n')




