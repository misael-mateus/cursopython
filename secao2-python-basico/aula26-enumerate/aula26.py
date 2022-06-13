"""
* Enumerate - Enumerar elementos da lista # List
"""
lista = [['Edu', 'Joao', 'Luiz'],['Maria', 'Aline', 'Joana'],['Helena', 'Ed', 'Lu']]

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
