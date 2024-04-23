n = int(input())
a, c = 0, 0
while (c < n):
  numero = int(input())
  a += numero
  c += 1
  if c == 1:
        maior_valor = numero
        menor_valor = numero
  else:
    if numero > maior_valor:
            maior_valor = numero

    if numero < menor_valor:
            menor_valor = numero

print(a)
media = a/c
print ("{:.2f}".format(media))
print(menor_valor)
print(maior_valor)
