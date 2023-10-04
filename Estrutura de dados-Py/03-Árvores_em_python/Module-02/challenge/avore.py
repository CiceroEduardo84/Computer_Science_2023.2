# Binary search tree

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)

def insere(raiz, nodo):
    """Insere um nodo em uma árvore binária de pesquisa."""
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo

    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def DeleteBST(raiz, chave):
    if raiz is None:
        return raiz
    if chave < raiz.chave:
        raiz.esquerda = DeleteBST(raiz.esquerda, chave)
    elif chave > raiz.chave:
        raiz.direita = DeleteBST(raiz.direita, chave)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        temp = NodoArvore(raiz.dirieta)
        raiz.chave = temp.chave
        raiz.direita = DeleteBST(raiz.direita, temp.chave)
    return raiz

def busca(raiz, chave):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None
    if raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    return busca(raiz.esquerda, chave)

def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave),
    em_ordem(raiz.direita)
            
if __name__ == '__main__':
    raiz = NodoArvore(40)
    
    # Inserir
    for chave in [20, 60, 50, 70, 10, 30]:
        nodo = NodoArvore(chave)
        insere(raiz, nodo)
    # Imprime o caminhamento em ordem da árvore.
    em_ordem(raiz)
    
    print(30*"-"+"Buscar"+30*"-")
    
    # Buscar
    for chave in [-50, 10, 30, 70, 100]:
        resultado = busca(raiz, chave)
        if resultado:
            print("Busca pela chave {}: Sucesso!".format(chave))
        else:
            print("Busca pela chave {}: Falha!".format(chave))
    
    print(30*"-"+"delete 30, buscar"+30*"-")

    # deletar e buscar
    for chave in [-50, 10, 30, 70, 100]:
        DeleteBST(raiz, 30)
        resultado = busca(raiz, chave)
        if resultado:
            print("Busca pela chave {}: Sucesso!".format(chave))
        else:
            print("Busca pela chave {}: Falha!".format(chave))