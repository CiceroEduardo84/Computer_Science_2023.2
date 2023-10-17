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

        i = 0  # Contador
        # Irá percorer os nós da minha árvore
        while i < len(x.chaves) and value > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and value == x.chaves[i]:  # encontrado o valor
            return x, i
        if x.folha:  # Não encontrado o valor
            return None
        return self.buscar(value, x.filhos[i])  # Procura nos nós filhos

    # Dividir pagina
    def split_children(self, x, i):
        t = 1
        y = x.filhos[i]
        z = BTree(folha=y.folha)
        x.filhos.insert(i + 1, z)
        x.chaves.insert(i, y.chaves[t - 1])
        z.chaves = y.chaves[t:]
        y.chaves = y.chaves[:t - 1]

        if not y.folha:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t]

    # Inserção em arvores B, com a ordem
    def insert(self, value, order):
        root = self

        # Checar se minha lista de chaves respeita a propriedade ordem
        if len(self.chaves) == order:
            temp = BTree(folha=False)
            self = temp
            temp.filhos.append(root)
            self.split_children(temp, 0)
            self.insert_non_full(temp, value, order)

        else:
            self.insert_non_full(root, value, order)

    def insert_non_full(self, k, value, order):
        i = len(k.chaves) - 1
        if k.folha:  # Inserir caso seja folha
            while i >= 0 and value < k.chaves[i]:
                i -= 1
            k.chaves.insert(i + 1, value)
        else:  # senão ele quebra minha arvore e encaixa o novo valor
            while i >= 0 and value < k.chaves[i]:
                i -= 1
            i += 1
            if len(k.filhos[i].chaves) == order:
                self.split_children(k, i)
                if value > k.chaves[i]:
                    i += 1
            self.insert_non_full(k.filhos[i], value, order)

    # Remover elemento do meu nó
    def remove(self, value, order, x=None):
        if x is None:
            x = self

        i = 0  # Contador
        # Irá percorer os nós da minha árvore
        while i < len(x.chaves) and value > x.chaves[i]:
            i += 1

        if i < len(x.chaves) and value == x.chaves[i]:  # encontrado o valor
            return x, i
        if x.folha:  # Não encontrado o valor
            return None
        return self.remove(value, x.filhos[i])  # Procura nos nós filhos
        
        
if __name__ == "__main__":
    btree = BTree()
    order = 2
    keys = [10, 39, 45, 25, 15, 10]
    for key in keys:
        btree.insert(key, order)

    print(btree.search(80))
