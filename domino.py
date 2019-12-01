import collections

# NamedTuple para inicializar os parâmetros 'first' e 'second'
# de maneira imutável, simples e com melhor desempenho
DominoBase = collections.namedtuple('DominoBase', ['first', 'second'])


class Domino(DominoBase):
    '''
    Classe Python para objetos que representam um dominó. Cada
    dominó é um ladrilho retangular com uma linha que divide
    sua face em duas extremidades quadradas. Cada extremidade é
    marcada com um valor inteiro, geralmente variando de 0 a 6.

    No Programinó, estas extremidades são formadas por variáveis
    e tipos da programação, através da classe Head, que representa
    cada 'cabeça' ou extremidade do dominó.

    :param int first: valor em uma extremidade
    :param int second: valor na outra extremidade
    :var first: valor em uma extremidade
    :var second: valor na outra extremidade

    .. code-block:: python

        >>> import programino
        >>> from programino import Head
        >>> d = programino.Domino(Head(3.14), Head(False))
        >>> d
        [3.14|False]
        >>> d_inv = d.inverted()
        >>> d_inv
        [Fasle|3.14]
        >>> d == d_inv
        True
        >>> other_d = programino.Domino(Head('Maria'), Head(13))
        >>> d == other_d
        False
        >>> 3.14 in d
        True
    '''

    def inverted(self):
        '''
        :return: um novo Domino, com os mesmos valores, mas com posições invertidas
        '''
        return Domino(self.second, self.first)

    def __str__(self):
        return '[{}|{}]'.format(self.first, self.second)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        # A ordem dos valores não importa
        # ex: Domino(Head(2), Head(True)) == Domino(Head(True), Head(2))
        return (self.heads == other.heads) or \
            (self.inverted_heads == other.inverted_heads)

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        # A ordem dos valores não importa
        # ex: hash(Domino(Head('Casa'), Head(3))) == hash(Domino(Head(3), Head('Casa')))
        return hash(tuple(sorted((self.first, self.second))))

    def __contains__(self, key):
        return (key == self.first) or (key == self.second)

    @property
    def heads(self):
        '''
        :return: uma tupla com os valores das cabeças do Domino
        '''
        return (self.first, self.second)

    @property
    def inverted_heads(self):
        '''
        :return: uma tupla com os valores invertidos das cabeças do Domino
        '''
        return (self.second, self.first)
