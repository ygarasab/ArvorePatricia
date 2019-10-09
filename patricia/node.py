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


    def derivates(self):

        derivates = []

        for i in self.children:

            if type(i) == str: derivates.append(i[:-1])

            else: derivates += i.derivates()

        return derivates


    def __repr__(self):

        return "[{}|{}]".format(self.position, chr(self.value))