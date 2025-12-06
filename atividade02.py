################# ATIVIDADES ###################

# 1

# amigos = {}

# amigos ['João'] = 20
# amigos ['Maria'] = 22
# amigos ['Carlos'] = 19

# print("\nAmigos adicionados:", amigos)

# idade_maria = amigos ['Maria']
# print(f'\nA idade de Maria é: {idade_maria} anos')

# amigos['Carlos'] = 20
# print('\nIdade de Carlos atualizada:', amigos)

# amigos['Ana'] = 21
# print('\nAna foi adicionada', amigos)

# del amigos['João']
# print('\nJoão foi deletado', amigos)

# print(amigos)

# 2 

# produtos = {}

# produtos ['Arroz'] = 25.90
# produtos ['Feijão'] = 8.50
# produtos ['Leite'] = 5.80

# print('\nItens Adicionados;', produtos)

# valor_arroz = produtos ['Arroz']
# print(f'\nO valor do arroz é: {valor_arroz}')

# produtos['Leite'] = 4.00
# print('\nNovo preço do leite', produtos) 

# produtos['Açúcar'] = 6.30
# print('\nNovo item adicionado', produtos)

# del produtos['Feijão']
# print('\nProduto *Feijâo* removido:', produtos)

# # Lista atualizada

# print('\n        Lista de produtos atualizada\n',produtos)


# 3

# candidatos = []

# for c in range(5):
#     nome = input('Digite seu nome: ')
#     idade = input('Digite sua idade: ')
#     telefone = input('Digite seu telefone: ')
#     email = input('Digite seu email: ')
#     formação = input('Digite sua formação Acadêmica: ')

#     info = {
#         'nome': nome,
#         'idade': idade,
#         'email': email,
#         'formação': formação
#     }
#     candidatos.append(info)
#     print(f'Candidato {c + 1} - {nome} cadastrado com sucesso!!')

# 4

# atletas = []

# for a in range(2):
#     nome = input('Digite seu nome: ')
#     tempo = float(input('Digite o tempo: '))
#     categoria = input('Digite sua categoria: ')


#     if tempo <= 12:
#         print('Classificado!')

#         info = {
#             'nome' : nome,
#             'tempo' : tempo,
#             'categoria' : categoria
#         }
#         atletas.append(info)
#     else:
#         print('Desclassificado')

# print('RESULTADOS')

# if atletas:
#     for info in atletas:
#         print(f'{info['nome']} , {info['tempo']}, {info['categoria']}')
# else:
#      print("Nenhum atleta atingiu o tempo de classificação de 12.0 segundos ou menos.")
