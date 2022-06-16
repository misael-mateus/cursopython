"""
Dictionary Comprehension
"""
Lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

# d1 = {x: y for x, y in Lista}
# print(d1)

#########################################
# d1 = {x: y for x, y in enumerate(range(5))}
# print(d1)

# d1 = {x for x in range(5)}  # Set
# print(d1, type(d1))


d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)
      