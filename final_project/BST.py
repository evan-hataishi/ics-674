import random

class BST():

    root = None
    # Keep track of nodes by order of insertion
    nodes = []

    def __init__(self, data):
        self.insert_nodes(data)

    def __str__(self):
        return '\n'.join(self.in_order())

    def insert_nodes(self, data):
        for x in data:
            node = BST.TreeNode(x[0], x[1])
            self.nodes.append(node)
            if not self.root:
                self.root = node
            else:
                self.root.insert(node)

    def in_order(self):
        nodes = in_order(self.root, 0)
        return [str(x[0]) + "\tDepth: " + str(x[1]) for x in nodes]

    def traverse(self):
        traverse(self.root)

    def cost(self):
        return cost(self.root, 1)

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

def in_order(root, depth):
    if not root:
        return []
    left = in_order(root.left, depth+1)
    right = in_order(root.right, depth+1)
    return left + [(root, depth)] + right

def traverse(root):
    if not root:
        return
    traverse(root.left)
    print(root)
    traverse(root.right)

def cost(root, level):
    if not root:
        return 0
    left = cost(root.left, level+1)
    right = cost(root.right, level+1)
    return (root.freq * level) + left + right
