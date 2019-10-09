class Node:

    def __init__(self, position, value, radix):

        """
        Unidade basica
        :param int position:
        :param str value:
        :param str radix:
        """

        self.children = [None, None]

        self.radix = radix
        self.position = position
        self.value = ord(value)

    def get(self, word):

        if word[:self.position] != self.radix or len(word) <= self.position: return 0

        value = ord(word[self.position])

        if value <= self.value:
        #if value < self.value:

            #print("Esquerda!")
            return self.children[0]

        #print("Direita!")
        return self.children[1]


    def get_derivatives(self):

        derivatives = []

        for child in self.children:

            if type(child) == str: derivatives.append(child[:-1])

            else: derivatives += child.derivates()

        return derivatives


    def __repr__(self):

        return "[{}|{}]".format(self.position, chr(self.value))