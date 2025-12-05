notas = []

for num in range(5):
    num = float(input('informe a nota: '))
    notas.append(num)

for num in notas:
    if num >= 7:
        print(f'{num} / APROVADO')
    else:
        print(f'{num} / REPROVADO')


