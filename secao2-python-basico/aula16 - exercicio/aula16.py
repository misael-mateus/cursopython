"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

numero = int(input('Digite um número inteiro: '))
res = numero % 2

if res == 1:
    print('Este número é ímpar')
else:
    print('Este número é par')
##########################################
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
else:
    print('Isso não é um número inteiro')
"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = int(input('Digite a hora: '))

if hora >= 0 and hora <= 11:
    print(f'Bom dia {hora}')
elif hora >= 12 and hora <= 17:
    print(f'Boa tarde {hora}')
elif hora >= 18 and hora <= 23:
    print(f'Boa noite {hora}')
else:
    print('Você não digitou um valor válido para hora de ')

###############################################
horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print("Horário deve estar entre 0 e 23")
    else:
        if horario <= 11:
            print('Boa dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print("Por favor, digite um horário entre 0 e 23.")
"""




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = input('Digite seu nome: ')

nome =len(nome)

if nome <= 4:
    print('Seu nome é curto')
elif nome == 5 or nome == 6:
    print('Seu nome é normal')
elif nome > 6:
    print('Seu nome é muito grande')
    
#############################################
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
"""

