# https://numpy.org/
# pip install numpy

# len() == Tamanho da lista
from numpy import *

nomes = array(["João", "Maria", "Ana"])
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
