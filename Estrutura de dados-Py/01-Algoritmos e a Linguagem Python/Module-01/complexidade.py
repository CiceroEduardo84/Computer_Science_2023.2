# Exemplo para entender o conceito de complexidade

def inverter_lista(lista):
    tamanho = len(lista)  # 1
    limite = tamanho//2  # 2
    for i in range(limite):
        aux = lista[i]  # 3
        lista[i] = lista[n-i]  # 4 #operação elementar
        lista[tamanho-i] = aux

# 4 + n complexidade de espaço
# 2+2*N - complexidade de tempo = O(n)


def inverter_lista2(lista):
    nova_lista = []
    tamanho = len(lista)
    for i in range(tamanho):
        nova_lista.append(lista[tamanho-1])
    return nova_lista

# 2 + N
# 3 + 2 + N


def tem_duplicados(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False
# complexidade de tempo = N-1 + N-2 + N-3 ... + 1 = N*(N-1)/2
# (N^2 - N)/2 + 1 = O(n^2)
#Termo de maior grau - Termo dominante