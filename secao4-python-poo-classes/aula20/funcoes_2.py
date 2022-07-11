"""..."""

variavel_1 = 'valor 1'

def soma(x, y):
    """soma x e y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y


def multiplica(x, y, z=None):
    """Multiplica x, y, z

    Multiplica x, y e z. O progrmador por omitir a variável z caso não tenha
    necessidade de usá-la.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :param z: Número 3 (optional)
    :type z: int, float or None

    :return: A soma entre x e y
    :rtype: int or float
    """
    if z:
        return x * y
    else:
        return x * y * z


variavel_1 = 'valor 2'
variavel_2 = 'valor 3'
variavel_3 = 'valor 4'