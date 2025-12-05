lista_numeros = []

for n in range(5):
    num = input('informe o numero: ')
    lista_numeros.append(num)

print(lista_numeros[0])
lista_numeros[0] = 22 # altera o valor do indice 0
lista_numeros.pop(-2) # deleta o ultimo numero
lista_numeros.remove(30) # deleta pelo valor