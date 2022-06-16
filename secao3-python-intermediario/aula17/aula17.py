# list, tuples, str -> Sequences -> Iterável
nome = 'Danniel de Albuquerque'
iterador = iter(nome)
gerador = (letra for letra in nome)


print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('OLHA O FOR')

for letra in gerador:
    print(letra)

