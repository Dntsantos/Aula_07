# # Dicionario
# # Estrutura chave e valor
# # Simbolo {}

# notas = {} # Dicionário vazio
# notas['matematica'] = 8.5
# notas['portugues'] = 7.0
# notas['historia'] = 9.2

# notas['matematica'] = 8.0
# notas['geografia'] = 9.9
# del notas['historia']  # deleta do dicionario/lista
# print(notas)

livros = {}
lista_cadastro = []

# Cadastro em Dicionários
for i in range(3):
    titulo = input('informe o titulo: ')
    ano = input('informe o ano: ')
    autor = input('informe o autor: ')
    genero = input('informe o genero: ')

    livros = {
        'titulo': titulo,
        'ano': ano,
        'autor': autor,
        'genero': genero
    }

    lista_cadastro.append(livros)
    print(f'Livro {i + 1} - {titulo} CADASTRADO')