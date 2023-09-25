# Matrizes == Array de Arrays

# Append --- Add new element
# Remove --- remove one element
# Pop --- Remove to índice

compras = [["Arroz", 6], ["Feijão", 5, 1], ["Carne", 50, 2]]
print(compras)
compras.append(["cebola", 5, 1])
print(compras)
compras[0].append(2)
print(compras)
compras.remove(["Feijão", 5, 1])
print(compras)
compras.pop(2)
print(compras)
