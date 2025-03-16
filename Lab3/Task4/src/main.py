import sys
from Lab3.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

sys.setrecursionlimit(200000)# Увеличиваем лимит рекурсии для больших графов

def topological_sort(n, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * (n + 1)
    order = []

    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        order.append(node)

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)

    return order[::-1]

def main():
    n, edges = read(PATH_INPUT, 4)
    results = topological_sort(n, edges)
    write(PATH_OUTPUT, results, 4)

if __name__ == "__main__":
    main()
