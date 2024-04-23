n = int(input())
v = []
g = 0

for i in range(n):
    elemento = int(input())
    v.append(elemento)
    v[i] = elemento

if n%2 == 0:
    for j in range(0, len(v), 2):
      if v[j] != v[j + 1]:
          c = 'Nao eh um vetor de duplas!'
      else: 
          c = 'Eh um vetor de duplas!'
else:
    c = 'Nao eh um vetor de duplas!'
print(c)

