"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

from itertools import zip_longest, count

# ### Código
# cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
#
# # Código
# estados = ['SP', 'MG', 'BA']
#
# # cidades_estados = zip(cidades, estados)
# cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')
# print(list(cidades_estados))

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']


cidades_estados = zip(indice, estados, cidades)

for indice, estado, cidades in cidades_estados:
    print(indice, estado, cidades)

