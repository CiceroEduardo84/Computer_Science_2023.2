# Dada uma árvore de pesquisa binária e uma chave. Verifique se a chave fornecida existe no BST ou não sem recursão.
import colorama
from colorama import Fore


class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def searchNode(root, key):
    while root != None:
        if key > root.key:
            root = root.right
        elif key < root.key:
            root = root.left
        else:
            return True
    return False


def insert(Node, key):
    # Node == None->insert key
    if Node == None:
        return Tree(key)
    # key more node.key ->insert(Node)
    if key < Node.key:
        insert(Node.left, key)
    elif key > Node.key:
        insert(Node.right, key)

    return Node


if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    key = [10, 70, 40, 60, 100, 5, 6, 7, 8]
    for key in key:
        insert(root, key)

    colorama.init()
    print(Fore.MAGENTA + 15*"--" + "Verificar se valor está presente na arvore" + 15*"--")
    a = 20
    print('Valor {}'.format(a))
    if searchNode(root,a):
        print(Fore.GREEN + "Yes, is present!")
    else:
        print(Fore.RED + "Not present!")
    colorama.deinit()
