# Arvores binarias são arvores nas quais cada nó pode ter no máximo dois filhos
# Arvore é um conjunto de nós, e cada nó é um objeto com uma chave e uma referência aos seus dois filhos (Esq, Dir).

class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


if __name__ == '__main__':
    raiz = NoArvore(55)

    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)

    raiz.direita.esquerda = NoArvore(65)
    raiz.direita.direita = NoArvore(85)
    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita = NoArvore(45)
