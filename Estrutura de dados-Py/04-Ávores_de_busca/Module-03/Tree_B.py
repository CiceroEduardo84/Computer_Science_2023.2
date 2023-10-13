# class BTree:
#     def __init__(self, folha=True):
#         self.folha = folha
#         self.chaves = []
#         self.filhos = []

#     def inserir(self, value, order):
#         if len(self.chaves) is 0:
#             self.chaves.append(value)

#     def buscar(self, value):
#         if value == self.key:
#             return 1
#         elif value > self.key:
#             if self.direita is None:
#                 return 0
#             else:
#                 return self.direita.buscar(value)
#         elif value < self.key:
#             if self.esquerda is None:
#                 return 0
#             else:
#                 return self.esquerda.buscar(value)


# if __name__ == "__main__":
#     btree = BTree()
#     order = 3
#     keys = [10]
#     for key in keys:
#         btree.inserir(key, order)

