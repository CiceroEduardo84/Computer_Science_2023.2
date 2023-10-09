class No:
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

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
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.setaFilhos(self.direita, self.direita.direita)
        self.esquerda.setaFilhos(old_esquerda, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.setaFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setaFilhos(self.direita.direita, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def insere(self, data):
      if self.data is None:
        self.data = data
        return self.data
      elif self.data == data:
        return self.data
      else:
        if data < self.data:
            if self.esquerda is None:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        elif data > self.data:
            if self.direita is None:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executaBalanco()

    def imprimeArvore(self, indent = 0):
        if self.esquerda:
            self.esquerda.imprimeArvore(indent + 2)
        print (" " * indent + str(self.data))
        if self.direita:
            self.direita.imprimeArvore(indent + 2)

if __name__=="__main__":
    raiz = No(None)
    for data in [10,5,3]:
        raiz.insere(data)

    raiz.imprimeArvore()