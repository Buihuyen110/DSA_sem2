from Lab2.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def is_bst_util(nodes, index, min_val, max_val):
   if index == 0:
       return True
   key, left, right = nodes[index - 1]
   if not (min_val < key < max_val):
       return False
   return is_bst_util(nodes, left, min_val, key) and is_bst_util(nodes, right, key, max_val)

def is_bst(n, nodes):
   if n == 0:
       return "YES"
   return "YES" if is_bst_util(nodes, 1, float('-inf'), float('inf')) else "NO"

def main():
   n, nodes = read(PATH_INPUT, 10)
   result = is_bst(n, nodes)

   write(PATH_OUTPUT, result, 10)

if __name__ == "__main__":
   main()


