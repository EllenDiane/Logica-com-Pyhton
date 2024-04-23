def comparar_matrizes(matriz1, matriz2):
  if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
    return False
  dobro = True
  for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
      if 2*(matriz1[i][j]) != matriz2[i][j]:
        dobro = False
  return dobro
        