from node import Node

class Arvore:

    def __init__(self, root):

        """
        Inicia a árvore
        :param str root:
        """

        self.root = root + "$"


    def get_intersect(self, p1, p2):

        """
        Buca o ponto onde duas strings de diferenciam
        :param str p1:
        :param str p2:
        :return int:
        """

        for i in range(len(p1)):

            if len(p2) > i:

                if p1[i] != p2[i]: return i


    def insere(self, palavra):

        """
        Insere uma string na árvore
        :param str palavra:
        :return None:
        """

        palavra += '$'

        if self.check(palavra):

            print("[Erro] Palavra já inserida")

        pai = None
        node = self.root
        i = 0

        while 1:

            # Caso nó folha

            if type(node) == str:

                pos = self.get_intersect(palavra, node)

                # Caso nó folha é raiz também

                if pai is None:

                    l = sorted([palavra, node])

                    self.root = Node(pos, l[0][pos], l[0][:pos])
                    self.root.filhos = l

                    print(self.root)
                    return


                # Caso padrão

                else:

                    lado = pai.filhos.index(node)

                    l = sorted([palavra, node])

                    # pai.filhos[lado] = Node(pos, l[0][pos], l[0][:pos])
                    pai.filhos[lado] = Node(pos, l[0][pos], l[0][:pos])
                    pai.filhos[lado].filhos = l

                    print(pai.filhos[lado])
                    return



            else:

                prox = node.get(palavra)

                # Caso prefixo não combina

                if not prox:

                    pos = self.get_intersect(palavra, node.prefixo)
                    l = sorted([palavra, node.prefixo])

                    # Caso raiz

                    if pai is None:

                        self.root = Node(pos,l[0][pos], palavra[:pos])

                        self.root.filhos = [palavra, node] if node.prefixo > palavra else [node, palavra]

                        return

                    else:

                        lado = pai.filhos.index(node)
                        pai.filhos[lado] = Node(pos, l[0][pos], palavra[:pos])
                        pai.filhos = [palavra, node] if node.prefixo > palavra else [node, palavra]

                        return

                # Base de iteração

                else:

                    pai = node
                    node = prox


    def check(self, palavra):

        palavra += '$'

        node = self.root

        while 1:

            if type(node) == str:

                return node == palavra

            next = node.get(palavra)
            print(f"next: {next}")
            if next:

                node = next

            else:

                return False


    def remove(self, palavra):

        if not self.check(palavra):

            print("[Erro] Palavra não encontrada")
            return

        palavra += '$'

        avo = None
        pai = None
        node = self.root

        while 1:

            if type(node) == str:

                if pai is None:

                    print("[Erro] Não é possível remover único item da arvore")
                    return

                else:

                    pai.filhos.remove(node)
                    novo_sucessor = pai.filhos[0]

                    if avo is None:

                        self.root = novo_sucessor
                        del pai

                        return

                    else:

                        index = avo.filhos.index(pai)
                        avo.filhos[index] = novo_sucessor
                        del pai

                        return

            else:

                prox = node.get(palavra)

                if pai is None:

                    pai = node
                    node = prox

                else:

                    avo = pai
                    pai = node
                    node = prox










# p = Arvore('corno')
# p.insere('coro')
# p.insere('cornada')
# p.insere('ava')
# p.insere('cornarada')
# p.insere('abelha')
# p.insere('ab')
#
# p.remove('abelha')
#
# print(p.check('ava'))

p = Arvore("abacate")
p.insere("abaetetuba")
p.insere("aba")
p.insere("abacaxi")
p.insere("amanda")
p.check("amanda")