from Lab3.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def dfs(v, graph, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

def find_connected_components(n, m, edges):
    # Создаём список смежности для графа
    graph = [[] for _ in range(n)]

    for edge in edges:
        u, v = edge
        graph[u - 1].append(v - 1)  # Индексы вершин начинаются с 0
        graph[v - 1].append(u - 1)

    visited = [False] * n
    component_count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited)
            component_count += 1

    return component_count

def main():
    n, m, edges = read(PATH_INPUT, 2)
    results = find_connected_components(n, m, edges)
    write(PATH_OUTPUT, results, 2)

if __name__ == "__main__":
    main()
