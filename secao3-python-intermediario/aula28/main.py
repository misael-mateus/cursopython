#https://docs.python.org/pt-br/3/library/functions.html#open

"""
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('#########')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print('#########')

file.seek(0, 0)
for linha in file:
    print(linha, end='')


file.close()
################################################
try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()
"""

# com with não preciso pedir para fechar o arquivo, ele faz isso já
# with open('abc.txt', 'w+') as file:
#     file.write('Linha1\n')
#     file.write('Linha2\n')
#     file.write('Linha3\n')
#
#     file.seek(0)
#     print(file.read())

# lê o arquivo
# with open('abc.txt', 'r') as file:
#     print(file.read())

# with open('abc.txt', 'a+') as file:
#     file.write('Outra linha\n')
#     file.seek(0)
#     print(file.read())

#remove o arquivo
# import os
# os.remove('abc.txt')

import json

d1 = {
    'Pessoa1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa2': {
        'nome': 'Rose',
        'idade': 30,
    }
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)


