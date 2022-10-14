'''
Este programa gera um nome automático com base nas três primeiras letras do seu primeiro nome e as três últimas do seu Sobrenome

'''

print('------------------------------------------------------------------------------------------------------------------------------------------------------\nBem vindo ao gerador de nomes \nEste Programa gera um nome fantasia com base nas três primeiras letra do '
      'seu nome e nas três últimas do seu sobrenome. \nDepois te dá um título com base na cor escolhida.\n'
      'O Sufixo depende do gênero escolhido: Or (Masculino), Si (Feminino) ou Us (Outro) '
      '\nSiga as instruções abaixo \n ------------------------------------------------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------------------------------------------------')
gender = input('Qual é seu gênero?\n Masculino \n Feminino \n Outro \n Digite sua resposta: ')
capitalize(gender)
print(gender)
if gender == 'Feminino':
    suffix = 'si'

elif gender == 'Masculino':
    suffix = 'or'
else:
    suffix = 'us'
print('------------------------------------------------------------------------------------------------------------------------------------------------------')

firstName = input('Digite seu nome: ')
lastName = input('Digite seu sobrenome: ')
print('------------------------------------------------------------------------------------------------------------------------------------------------------')

part_One = firstName[0:3]
length = len(lastName)
partTwo = lastName[length - 3: length]

print('Gerando novo nome ...')
print('Atualizando dados ...')

generatedName = part_One + partTwo

print('------------------------------------------------------------------------------------------------------------------------------------------------------')
favouriteColor = input('Qual é sua cor preferida: \nAzul \nRoxo \nVerde \nVermelho \nAmarelo \nRosa  \nDigite sua Resposta ')


if favouriteColor == 'Azul':
    Title = 'The Sailor'
elif favouriteColor == 'Roxo':
    Title = 'The Royal'
elif favouriteColor == 'Verde':
    Title = 'The Ranger'
elif favouriteColor == 'Vermelho':
    Title = 'The thief'
elif favouriteColor == 'Amarelo':
    Title = 'The Mad'
elif favouriteColor == 'Rosa':
    Title = 'The Young'
elif favouriteColor == 'Preto':
    Title = 'The seducer of brides'
else:
    Title = 'The nobody'


print('------------------------------------------------------------------------------------------------------------------------------------------------------ \n '
      'Opção 1 - Seu novo nome é' + ' ' + generatedName+suffix + ' ' + Title +
      '\n------------------------------------------------------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------------------------------------------------------ \n '
      'Opção 2 - Seu novo nome é' + ' ' + generatedName + ' ' + Title +
      '\n------------------------------------------------------------------------------------------------------------------------------------------------------')

