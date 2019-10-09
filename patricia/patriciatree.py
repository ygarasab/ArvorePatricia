from patricia.node import Node


class PatriciaTree:

    def __init__(self, root):

        """
        Inicia a árvore
        :param str root:
        """

        self.root = root + "$"


    def get_intersection(self, word_one, word_two):

        """
        Buca o ponto onde duas strings de diferenciam
        :param str word_one:
        :param str word_two:
        :return int:
        """
        for i in range(len(word_one)):


            if len(word_two) > i:

                if word_one[i] != word_two[i]: return i


    def insert(self, word):

        """
        Insere uma string na árvore
        :param str word:
        :return None:
        """

        # print("Inserindo %s" % word)

        if self.check(word):

            raise ValueError(f"The word {word} has already been inserted.")

        word += '$'

        

        pai = None
        node = self.root
        i = 0

        while 1:

            # Caso nó folha

            if type(node) == str:

                pos = self.get_intersection(word, node)



                # Caso nó folha é root também

                if pai is None:

                    l = sorted([(ord(word[pos]), word), (ord(node[pos]), node)])
                   # print(l)
                    self.root = Node(pos, chr(l[0][0]), l[0][1][:pos])
                    self.root.children = [k[1] for k in l]

                    #print(self.root)
                    return


                # Caso padrão

                else:

                    lado = pai.children.index(node)

                   # print(position)

                    l = sorted([(ord(word[pos]), word), (ord(node[pos]), node)])

                    # pai.children[lado] = Node(position, l[0][position], l[0][:position])
                    pai.children[lado] = Node(pos, chr(l[0][0]), l[0][1][:pos])
                    pai.children[lado].children = [k[1] for k in l]

                   # print(pai.children[lado])
                    return



            else:

                prox = node.get(word)

                # Caso radix não combina

                if not prox:

                    pos = self.get_intersection(word, node.radix)

                    l = sorted([(ord(word[pos]), word), (ord(node.radix[pos]), node)])

                    # Caso root

                    if pai is None:

                        self.root = Node(pos, chr(l[0][0]), word[:pos])

                        self.root.children = [k[1] for k in l]

                        return

                    else:

                        lado = pai.children.index(node)
                       # print(lado, pai.children)
                       # print(l)
                        pai.children[lado] = Node(pos, chr(l[0][0]), word[:pos])
                        pai.children[lado].children = [k[1] for k in l]

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
            #print(next)
            if next:

                node = next

            else:

                return False


    def remove(self, word):

        if not self.check(word):

            raise ValueError(f"Word {word} not found.")

        word += '$'

        grandparent = None
        parent = None
        node = self.root

        while 1:

            if type(node) == str:

                if parent is None:

                    raise ValueError("The PATRICIA Tree cannot be empty.")

                else:

                    parent.children.remove(node)
                    new_sucessor = parent.children[0]

                    if grandparent is None:

                        self.root = new_sucessor
                        del parent

                        return

                    else:

                        index = grandparent.children.index(parent)
                        grandparent.children[index] = new_sucessor
                        del parent

                        return

            else:

                next = node.get(word)

                if parent is None:

                    parent = node
                    node = next

                else:

                    grandparent = parent
                    parent = node
                    node = next

    def derivates(self, radix):

        """
        Exibe folhas derivadas de determinado radix
        :param str radix:
        :return str[]:
        """

        size = len(radix)
        node = self.root

        while 1:

            if type(node) == str:

                if node[:size] == radix:

                    return [node[:-1]]

                else:

                    return []

            else:

                if node.radix == radix or node.radix[:size] == radix:

                    return node.derivates()

                next = node.get(radix)

                if next: node = next
                else: return []