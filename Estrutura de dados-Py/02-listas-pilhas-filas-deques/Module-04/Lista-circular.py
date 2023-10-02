class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None

# Lista circular


def insereCircular(novoNo):
    global inicioLista
    global finalLista
    if inicioLista == None:  # lista vazia
        inicioLista = novoNo
        finalLista = novoNo
        novoNo.proximo = novoNo
    else:
        finalLista.proximo = novoNo  # insere o nó
        finalLista = novoNo  # atualiza ponteiros
        finalLista.proximo = inicioLista


def buscarAnterior(self, K):
    noAtual = self.cabeca
    if noAtual.chave == K:
        return noAtual
    while noAtual.proximo != None:
        noAtual = noAtual.proximo
    # Passe para o próximo nó
        if noAtual.chave == K:
            return noAtual
    # Chave encontrada
    return None


def removeCircular(k):
    global inicioLista
    global finalLista
    noAnterior = buscarAnterior(k)
    if noAnterior == None:
        return None
    if finalLista == inicioLista:
        lista = None
        return 0
    if noAnterior == finalLista:
        finalLista.proximo = inicioLista.proximo
        inicioLista = finalLista.proximo
    elif noAnterior.proximo == finalLista:
        finalLista = noAnterior
        noAnterior.proximo = inicioLista
    else:
        noAtual = noAnterior.proximo
        noAnterior.proximo = noAtual.proximo
    return 0


