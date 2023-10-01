from collections import deque

q = deque()  # cria o deque
q.append('b')  # insere no final
q.append('c')
q.appendleft('a')  # Insere no incio

print(q)  # imprime o deque

print(q.popleft())  # remove do inicio
print(q)  # imprime o deque

print(q.pop())  # remove do final
print(q)  # imprime o deque
