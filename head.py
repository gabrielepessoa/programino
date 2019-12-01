def is_a_primitive_type(value):
    return isinstance(value, type)


class Head:
    '''
    Classe Python para objetos que representam uma 'cabeça' ou
    extremidade de um dominó. Como no Programinó as peças são
    formadas por variáveis e tipos da programação, fez-se necessário
    a criação desta classe para definir a equivalência de valores
    que, na realidade, não são iguais.

    :param obj value: valor da cabeça/extremidade

    .. code-block:: python

        >>> from programino import Head
        >>> h1 = Head(3.14)
        >>> h2 = Head(float)
        >>> h1 == h2
        True
    '''

    TRUTHS = ['V', 'True', 'Verdadeiro']
    LIES = ['F', 'False', 'Falso']
    BOOLEANS = TRUTHS + LIES

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):

        if self.value in Head.BOOLEANS:
            self.value = True if self.value in Head.TRUTHS else False

        if other.value in Head.BOOLEANS:
            other.value = True if other.value in Head.TRUTHS else False

        # Verifica se o primeiro valor é um tipo primitivo (int, str, bool)
        if is_a_primitive_type(self.value):

            # Verifica se o segundo valor é um tipo primitivo (int, str, bool)
            if is_a_primitive_type(other.value):

                # Caso ambos sejam tipos primitivos compara diretamente
                # ex: (str, int)
                return self.value == other.value

            else:
                # Caso o segundo seja um valor normal compara com o tipo
                # ex: (bool, True)
                return type(other.value) == self.value

        # Se o primeiro valor não for um tipo primitivo
        # ou seja, um valor normal, como: 12, 'maria', 45.7
        else:

            # Verifica se o segundo valor é um tipo primitivo (int, str, bool)
            if is_a_primitive_type(other.value):

                # Caso o segundo seja um tipo primitivo compara com o tipo
                # ex: (12, int)
                return type(self.value) == other.value

            else:
                # Caso o segundo seja um valor normal compara o tipo dos dois
                # ex: (12, 15)
                return type(self.value) == type(other.value)

        return False
