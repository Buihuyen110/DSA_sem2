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
        if task == 1:
            p = f.readline().strip()
            t = f.readline().strip()
            return p, t

        elif task == 6:
            s = f.readline().strip()
            return s

        else:
            lines = f.readlines()
            return lines


def write(file_path, result, task):
    with open(file_path, 'w', encoding='utf-8') as f:
        if task == 1:
            f.write(f"{len(result)}\n")
            if result:
                f.write(" ".join(map(str, result)) + "\n")

        elif task == 6:
            f.write(" ".join(map(str, result[1:])) + "\n")

        else:
            f.write("\n".join(result) + "\n")






