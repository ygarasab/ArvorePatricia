class Node:

    def __init__(self, pos, val, prefixo):

        """
        Unidade basica
        :param int pos:
        :param str val:
        :param str prefixo:
        """

        self.filhos = [None, None]

        self.prefixo = prefixo
        self.pos = pos
        self.val = ord(val)

    def get(self, palavra):

        if palavra[:self.pos] != self.prefixo or len(palavra) <= self.pos: return 0

        valor = ord(palavra[self.pos])

        if valor <= self.val:
        #if valor < self.val:

            print("Esquerda!")
            return self.filhos[0]

        print("Direita!")
        return self.filhos[1]

    def __repr__(self):

        return "[{}|{}]".format(self.pos, chr(self.val))