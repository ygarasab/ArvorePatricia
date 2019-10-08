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


    def derivados(self):

        derivados = []

        for i in self.filhos:

            if type(i) == str: derivados.append(i[:-1])

            else: derivados += i.derivados()

        return derivados


    def __repr__(self):

        return "[{}|{}]".format(self.pos, chr(self.val))