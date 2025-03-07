from Lab2.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def build_tree(nodes, index):
    if index == 0:
        return None
    key, left, right = nodes[index - 1]
    return (key, build_tree(nodes, left), build_tree(nodes, right))

def tree_height(root):
    if not root:
        return 0
    _, left, right = root
    return 1 + max(tree_height(left), tree_height(right))

def main():
    n, nodes = read(PATH_INPUT, 8)
    if n == 0:
        height = 0
    else:
        root = build_tree(nodes, 1)
        height = tree_height(root)

    write(PATH_OUTPUT, height, 8)

if __name__ == "__main__":
    main()
