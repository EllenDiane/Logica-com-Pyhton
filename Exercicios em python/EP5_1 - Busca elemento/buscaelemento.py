l = int(input()) 
c = int(input())

m = [[0]*c for _ in range(l)]

for i in range(l):
  for j in range(c):
    m[i][j] = int(input())

numero = int(input())


numeroencontrado = False
for i in range(l):
  for j in range(c):
    if numero == m[i][j]:
      print(f"{i+1} {j+1}")
      numeroencontrado = True

if numeroencontrado == False:
  print('-1')
