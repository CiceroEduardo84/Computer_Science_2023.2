class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


def BuscaBST(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return BuscaBST(raiz.direita, chave)
    else:
        return BuscaBST(raiz.esquerda, chave)


def InserirBST(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    elif raiz.chave == chave.chave:
        return raiz
    elif raiz.chave < chave.chave:
        if raiz.direita is None:
            raiz.direita = chave
        else:
            raiz.direita = InserirBST(raiz.direita, chave)
    elif raiz.chave > chave.chave:
        if raiz.esquerda is None:
            raiz.esquerda = chave
        else:
            raiz.esquerda = InserirBST(raiz.esquerda, chave)
    return raiz


def DeleteBST(raiz, chave):
    if raiz is None:
        return raiz
    if chave < raiz.chave:
        raiz.esquerda = DeleteBST(raiz.esquerda, chave)
    elif chave > raiz.chave:
        raiz.direita = DeleteBST(raiz.direita, chave)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        temp = ValorNo(raiz.direita)
        raiz.chave = temp.chave
        raiz.direita = DeleteBST(raiz.direita, temp.chave)
    return raiz


def ValorNo(no):
    atual = no
    while (atual.esquerda is not None):
        atual = atual.esquerda
    return atual


cont = [10]


def ImprimeArvoreRecurs(raiz, nivel):
    global cont

    if raiz is None:
        return
    nivel += 1
    ImprimeArvoreRecurs(raiz.direita, nivel)
    for i in range(cont[0], nivel):
        print(" ", end=" ")
    print(raiz.chave)
    ImprimeArvoreRecurs(raiz.esquerda, nivel)


def ImprimeArvore(raiz):
    global cont
    cont[0] = 0
    ImprimeArvoreRecurs(raiz, 0)

# Percurso Prá-Ordem
def PreFixa(raiz):
    if raiz:
        print(raiz.chave)
        PreFixa(raiz.esquerda)
        PreFixa(raiz.direita)

# Percurso em Ordem(In-Order)
def InFixa(raiz):
    if raiz:
        InFixa(raiz.esquerda)
        print(raiz.chave)
        InFixa(raiz.direita)

# Percurso Pós-Ordem
def PosFixa(raiz):
    if raiz:
        PosFixa(raiz.esquerda)
        PosFixa(raiz.direita)
        print(raiz.chave)


if __name__ == '__main__':
    raiz = NoArvore("+")
    raiz.direita = NoArvore("*")
    raiz.esquerda = NoArvore(1)
    
    raiz.direita.esquerda = NoArvore(3)
    raiz.direita.direita = NoArvore(4)

    print(30 * "-" + "Imprimir Árvore" + 30 * "-")
    ImprimeArvore(raiz)

    print(30 * "-" + "Percurso em Pré-fixa" + 30 * "-")
    PreFixa(raiz)

    print(30 * "-" + "Percurso em In-fixa" + 30 * "-")
    InFixa(raiz)

    print(30 * "-" + "Percurso em Pós-fixa" + 30 * "-")
    PosFixa(raiz)
