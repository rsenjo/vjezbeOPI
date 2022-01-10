n = int(input('Unesi broj elemenata liste: '))
lista1 = [0] * n
lista2 = [0] * n

for i in range(n):
    lista1[i] = int(input('Unesite broj: '))
    if lista1[i]%2 != 0:
        lista2[i] = lista1[i] - 3
    else:
        lista2[i] = lista1[i] + 3

for i in range(n):
    print(lista1[i], lista2[i])
