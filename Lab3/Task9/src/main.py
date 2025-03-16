from Lab2.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1  # Размер корневого поддерева в этом узле

def build_tree(N, nodes_data):
    nodes = {key: TreeNode(key) for key, _, _ in nodes_data}  # Использую dict для быстрого доступа

    for key, left, right in nodes_data:
        if left in nodes:
            nodes[key].left = nodes[left]
        if right in nodes:
            nodes[key].right = nodes[right]

    root = nodes[nodes_data[0][0]]  # Корень — это первый элемент в списке
    update_sizes(root)  # Обновить размер всего дерева
    return root

def update_sizes(node):
    if not node:
        return 0
    node.size = 1 + update_sizes(node.left) + update_sizes(node.right)
    return node.size

def delete_subtree(root, key):
    if not root:
        return root, 0

    if key < root.key:
        root.left, deleted_size = delete_subtree(root.left, key)
    elif key > root.key:
        root.right, deleted_size = delete_subtree(root.right, key)
    else:
        deleted_size = root.size
        return None, deleted_size  # Удалить все корневое поддерево в этом узле

    root.size -= deleted_size  # Обновить размер после удаления
    return root, deleted_size

def process_queries(root, queries):
    results = []
    for key in queries:
        root, deleted_size = delete_subtree(root, key)
        results.append(root.size if root else 0)  # Если все удалено, вернуть 0
    return results

def main():
    N, nodes_data, queries = read(PATH_INPUT, 9)
    root = build_tree(N, nodes_data)
    results = process_queries(root, queries)
    write(PATH_OUTPUT, results, 9)

if __name__ == "__main__":
    main()
