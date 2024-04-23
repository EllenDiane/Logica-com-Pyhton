n = int(input("quantidade de elemento do vetor:"))
v = []

for i in range(n):
    el = int(input("Elementos do vetor:"))
    v.append(el)


for j in range(n):
  c = v[j-1] + v[j+1]
  if v[j] == 1:
    print(c)