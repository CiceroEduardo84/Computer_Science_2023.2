# Nó
class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    def __init__(self, inicio=None, cabeca=None):
        self.inicio = inicio
        self.final = inicio
        self.cabeca = cabeca

    def print(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo

    def insere(self, novoNo):
        if self.inicio == None:
            self.inicio = novoNo
            self.final = novoNo
        else:
            self.final.proximo = novoNo
            self.final = novoNo
    # Para caso continguo

    def insereFila(novoNo):
        global inicioFila  # Indica o acesso  avariavel globais
        global maxFila
        global finalFila
        global fila
        if inicioFila == None:  # fila Vazia
            fila[0] = novoNo  # insere No
            inicioFila = 0  # atualiza o onicio da fila
            finalFila = 0  # atualiza o final da fila
        elif (finalFila+1) % maxFila == inicioFila:  # fila cheia
            return -1  # retorna -1 se a fila estiver cheia
        else:
            finalFila = (finalFila+1) % maxFila  # atualiza o onicio da fila
            fila[finalFila] = novoNo  # Insere o nó
        return finalFila  # saída normal

    def remove(self):
        if self.inicio == None:  # Fila vazia
            return "Fila vazia"  # None indica erro fila vazia
        else:
            k = self.inicio  # salva o nó removido
            self.inicio = self.inicio.proximo  # remove o nó
            ini = self.inicio
            fin = self.final
            return k, ini, fin  # retorna k = o nó consumido

    # Para caso continguo
    def removeFila():
        global inicioFila  # Indica o acesso  avariavel globais
        global maxFila
        global finalFila
        global fila
        if inicioFila == None:  # Fila vazia
            return None  # erro fila vazia
        k = fila[inicioFila]
        if finalFila == inicioFila:
            inicioFila = None  # Fila vazia após remoção
        else:
            inicioFila = (inicioFila+1) % maxFila  # remove o nó
        return k  # retorna k = o nó consumido


# testes
e0 = No(0, 'Joao')
fila = FilaEncadeada(e0)
fila.print()

e1 = No(1, 'Maria')
fila.insere(e1)
fila.print()

e2 = No(-1, 'Ana')
fila.insere(e2)
fila.print()

e3 = No(2, 'Arthur')
fila.insere(e3)
fila.print()
k = fila.remove()

print("No removido: " + k[0].valor)
print("Inicio da fila: " + k[1].valor)
print("final da fila: " + k[2].valor)
fila.print()
print(30*"-")


while k[1] != None:
    k = fila.remove()
    if k[1] == None:
        print("Fila Vazia")
    else:
        print("No removido: " + k[0].valor)
        print("Inicio da fila: " + k[1].valor)
        print("final da fila: " + k[2].valor)
        fila.print()
        print(30*"-")
