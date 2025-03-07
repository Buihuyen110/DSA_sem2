from Lab2.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

def height(node):
    return node.height if node else 0

def update_height(node):
    if node:
        node.height = max(height(node.left), height(node.right)) + 1

def balance_factor(node):
    return height(node.right) - height(node.left) if node else 0

def rotate_right(node):
    y = node.left
    node.left = y.right
    y.right = node
    update_height(node)
    update_height(y)
    return y

def rotate_left(node):
    y = node.right
    node.right = y.left
    y.left = node
    update_height(node)
    update_height(y)
    return y

def balance(node):
    if not node:
        return node
    bf = balance_factor(node)
    if bf > 1:
        if balance_factor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)
    if bf < -1:
        if balance_factor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
    return node

def find_max(node):
    current = node
    while current.right:
        current = current.right
    return current

def delete_node(root, key):
    # Удаление вершины
    if not root:
        return None
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Нашли вершину для удаления
        if not root.left and not root.right:  # Лист
            return None
        if not root.left:  # Нет левого ребёнка
            return root.right
        else:  # Есть оба ребёнка
            max_node = find_max(root.left)
            root.key = max_node.key
            root.left = delete_node(root.left, max_node.key)
    update_height(root)
    return balance(root)

def build_tree(nodes, index):
    # Построение дерева
    if index == 0 or index > len(nodes):
        return None
    key, left, right = nodes[index - 1]
    node = Node(key)
    node.left = build_tree(nodes, left)
    node.right = build_tree(nodes, right)
    update_height(node)
    return node

def collect_nodes(root, nodes_list):
    # Сбор оставшихся вершин
    if not root:
        return
    nodes_list.append(root)
    collect_nodes(root.left, nodes_list)
    collect_nodes(root.right, nodes_list)

def main():
    _, nodes, X = read(PATH_INPUT, 15)

    root = build_tree(nodes, 1)
    root = delete_node(root, X)
    nodes_list = []
    collect_nodes(root, nodes_list)

    # Присвоение новых индексов и подготовка вывода
    if not nodes_list:
        output = "0\n"
    else:
        node_to_index = {node: i + 1 for i, node in enumerate(nodes_list)}
        output = f"{len(nodes_list)}\n"
        for node in nodes_list:
            left_idx = node_to_index.get(node.left, 0)
            right_idx = node_to_index.get(node.right, 0)
            output += f"{node.key} {left_idx} {right_idx}\n"

    # Запись результата
    write(PATH_OUTPUT, output, 15)

if __name__ == "__main__":
    main()