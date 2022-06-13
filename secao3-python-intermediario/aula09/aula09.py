# d1 = {
#     'chave1' : 'valor',
#     'chave2' : 'Outro valor',
#     'chave3' : 'Tuplar'
# }

# for k in d1.items():
#     print(k[0], k[1])

# for k in d1.values():
#     print(k)

# for k, v in d1.items():
#     print(k, v)
####################################
# clientes = {
#    'Cliente1' : {
#        'nome' : 'Luiz',
#        'sobrenome':'Otávio',
#    },
#     'Cliente2' : {
#        'nome' : 'Danniel',
#        'sobrenome':'Albuquerque',
#    },
# }
#
# for clients_k, clientes_v in clientes.items():
#     print(f'Exibindo {clients_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')
###################################################
"""
Convertendo lista em dicionário
"""
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)