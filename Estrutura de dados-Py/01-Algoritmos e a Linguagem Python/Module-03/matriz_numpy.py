import numpy as np

numeros = np.array([[4, 13, 16], [5, 7, 1], [8, 10, 15]])
print(numeros)
minimo = numeros.min()  # Return number Min in to array
maximo = numeros.max()  # Return number Max in to array
soma = numeros.sum()  # Return sum all to array
media = numeros.mean()  # Return avarage number
desvio = numeros.std()  # Return standard deviation in to array

print("Minimo = ", minimo)
print("Maximo = ", maximo)
print("Soma = ", soma)
print("Media = ", media)
print("Desvio = ", desvio)
