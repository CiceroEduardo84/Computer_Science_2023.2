
class TreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self):
        self.root = TreeNode()

    def search(self, k, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:
            return x, i

        if x.leaf:
            return None

        return self.search(k, x.children[i])

    def split_child(self, x, i):
        t = 1  # A ordem t=3 implica que t-1=2
        y = x.children[i]
        z = TreeNode(leaf=y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def insert(self, k):
        root = self.root
        if len(root.keys) == 2:
            temp = TreeNode(leaf=False)
            self.root = temp
            temp.children.append(root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.keys.insert(i + 1, k)
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == 2:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def display(self, x=None, level=0):
        if x is None:
            x = self.root

        print("Level", level, ":", x.keys)

        if not x.leaf:
            level += 1
            for child in x.children:
                self.display(child, level)


# Exemplo de uso
b_tree = BTree()
keys = [3, 7, 1, 5, 8, 2, 6, 4]

for key in keys:
    b_tree.insert(key)

print("Árvore B:")
b_tree.display()