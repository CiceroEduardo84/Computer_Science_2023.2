# https://numpy.org/
#  abara o terminal e digite: pip install numpy
# para instalar a biblioteca numpy

# len() == Tamanho da lista
# append() == adicionar novo valor a lista
# remove() == remover valor da lista
# pop() == remover pelo índice

import numpy as np

nomes = np.array(["João", "Maria", "Ana"])
print(nomes)

copia = nomes.copy()
copia[0] = "Nelson"
print(nomes)
print(copia)

visao = nomes.view()
visao[0] = "Nelson"
print(nomes)
print(visao)

for indice, valor in enumerate(nomes):
    print(indice, valor)
