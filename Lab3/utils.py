import time
import tracemalloc
import functools
from os.path import split


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
        if task == 4:
            queries = []
            for line in f:
                query = line.strip().split()
                if query[0] == '+':
                    queries.append(('+', int(query[1])))
                elif query[0] == '?':
                    queries.append(('?', int(query[1])))
            return queries

        elif task == 8 or task == 10:
            n = int(f.readline().strip())
            nodes = []
            for _ in range(n):
                nodes.append(list(map(int, f.readline().split())))

            return n, nodes

        elif task == 9:
           N = int(f.readline())
           nodes_data = [list(map(int, f.readline().split())) for _ in range(N)]
           M = int(f.readline())
           queries = list(map(int, f.readline().strip().split()))
           return N, nodes_data, queries

        elif task == 11:
            input_data = f.read().splitlines()
            return input_data

        else:
            lines = f.readlines()
            N = int(lines[0].strip())
            nodes = []
            for i in range(N):
                key, left, right = map(int, lines[i + 1].strip().split())
                nodes.append((key, left, right))
            X = int(lines[N + 1].strip())
            return N, nodes, X


def write(file_path, result, task):
    with open(file_path, 'w', encoding='utf-8') as f:
        if task in [4, 9]:
            for i in result:
                f.write(f"{i}\n")

        elif task == 8:
            f.write(str(result) + '\n')

        elif task == 10:
            f.write(result + '\n')

        elif task == 11:
            f.write('\n'.join(result) + '\n')

        elif task == 15:
            f.write(result.strip())





