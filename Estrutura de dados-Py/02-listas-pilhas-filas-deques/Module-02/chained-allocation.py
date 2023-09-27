# Nó
class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

# Lista encadeada


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def print(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo

    # Código Busca

    # Tratamento do caso: nó buscado é o inicial
    # Tratamento do caso: nó não encontrado

    # Complexidade: O(n)

    def busca(self, K):
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
        # have não encontrada

    # Codigo de inserção

    # Inserção inicio
    # Inserção Final (variável ou percurso)

    # Complexidade: O(1) caso geral
    # O(n) caso ordenada -> limitada pela busca

    def insereInicio(self, novoNo):
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo

    def insereFinal(self, novoNo):
        noAtual = self.cabeca
        if noAtual:
            while noAtual.proximo:
                noAtual = noAtual.proximo
            noAtual.proximo = novoNo
        else:
            self.cabeca = novoNo

    def insereOrdenada(self, novoNo):
        noAtual = self.cabeca
        if noAtual.chave > novoNo.chave:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo
            return 0
        if noAtual.proximo != None:
            while (noAtual.chave < novoNo.chave):
                if (noAtual.proximo == None):
                    noAtual.proximo = novoNo
                    return 0
                noAnterior = noAtual
                noAtual = noAtual.proximo
        novoNo.proximo = noAtual
        noAnterior.proximo = novoNo

    # Código de remoção

    # Busca pela chave K para remover
    # 2 etapas: busca e remoção

    # Complexidade: O(n)
    # (para remover o primeiro nó apenas: O(1))

    def removeLista(self, K):
        noAtual = self.cabeca
        if noAtual == None:
            return None
        if noAtual.chave == K:
            self.cabeca = noAtual.proximo
            return 0
        noAnterior = noAtual
        noAtual = noAtual.proximo
        while (noAtual != None):
            if noAtual.chave == K:
                noAnterior.proximo = noAtual.proximo
                return K
            else:
                noAnterior = noAtual
                noAtual = noAtual.proximo
        return -1

# teste


e0 = No(0, 'Joao')
Lista = ListaEncadeada(e0)
k0 = Lista.busca(0)
print(k0.valor)
Lista.print()

e1 = No(1, 'Maria')
Lista.insereFinal(e1)
Lista.print()

e2 = No(-1, 'Ana')
Lista.insereInicio(e2)
Lista.print()

e3 = No(2, 'Arthur')
Lista.insereOrdenada(e3)
Lista.removeLista(2)
Lista.print()
