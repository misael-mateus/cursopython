carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))


# total = 0
# for produto in carrinho:
#     total += produto[1]
#
# print(total)

# total = []
# for produto in carrinho:
#     total.append(produto[1])
#
# print(sum(total))

# Solução com list Comprehension
total = sum([float(y) for x, y in carrinho])

print(total)