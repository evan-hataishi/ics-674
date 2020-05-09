import random
import math

class BST():

    root = None
    # Keep track of nodes by order of insertion
    nodes = None

    def __init__(self, data):
        self.nodes = []
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

    def crossover(a, b):
        a_data = a.raw_data()
        b_data = b.raw_data()
        child_data = BST.merge_data(a_data, b_data)
        return BST(child_data)

    def raw_data(self):
        data = []
        for node in self.nodes:
            data.append((node.key, node.freq))
        return data

    def merge_data(a, b):
        d = {}
        for i, item in enumerate(a):
            d[item] = [i, None]
        for i, item in enumerate(b):
            d[item][1] = i
        tmp = [None] * len(a)
        for k, v in d.items():
            index = random.choice(v)
            if tmp[index]:
                tmp[index].append(k)
            else:
                tmp[index] = [k]
        return BST.flatten(tmp)

    def flatten(l):
        res = []
        for x in l:
            if x:
                res += x
        return res

    def mutate(self):
        prob = random.uniform(0,1)
        if prob <= 0.2:
            tmp = self.raw_data()
            random.shuffle(tmp)
            return BST(tmp)
        return self

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

# https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
def optBSTCost(keys, freq, n):
    cost = [[0 for x in range(n)]
               for y in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
    for L in range(2, n + 1):
        for i in range(n - L + 2):
            j = i + L - 1
            if i >= n or j >= n:
                break
            cost[i][j] = math.inf

            for r in range(i, j + 1):
                c = 0
                if (r > i):
                    c += cost[i][r - 1]
                if (r < j):
                    c += cost[r + 1][j]
                c += sum(freq, i, j)
                if (c < cost[i][j]):
                    cost[i][j] = c
    return cost[0][n - 1]

def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s
