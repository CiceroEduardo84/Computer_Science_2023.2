# Implementação do meu proprio deque

class No():
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None


class DequeEncadeada():
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

    # igual a inserção em pilha
    def PUSH_front(self, novoNo):
        novoNo.proximo = self.final
        self.final = novoNo

    # Para caso continguo
    # def PUSH_front(novoNo):
    #     global deque
    #     global inicioDeque
    #     global maxDeque
    #     if inicioDeque == None:
    #         deque[9] = novoNo
    #         inicioDeque = 0
    #     elif (inicioDeque == maxDeque+1):
    #         return (30*"-") + "\n Pilha cheia\n " + (30*"-")
    #     else:
    #         inicioDeque = inicioDeque-1
    #         deque[inicioDeque] = novoNo
    #     return inicioDeque
    def PUSH_front(novoNo):
        global deque
        global inicioDeque
        global maxDeque

        if inicioDeque is None:
            deque[9] = 0
            inicioDeque = maxDeque-1
        elif inicioDeque == 0:
            return (30 * "-") + "\n Deque cheia\n " + (30 * "-")
        else:
            inicioDeque = (inicioDeque - 1) % (maxDeque + 1)
            deque[inicioDeque] = novoNo
        return inicioDeque

    # igual a inserção em fila
    def PUSH_back(self, novoNo):
        if self.inicio == None:
            self.inicio = novoNo
            self.final = novoNo
        else:
            self.final.proximo = novoNo
            self.final = novoNo

    # Para caso continguo
    def PUSH_back(novoNo):
        global inicioDeque
        global maxDeque
        global finalDeque
        global deque
        if inicioDeque == None:
            deque[0] = novoNo
            inicioDeque = 0
            finalDeque = 0
        elif (finalDeque+1) % maxDeque == inicioDeque:
            return (30*"-") + "\n Deque Cheio \n " + (30*"-")
        else:
            finalDeque = (finalDeque+1) % maxDeque
            deque[finalDeque] = novoNo
        return finalDeque

    # Identico a remoção em pilha
    def popfront(self):
        if self.final == None:
            return None
        k = self.final
        self.final = self.final.proximo
        return k

    def popFront():
        global deque
        global inicioDeque
        global maxDeque
        if inicioDeque == maxDeque:
            return (30*"-") + "\n Deque Vazia\n " + (30*"-")
        k = deque[inicioDeque]
        inicioDeque = inicioDeque+1
        return k

    def popBack(self):
        if self.inicio == None:
            return None			                # None indica erro deque vazia
        else:
            k = self.final  # salva o nó removido
            self.final = self.final.anterior  # remove o nó
            self.final.proximo = None  # aponta o próximo do final para λ
            return k  # retorne k=o nó consumido

    # Para o caso contíguo
    def popBack():
        global inicioDeque  # indica o acesso a variáveis globais
        global maxDeque
        global finalDeque
        global deque
        if finalDeque == None:  # Deque vazia
            # erro Deque vazia
            return (30*"-") + "\n Deque Vazia\n " + (30*"-")
        k = deque[finalDeque]  # salva o nó removido
        if finalDeque == inicioDeque:
            finalDeque = None  # Deque vazia após remoção
        else:
            finalDeque = (finalDeque-1) % maxDeque  # remove o nó
        return k			               	   	           # retorne k=o nó consumido


maxDeque = 10
deque = [None] * maxDeque
inicioDeque = None
finalDeque = None

print(30*"-"+"Inserção no incio e remoção no incio"+30*"-")
print(deque)
# inserir
for i in range(10):
    DequeEncadeada.PUSH_front(i)
    print(deque)
print(DequeEncadeada.PUSH_front(11))

# Remover
for i in range(10):
    print(DequeEncadeada.popFront())
print(DequeEncadeada.popFront())

maxDeque = 10
deque = [None] * maxDeque
inicioDeque = None
finalDeque = None

print(30*"-"+"Inserção no FINAL e remoção no FINAL"+30*"-")
print(deque)
# inserir
for i in range(10):
    DequeEncadeada.PUSH_back(i)
    print(deque)
print(DequeEncadeada.PUSH_back(11))

# Remover
for i in range(10):
    print(DequeEncadeada.popBack())
print(DequeEncadeada.popBack())
