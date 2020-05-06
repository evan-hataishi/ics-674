import random

class TreeNode():

    key = 0
    freq = 0
    left = None
    right = None

    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        return "Key: " + str(self.key) + "\tFrequency: " + str(self.freq)

    def insert(self, node):
        if self.key > node.key and self.left:
            self.left.insert(node)
        elif self.key > node.key and not self.left:
            self.left = node
        elif self.key <= node.key and self.right:
            self.right.insert(node)
        else:
            self.right = node

def traverse(root):
    if not root:
        return
    traverse(root.left)
    print(root)
    traverse(root.right)
