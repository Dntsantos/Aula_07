previsoes = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']
print(previsoes)

PREVISAO_FELIZ = 'Ensolarado'

for p in previsoes:
    # print(p)

    if p == PREVISAO_FELIZ:
        print('Pode passear')
    else:
        print('Não esqueça o guarda-chuva')
    input()
    