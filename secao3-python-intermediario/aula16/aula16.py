"""
lista = [0,1,2,3,4,5]

print(hasattr(lista, '__iter__'))
"""
import sys

lista = list(range(100000))

print(sys.getsizeof(lista))


l1 = [x for x in range(10000)] # lista
l2 = (x for x in range(10000)) # geradores

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))


print(next(l2)) # pedir o valor

