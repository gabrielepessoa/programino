def is_a_primitive_type(value):
    return isinstance(value, type)


TRUTHS = ['V', 'True', 'Verdadeiro']
LIES = ['F', 'False', 'Falso']
BOOLEANS = TRUTHS + LIES

#Classe criada para verificar cabeça por cabeça do programinó
class Head:

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):

        if self.value in BOOLEANS:
            self.value = True if self.value in TRUTHS else False

        if other.value in BOOLEANS:
            other.value = True if other.value in TRUTHS else False

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

    def __str__(self):
        return str(self.value)
