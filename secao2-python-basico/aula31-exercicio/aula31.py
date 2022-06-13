"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
contador_1 = 0
contador_2 = 10

while contador_1 <= 8:
    print(contador_1, contador_2)
    contador_1 += 1
    contador_2 += -1

print('Solução da aula')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)