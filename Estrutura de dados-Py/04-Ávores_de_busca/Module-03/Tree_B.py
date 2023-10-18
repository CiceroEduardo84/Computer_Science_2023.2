class BTreeNode:
    def __init__(self, folha=True):
        self.folha = folha
        self.chaves = []
        self.filhos = []


class BTree:
    def __init__(self):
        self.root = BTreeNode()

    def search(self, value, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.chaves) and value > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and value == x.chaves[i]:
            return x, i
        if x.folha:
            return None
        return self.search(value, x.filhos[i])

    def split_children(self, x, i):
        t = 1
        y = x.filhos[i]
        z = BTreeNode(folha=y.folha)
        x.filhos.insert(i + 1, z)
        x.chaves.insert(i, y.chaves[t - 1])
        z.chaves = y.chaves[t:]
        y.chaves = y.chaves[:t - 1]

        if not y.folha:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t]

    def insert(self, value, order):
        root = self.root

        if len(root.chaves) == order:
            temp = BTreeNode(folha=False)
            self.root = temp
            temp.filhos.append(root)
            self.split_children(temp, 0)
            self.insert_non_full(temp, value, order)

        else:
            self.insert_non_full(root, value, order)

    def insert_non_full(self, k, value, order):
        i = len(k.chaves) - 1
        if k.folha:
            while i >= 0 and value < k.chaves[i]:
                i -= 1
            k.chaves.insert(i + 1, value)
        else:
            while i >= 0 and value < k.chaves[i]:
                i -= 1
            i += 1
            if len(k.filhos[i].chaves) == order:
                self.split_children(k, i)
                if value > k.chaves[i]:
                    i += 1
            self.insert_non_full(k.filhos[i], value, order)

    def remove(self, value, order, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.chaves) and value > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and value == x.chaves[i]:
            return self.delete_non_full(x, value, order)
        
        if x.folha:
            return None
        return self.remove(value, order, x.filhos[i])

    def delete_non_full(self, k, value, order):
        # i = len(k.chaves) - 1
        if k.folha:
            k.chaves.remove(value)
        else:
            i += 1
            if len(k.filhos[i].chaves) == order:
                self.split_children(k, i)
                if value > k.chaves[i]:
                    i += 1


if __name__ == "__main__":
    btree = BTree()
    order = 2
    keys = [3, 7, 1, 5, 8, 2, 6, 4]
    
    for key in keys:
        btree.insert(key, order)
    
    btree.remove(4,order)
    
    for key in keys:
        print(btree.search(key))
