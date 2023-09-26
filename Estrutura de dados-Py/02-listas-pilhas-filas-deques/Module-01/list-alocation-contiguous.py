# Usando index()
# implememtando a busca
# Complexidade: O(n)

# Codigo de busca
nomes = ['João', 'Maria', 'Ana']
i = nomes.index("Ana")
# print(i)

# k= Item a ser descoberto o indice
# L= minha lista
# N= numero Max de objetos dessa lista


def buscaLista(k, L, n):
    i = 0
    indiceL = -1
    while i < n:
        if L[i] == k:
            indiceL = i
            i = n+1
        i = i+1
    return indiceL

def buscaOrdenada(k,L,n):
  i=0
  indiceL=-1
  while (i<n):
    if L[i] >= k:
      if L[i] == k:
        indiceL = i
        i=n+1
      else:
        i=n+1
    else:
      i=i+1
  return indiceL
      
# numeros=[1,2,3,4,6,7,8,9,10]
# i=buscaOrdenada(5,numeros,len(numeros))
# print (i)
# i=buscaOrdenada(3,numeros,len(numeros))
# print(i)

# -------------------------------------------------
# Usando o append()
# Implememtação de inserção
# Inserção em lista ordenada

# Complexidade: O(1) caso geral O(n) caso ordenado


# Código de inserção
nomes2 = ['Joao', 'Maria', 'Ana']
nomes2.append('Arthur')
# print(nomes)


def inserir(K, L, n):
    L.append('')
    L[n] = K
    n += 1
    return L

# print(inserir('Jose',nomes,len(nomes)))


def insereOrdenada(k, L, n):
    i = 0
    posInsercao = -1
    while (i < n):
        if L[i] >= k:
            if L[i] == k:
                return -1
            else:
                posInsercao = i
                i = n+1
        else:
            i = i+1
            if i == n:
                posInsercao = n
    L.append('')
    i = n
    while (i > posInsercao):
        L[i] = L[i-1]
        i -= 1
    L[posInsercao] = k
    return posInsercao

# numeros=[1,2,3,4,6,7,8,9,10]
# inserir(12,numeros,len(numeros))
# print(numeros)
# insereOrdenada(5,numeros,len(numeros))
# print(numeros)

# Usando remove()
# Usando pop()
# implementando a remoção

# complexidade: O(n)

# Código de remoção

nomes3 = ['João', 'maria', 'Ana', 'Arthur']
# nomes.remove('Arthur')
# print(nomes)
nomes.pop(2)
# print(nomes)


def removeL(k, L, n):
    i = 0
    posRemocao = -1
    while (i < n):
        if L[i] == k:
            posRemocao = i
            i = n+i
        else:
            i = i+1
            if i == n:
              return -1
    i = posRemocao
    while (i < n-1):
        L[i] = L[i+1]
        i = i+1
    L.pop(n-1)
    return L

# print(removeL('João',nomes3,len(nomes3)))