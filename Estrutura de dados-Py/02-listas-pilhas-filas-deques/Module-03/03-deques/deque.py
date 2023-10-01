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
        
    #igual a inserção em pilha
    def PUSH_front(self, novoNo):
        novoNo.proximo = self.final  
        self.final = novoNo 
        
    # Para caso continguo
    def PUSH_front(novoNo):
        global deque
        global finalDeque
        global maxDeque
        if finalDeque == None: 
            deque[0] = novoNo 
            finalDeque = 0 
        elif (finalDeque == maxDeque-1): 
            return (30*"-") + "\n Pilha cheia\n " + (30*"-")
        else:
            finalDeque = finalDeque+1 
            deque[finalDeque] = novoNo 
        return finalDeque
      
    #igual a inserção em fila
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
            return (30*"-") + "\n Filha Cheia \n " + (30*"-")
        else:
            finalDeque = (finalDeque+1) % maxDeque
            deque[finalDeque] = novoNo  
        return finalDeque 
    

maxDeque = 10
deque=[None] * maxDeque
inicioDeque = None
finalDeque = None