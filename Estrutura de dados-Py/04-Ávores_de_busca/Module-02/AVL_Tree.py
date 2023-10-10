class No:
    def __init__(self, key):
        self.key = key
        self.esquerda = None
        self.direita = None

    def setFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def rotacaoEsquerda(self):
        self.key, self.direita.key = self.direita.key, self.key
        old_esquerda = self.esquerda
        self.setFilhos(self.direita, self.direita.direita)
        self.esquerda.setFilhos(old_esquerda, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.key, self.esquerda.key = self.esquerda.key, self.key
        old_direita = self.direita
        self.setFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setFilhos(self.direita.direita, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executabalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.esquerda.rotacaoEsquerdaDireita()
        if bal < -1:
            if self.direita.balanco() > 0:
                self.direita.rotacaoEsquerda()
            else:
                self.direita.rotacaoDireitaEsquerda()

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()

        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()

        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_dir, prof_esq)

    def insere(self, data):
        if self.key is None:
            self.key = data
            return self.key
        elif self.key == data:
            return self.key
        elif data < self.key:
            if self.esquerda is None:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        elif data > self.key:
            if self.direita is None:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executabalanco()

    def buscar(self, data):
        bal = self.balanco()
        if bal > 1 or bal < -1:
            return -1
        else:
            if data == self.key:
                return 1
            elif data > self.key:
                if self.direita is None:
                    return 0
                else:
                    return self.direita.buscar(data)
            elif data < self.key:
                if self.esquerda is None:
                    return 0
                else:
                    return self.esquerda.buscar(data)

    # Método para deletar um nó com valor 'data'

    def delete(self, data):
        # Verifica se o nó atual está vazio
        if self.key is None:
            print("Valor não encontrado!")
            return None

        # Se 'data' é menor que a chave atual, tenta deletar na subárvore esquerda
        if data < self.key:
            if self.esquerda:
                self.esquerda = self.esquerda.delete(data)
        # Se 'data' é maior que a chave atual, tenta deletar na subárvore direita
        elif data > self.key:
            if self.direita:
                self.direita = self.direita.delete(data)
        else:
            # Nó a ser deletado encontrado
            if self.esquerda is None:
                return self.direita
            elif self.direita is None:
                return self.esquerda
            else:
                # Nó tem ambos os filhos
                # Encontra o nó mínimo na subárvore direita (sucessor)
                min_right_subtree = self.direita.find_min()
                self.key = min_right_subtree.key
                self.direita = self.direita.delete(min_right_subtree.key)
        # Reequilibra a árvore após a exclusão
        self.executabalanco()
        return self

    # Método para encontrar o nó com a menor chave na subárvore atual
    def find_min(self):
        current = self
        while current.esquerda:
            current = current.esquerda
        return current

    # In-Order
    def imprimirArvore(self, indent=0):
        if self.esquerda:
            self.esquerda.imprimirArvore(indent + 2)
        print(" " * indent + str(self.key))
        if self.direita:
            self.direita.imprimirArvore(indent + 2)


if __name__ == "__main__":
    print(30 * "-" + "Inserir" + 30 * "-")
    raiz = No(None)

    for data in [10, 5, 4, 3, 2, 1, 0]:
        raiz.insere(data)

    print(30 * "-" + "Buscar" + 30 * "-")
    # -1 = Tree not AVl
    # 0 = value notfound
    # 1 = value found
    for chave in [-50, 10, 30, 70, 100]:
        # Search value
        result = raiz.buscar(chave)
        if result == -1:
            print("Arvore não é AVL, está desbalanceada")
        elif result == 0:
            print("{} não encontrado".format(chave))
        elif result == 1:
            print("{} encontrado".format(chave))

    print(30 * "-" + "Remover" + 30 * "-")
    raiz.delete(3)
    for chave in [5, 10, 30, 70, 100]:
        # Search value
        result = raiz.buscar(chave)
        if result == -1:
            print("Arvore não é AVL, está desbalanceada")
        elif result == 0:
            print("{} não encontrado".format(chave))
        elif result == 1:
            print("{} encontrado".format(chave))

    print(30 * "-" + "Imprimi" + 30 * "-")
    # Print Tree
    raiz.imprimirArvore()
