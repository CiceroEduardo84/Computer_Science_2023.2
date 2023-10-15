# Criação da arvore B
class BTree:
    # Definindo minha folhas, chaves/nós e filhos
    def __init__(self, folha=True):
        self.folha = folha
        self.chaves = []
        self.filhos = []

    # Busca em arvores B
    def search(self, value, x=None):
        if x is None:
            x = self

        i = 0
        while i < len(x.chaves) and value > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and value == x.chaves[i]:
            return "Econtrado"
        if x.folha:
            return None
        return self.buscar(value, x.filhos[i])

    # Inserção em arvores B, com a ordem
    def insert(self, value, order):
        i = 0
        while i < len(self.chaves) and value > self.chaves[i]:
            i += 1
        if i < len(self.chaves) and value == self.chaves[i]:
            return "Valor já existente!"

        if len(self.chaves) == order:
            temp = BTree(folha=False)
            self = temp
            temp.filhos.append(self)

        else:
            self.insert_non_full(self, value)

    # def insert_non_full(self, value):
    #     i = 

if __name__ == "__main__":
    btree = BTree()
    order = 5
    keys = [10]
    for key in keys:
        btree.inserir(key, order)

    print(btree.buscar(80))
