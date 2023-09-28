# -----LIFO------
class PilhaEncadeada:
    def __init__(self, topo=None):
        self.topo = topo

    def push(self, novoNo):
        novoNo.proximo = self.topo  # insere o nó
        self.topo = novoNo  # atualiza o topo da pilha

    def push(novoNo):
        global pilha
        global topoPilha
        global maxPilha
        if topoPilha == None:  # pilha vazia
            pilha[0] = novoNo  # insere o nó
            topoPilha = 0  # atualiza o topo da pilha
        elif (topoPilha == maxPilha-1):  # pilha cheia
            # -1 → erro de pilha cheia
            return (30*"-") + "\n Pilha cheia\n " + (30*"-")
        else:
            topoPilha = topoPilha+1  # atualiza o topo da pilha
            pilha[topoPilha] = novoNo  # insere o nó
        return topoPilha  # saída normal

    def pop(self):
        if self.topo == None:
            return None  # erro pilha vazia
        k = self.topo  # salva o nó removido
        self.topo = self.topo.proximo  # remove o nó
        return k  # retorna o nó removido

    def pop():
        global pilha
        global topoPilha
        global maxPilha
        if topoPilha == None:  # erro -pilha vazia
            # None indica erro pilha vazia
            return (30*"-") + "\n Pilha Vazia\n " + (30*"-")
        else:
            k = pilha[topoPilha]  # Salva o nó removido
            if topoPilha == 0:  # Pilha vazia após a remoção
                topoPilha = None
            else:
                topoPilha = topoPilha-1  # remove um nó
            return k  # retorne k= 0 nó consumido


maxPilha = 10
pilha = [None]*maxPilha
topoPilha = None

print(pilha)
# inserir
for i in range(10):
    PilhaEncadeada.push(i)
    print(pilha)
print(PilhaEncadeada.push(11))

# Remover
for i in range(10):
    print(PilhaEncadeada.pop())
print(PilhaEncadeada.pop())
