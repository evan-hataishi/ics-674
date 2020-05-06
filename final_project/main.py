from BST import *
import random

def main():
    root = TreeNode(1, 0)
    keys = [x for x in range(2, 50)]
    random.shuffle(keys)
    for key in keys:
        root.insert(TreeNode(key, 0))
    traverse(root)

if __name__ == '__main__':
    main()
