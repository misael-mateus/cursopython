"""
For / Else em Python
"""
variavel = ['Danniel', 'Albuquerque', 'Maria']

for valor in variavel:
    if valor.lower().startswith('a'):
        continue
    print(valor)