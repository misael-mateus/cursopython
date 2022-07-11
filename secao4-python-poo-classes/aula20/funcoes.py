"""..."""

variavel_1 = 'valor 1'

def soma(x, y):
    """soma x e y"""
    return x + y


def multiplica(x, y, z=None):
    """Multiplica x, y, z

    Multiplica x, y e z. O progrmador por omitir a variável z caso não tenha
    necessidade de usá-la.
    """
    if z:
        return x * y
    else:
        return x * y * z


variavel_1 = 'valor 2'
variavel_2 = 'valor 3'
variavel_3 = 'valor 4'