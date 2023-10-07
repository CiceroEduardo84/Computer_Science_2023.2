# Dada a árvore de pesquisa binária . A tarefa é encontrar a soma de todos os elementos menores e iguais ao K-ésimo menor elemento.
class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insertNodo(root, value):
    if root is None:
        return Tree(value)
    elif root.key == value.key:
        return root
    elif root.key < value.key:
        if root.right is None:
            root.right = value
        else:
            root.right = insertNodo(root.right, value)
    elif root.key > value.key:
        if root.left is None:
            root.left = value
        else:
            root.left = insertNodo(root.left, value)
    return root


def sumMinNodo(root, key, count):
    if root == None:
        return 0
    elif count[0] > key[0]:
        return 0

    res = sumMinNodo(root.left, key, count)
    if (count[0] >= key[0]):
        return res
    res += root.key
    count[0] += 1
    if count[0] >= key[0]:
        return res

    return res + sumMinNodo(root.right, key, count)


def initSumMinNodo(root, key):
    count = [0]
    return sumMinNodo(root, key, count)


if __name__ == '__main__':
    root = None
    root = Tree(50)
    key = [10, 70, 40, 60, 100, 5, 6, 7, 8]
    for key in key:
        nodo = Tree(key)
        insertNodo(root, nodo)
    
    k = [2]
    print(initSumMinNodo(root,k))
