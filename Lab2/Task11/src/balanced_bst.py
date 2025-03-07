import sys
from Lab2.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def update_height(node):
    if node:
        node.height = max(height(node.left), height(node.right)) + 1

def balance_factor(node):
    return height(node.right) - height(node.left) if node else 0

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    update_height(x)
    update_height(y)
    return y

def balance(node):
    update_height(node)
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

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return balance(node)

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete(node, key):
    if not node:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        min_larger_node = find_min(node.right)
        node.key = min_larger_node.key
        node.right = delete(node.right, min_larger_node.key)
    return balance(node)

def exists(node, key):
    if not node:
        return "false"
    if key == node.key:
        return "true"
    elif key < node.key:
        return exists(node.left, key)
    else:
        return exists(node.right, key)

def next(node, key):
    successor = None
    while node:
        if node.key > key:
            successor = node
            node = node.left
        else:
            node = node.right
    return successor.key if successor else "none"

def prev(node, key):
    predecessor = None
    while node:
        if node.key < key:
            predecessor = node
            node = node.right
        else:
            node = node.left
    return predecessor.key if predecessor else "none"

def main():
    root = None
    input_data = read(PATH_INPUT, 11)
    output = []
    for line in input_data:
        parts = line.split()
        command, value = parts[0], int(parts[1])
        if command == "insert":
            root = insert(root, value)
        elif command == "delete":
            root = delete(root, value)
        elif command == "exists":
            output.append(exists(root, value))
        elif command == "next":
            output.append(str(next(root, value)))
        elif command == "prev":
            output.append(str(prev(root, value)))
    write(PATH_OUTPUT, output, 11)

if __name__ == "__main__":
    main()

