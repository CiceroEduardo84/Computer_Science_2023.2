class NoArvore:
  def __init__(self, chave = None, esquerda = None, direita = None):
      self.chave = chave
      self.esquerda = esquerda
      self.direita = direita
  
      def BuscaBST(raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz
    
        if raiz.chave < chave:
            return  BuscaBST(raiz.direita, chave)
        else:
            return  BuscaBST(raiz.esquerda, chave)

if __name__ == '__main__':
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore (35)
    raiz.direita  = NoArvore (75)

    raiz.direita.esquerda  = NoArvore(65)
    raiz.direita.direita   = NoArvore(85)
    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita  = NoArvore(45)
    
    cont = [10]
    nivel = 0
  
    def ImprimeArvoreRecurs(raiz, nivel):
        if (raiz == None):
            nivel += cont[0] 
            return nivel

    # Imprime Filhos à Direita
    ImprimeArvoreRecurs(raiz.direita, nivel)
    print()
    for i in range(cont[0], nivel): 
        print(end=" ")
        print(f"{raiz.chave}<")

    # Imprime Filhos à Esquerda
    ImprimeArvoreRecurs(raiz.esquerda, nivel)

    def ImprimeArvore(raiz):
      ImprimeArvoreRecurs(raiz, 0)
      
