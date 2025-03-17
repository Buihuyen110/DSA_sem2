from Lab3.utils import read, write
from collections import deque

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def bfs(start_x, start_y, qx, qy, garden, n, m):
    queue = deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (qx, qy):
            return dist
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and garden[nx][ny] == '0':
                visited.add((nx, ny))
            queue.append((nx, ny, dist + 1))

    return float('inf')

def main():
    n, m, garden, (qx, qy, L), musketeers = read(PATH_INPUT, 15)

    # Переключиться на индекс, начинающийся с 0
    qx, qy = qx - 1, qy - 1
    musketeers = [(x - 1, y - 1, p) for x, y, p in musketeers]

    # Считаем подвески, которые успеют к королеве
    total_pendants = 0
    for Ax, Ay, Pa in musketeers:
        min_time = bfs(Ax, Ay, qx, qy, garden, n, m)  # Приводим к 0-индексации
        if min_time <= L:
            total_pendants += Pa

    # Запись результата
    write(PATH_OUTPUT, total_pendants, 15)

if __name__ == "__main__":
    main()