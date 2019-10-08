from node import Node

class Arvore:

    def __init__(self, root):

        self.root = root

    def get_intersect(self, p1, p2):

        for i in range(len(p1)):

            if len(p2) > i:

                if p1[i] != p2[i]: return i

            else: break

        return -1

    def insere(self, palavra):

        pai = None
        node = self.root
        i = 0

        while 1:

            if type(node) == str:

                pos = self.get_intersect(palavra, node)

                if pos >= 0:

                    if pai is None:

                        l = sorted([palavra, node])

                        self.root = Node(pos, l[0][pos], l[0][:pos])
                        self.root.filhos = l

                        print(self.root)
                        return

                    else:

                        lado = pai.filhos.index(node)

                        l = sorted([palavra, node])

                        pai.filhos[lado] = Node(pos, l[0][pos], l[0][:pos])
                        pai.filhos[lado].filhos = l

                        print(pai.filhos[lado])
                        return




            else:

                prox = node.get(palavra)

                if not prox:

                    pos = self.get_intersect(palavra, node.prefixo)

                    if pos >= 0:

                        if pai is None:

                            self.root = Node(pos,palavra[pos], palavra[:pos])

                            self.root.filhos = [palavra, node] if node.prefixo > palavra else [node, palavra]

                            print(self.root)

                            return

                else:

                    pai = node
                    node = prox

    def check(self, palavra):

        node = self.root

        while 1:

            if type(node) == str:

                return node == palavra

            next = node.get(palavra)

            if next:

                node = next

            else:

                return False








p = Arvore('corno')
p.insere('coro')
p.insere('cornada')
p.insere('ava')
p.insere('cornarada')
p.insere('abelha')
p.insere('a')

print(p.check('a'))



