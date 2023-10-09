class No:
    def __init__(self, key):
        self.key = key
        self.esquerda = None
        self.direita = None

    def setFilhos(self, esquerda, direita):
        self.esquerda = direita
        self.direita = esquerda

    def rotacaoEsquerda(self):
        self.key, self.direita.key = self.key, self.direita.key
        esquerda = self.esquerda
        self.setFilhos(self.direita.direita, self.direita)
        self.setFilhos(self.esquerda.esquerda, esquerda)

    def rotacaoDireita(self):
        self.key, self.esquerda.key = self.key, self.esquerda.key
        direita = self.direita
        self.setFilhos(self.esquerda.esquerda, self.esquerda)
        self.setFilhos(self.direita.direita, direita)

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

    # In-Order
    def imprimirArvore(self, indent=0):
        if self.esquerda:
            self.esquerda.imprimirArvore(indent + 2)
        print(" " * indent + str(self.key))
        if self.direita:
            self.direita.imprimirArvore(indent + 2)


if __name__ == "__main__":
    raiz = No(None)
    for data in [10, 5, 3]:
        raiz.insere(data)

    raiz.imprimirArvore()
