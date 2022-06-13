# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference^ (Elementos que estão nos dois sets mas não em ambos)


# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 | s2
#
# print(s3)

l1 = ['Danniel', 'João', 'Maria','Luiz']
l2 = ['Danniel', 'Maria', 'Maria', 'Luiz','João', 'Luiz', 'Luiz', 'Danniel']

if set(l1) == set(l2):
    print('L1 é igual a l2')
else:
    print('L1 é diferente de l2')