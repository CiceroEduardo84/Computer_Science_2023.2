# Bubblesort
# def trocar -- Procedimento para trocar elementos
# seq = [] -- Inicialização da sequencia de teste
# Troca -- Variavel de controle de laço
# while troca: -- Laço da multiplas passagens
# for i in range -- Laço interno de uma passagem
# print(seq) impressão da sequência

def trocar(seq, i):
    aux = seq[i]
    seq[i] = seq[i+1]
    seq[i+1] = aux


seq = [1, 15, 22, 6, 7, 19, 8, 3, 5, 20]
troca = 1
while troca:
    troca = 0
    i = 0
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            trocar(seq, i)
            troca = 1
print(seq)
