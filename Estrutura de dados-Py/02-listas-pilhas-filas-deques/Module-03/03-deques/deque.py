# DEQUE -- Double Ended QUEue
from collections import deque

q=deque()			     #cria o deque
q.append('b')		     #insere no final
q.append('c') 
q.append('d') 
q.appendleft('a')     #insere no inicio
print(q)			     #imprime o deque
print(q.popleft())	     #remove do inicio
print(q.pop())	     	 #remove do final
print(q)
print(30*"-")

class No():
    def __init__(self,chave,valor):
      self.chave = chave
      self.valor = valor
      self.proximo = None
      self.anterior = None

class DequeEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.inicio = inicio
    
    def PUSH_back(novoNo):
        global inicioDeque  # Indica o acesso  avariavel globais
        global maxDeque
        global finalDeque
        global deque
        if inicioDeque == None:  # fila Vazia
            deque[9] = novoNo  # insere No
            inicioDeque = 9  # atualiza o onicio da fila
            finalDeque = 9  # atualiza o final da fila
        elif (finalDeque - 1) % maxDeque == inicioDeque:  # fila cheia
            return (30*"-") + "\n Filha Cheia \n " + (30*"-")  # retorna -1 se a fila estiver cheia
        else:
            finalDeque = (finalDeque - 1) % maxDeque  # atualiza o onicio da fila
            deque[finalDeque] = novoNo  # Insere o nó
        return finalDeque  # saída normal
      
    def PUSH_front(novoNo):
        global inicioDeque  # Indica o acesso  avariavel globais
        global maxDeque
        global finalDeque
        global deque
        if inicioDeque == None:  # deque Vazia
            deque[0] = novoNo  # insere No
            inicioDeque = 0  # atualiza o onicio da deque
            finalDeque = 0  # atualiza o final da deque
        elif (finalDeque+1) % maxDeque == inicioDeque:  # deque cheia
            return (30*"-") + "\nDeque Cheio \n " + (30*"-")  # retorna -1 se a deque estiver cheia
        else:
            finalDeque = (finalDeque+1) % maxDeque  # atualiza o onicio da deque
            deque[finalDeque] = novoNo  # Insere o nó
        return finalDeque  # saída normal

    def popBack(self):
        if self.inicio==None:		                 	# erro -deque vazia
            return None			                # None indica erro deque vazia
        else:
            k =self.final			                #salva o nó removido
            self.final=self.final.anterior	    #remove o nó
            self.final.proximo=None	            #aponta o próximo do final para λ
            return k		                 	    #retorne k=o nó consumido
          
    def popBack():
        global inicioDeque        #acesso a variavel global
        global maxDeque
        global finalDeque
        global deque
        if inicioDeque == None: #deque vazia retorna erro
            return (30*"-") + "\n Deque Vazio \n " + (30*"-")
        k=deque[finalDeque]
        if finalDeque == inicioDeque:
            return  (30*"-") + "\n Deque Vazio \n " + (30*"-")
        else:
          finalDeque=(finalDeque-1) % maxDeque #remove nó
        return k          #retorne k= o nó consumido
      
    def popFront():
        global inicioDeque        #acesso a variavel global
        global maxDeque
        global finalDeque
        global deque
        if inicioDeque == None: #deque vazia retorna erro
            return (30*"-") + "\n Deque Vazio \n " + (30*"-")
        k=deque[inicioDeque]
        if finalDeque == inicioDeque:
            return  (30*"-") + "\n Deque Vazio \n " + (30*"-")
        else:
          inicioDeque=(inicioDeque+1) % maxDeque #remove nó
        return k          #retorne k= o nó consumido
      
# maxDeque=10
# deque=[None]*maxDeque
# inicioDeque=None
# finalDeque=None


# print(deque)

# print((30*"-")+"Insere no final e remove no final"+(30*"-"))

# # inserir
# for i in range(10):
#     DequeEncadeada.PUSH_back(i)
#     print(deque)
# print(DequeEncadeada.PUSH_back(11))

# # Remover
# for i in range(10):
#     print(DequeEncadeada.popBack())
# print(DequeEncadeada.popBack())

      
maxDeque=10
deque=[None]*maxDeque
inicioDeque=None
finalDeque=None


print(deque)

print((30*"-")+"Insere no inicio e remove no inicio"+(30*"-"))

# inserir
for i in range(10):
    DequeEncadeada.PUSH_front(i)
    print(deque)
print(DequeEncadeada.PUSH_front(11))

# Remover
for i in range(10):
    print(DequeEncadeada.popFront())
print(DequeEncadeada.popFront())
