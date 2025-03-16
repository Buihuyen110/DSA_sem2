from Lab3.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def bellman_ford(n, edges):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return 1

    return 0

def main():
    n, edges = read(PATH_INPUT, 9)
    result = bellman_ford(n, edges)
    write(PATH_OUTPUT, result, 9)

if __name__ == "__main__":
    main()
