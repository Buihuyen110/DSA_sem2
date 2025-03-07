from Lab2.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.size = 1  # Размер корневого поддерева в этом узле
        self.left = None
        self.right = None


def update_size(node):
    """Обновить размер узла на основе поддерева."""
    if node:
        left_size = node.left.size if node.left else 0
        right_size = node.right.size if node.right else 0
        node.size = 1 + left_size + right_size


def insert(root, x):
    """Вставить значение x в дерево BST и обновить размер."""
    if root is None:
        return TreeNode(x)

    if x < root.value:
        root.left = insert(root.left, x)
    elif x > root.value:
        root.right = insert(root.right, x)
    # Если x уже существует, не вставлять снова

    update_size(root)  # Обновить размер после добавления нового узла
    return root


def kth_smallest(root, k):
    """Найти k-й наименьший элемент в BST."""
    if not root:
        return None

    left_size = root.left.size if root.left else 0  # Количество узлов слева

    if k == left_size + 1:
        return root.value  # Текущий узел — это k-й элемент
    elif k <= left_size:
        return kth_smallest(root.left, k)  # Найти слева
    else:
        return kth_smallest(root.right, k - left_size - 1)  # Отрегулируйте индекс и найдите нужный


def process_queries(queries):
    root = None
    results = []
    for operation, value in queries:
        if operation == '+':
            root = insert(root, value)
        elif operation == '?':
            results.append(kth_smallest(root, value))
    return results


def main():
    queries = read(PATH_INPUT, 4)
    results = process_queries(queries)
    write(PATH_OUTPUT, results, 4)


if __name__ == "__main__":
    main()
