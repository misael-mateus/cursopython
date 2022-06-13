#       Índices
#       0123456789..........................33
# frase = 'o rato roeu a roupa do rei de roma'
# tamanho_frase = len(frase)
# contator = 0
# nova_string = ''
#
# while contator < tamanho_frase:
#     letra = frase[contator]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contator += 1
#
# print(nova_string)

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contator = 0
nova_string = ''

input_do_usuario = input('Digite a letra que deseja que seja maiúscula: ')  # Iterável

# Iteração <- Iterar
while contator < tamanho_frase:
    letra = frase[contator]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()

    else:
        nova_string += letra
    contator += 1

print(nova_string)