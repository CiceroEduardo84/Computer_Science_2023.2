class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


def BuscaBST(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return BuscaBST(raiz.direita, chave)
    else:
        return BuscaBST(raiz.esquerda, chave)


def InserirBST(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    elif raiz.chave == chave.chave:
        return raiz
    elif raiz.chave < chave.chave:
        if raiz.direita is None:
            raiz.direita = chave
        else:
            raiz.direita = InserirBST(raiz.direita, chave)
    elif raiz.chave > chave.chave:
        if raiz.esquerda is None:
            raiz.esquerda = chave
        else:
            raiz.esquerda = InserirBST(raiz.esquerda, chave)
    return raiz

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
        temp = ValorNo(raiz.dirieta)
        raiz.chave = temp.chave
        raiz.direita = DeleteBST(raiz.direita, temp.chave)
    return raiz

def ValorNo(no):
    atual = no
    while(atual.esquerda is not None):
        atual = atual.esquerda
    return atual

cont = [10]
def ImprimeArvoreRecurs(raiz, nivel):
    
    if (raiz == None):
        nivel = cont[0]
        return nivel

    # Imprime Filhos à Direita
    print(ImprimeArvoreRecurs(raiz.direita,nivel))

    for i in range(cont[0], nivel):
        print(end=" ")
        print(f"{raiz.chave}<")

    # Imprime Filhos à Esquerda
    ImprimeArvoreRecurs(raiz.esquerda, nivel)
    
def ImprimeArvore(raiz):
    ImprimeArvoreRecurs(raiz, 0)
    
# def em_ordem(raiz):
#     if not raiz:
#         return
#     em_ordem(raiz.esquerda)
#     print(raiz.chave),
#     em_ordem(raiz.direita)
    
if __name__ == '__main__':
    raiz = NoArvore(40)
    
    # Inserir
    for chave in [20, 60, 50, 70, 10, 30]:
        nodo = NoArvore(chave)
        InserirBST(raiz, nodo)
    # Imprime o caminhamento em ordem da árvore.
    # em_ordem(raiz)
    
    print(30*"-"+"Buscar"+30*"-")
    
    # Buscar
    for chave in [-50, 10, 30, 70, 100]:
        resultado = BuscaBST(raiz, chave)
        if resultado:
            print("Busca pela chave {}: Sucesso!".format(chave))
        else:
            print("Busca pela chave {}: Falha!".format(chave))
    
    print(30*"-"+"delete 30, buscar"+30*"-")

    # deletar e buscar
    for chave in [-50, 10, 30, 70, 100]:
        DeleteBST(raiz, 30)
        resultado = BuscaBST(raiz, chave)
        if resultado:
            print("Busca pela chave {}: Sucesso!".format(chave))
        else:
            print("Busca pela chave {}: Falha!".format(chave))
            
ImprimeArvore(raiz)

