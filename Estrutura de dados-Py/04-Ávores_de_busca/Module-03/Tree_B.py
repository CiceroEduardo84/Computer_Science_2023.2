class BTree:
    def __init__(self, folha=True):
        self.folha = folha
        self.chaves = []
        self.filhos = []

    def inserir(self, value, order):
        if len(self.chaves) is 0:
            self.chaves.append(value)

    def buscar(self, value, x = None):
        if x is None:
          x = self

        i = 0
        while i < len(x.chaves) and value > x.chaves[i]:
            i += 1
            
        if i<len(x.chaves) and value == x.chaves[i]:
            return x,i
        if x.folha:
          return None
        return self.buscar(value,x.filhos[i])

if __name__ == "__main__":
    btree = BTree()
    order = 3
    keys = [10]
    for key in keys:
        btree.inserir(key, order)

