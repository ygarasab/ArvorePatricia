from patricia.node import Node
from patricia.helper import get_intersection


class PatriciaTree:

    def __init__(self, root=None):

        """
        Inicia a árvore
        :param str root:
        """

        if type(root) == str:
            root += '$'

        self.root = root

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

        if self.root is None:
            self.root = word
            return

        parent = None
        node = self.root

        while True:

            # Caso nó folha

            if type(node) == str:

                position = get_intersection(word, node)

                # Caso nó folha é root também

                if parent is None:

                    elements = sorted([(ord(word[position]), word), (ord(node[position]), node)])
                    # print(elements)
                    self.root = Node(position, chr(elements[0][0]), elements[0][1][:position])

                    self.root.children = [element[1] for element in elements]

                    # print(self.root)
                    return


                # CASE: default

                else:

                    side = parent.children.index(node)

                    # print(position)

                    elements = sorted([(ord(word[position]), word), (ord(node[position]), node)])

                    # parent.children[side] = Node(position, elements[0][position], elements[0][:position])
                    parent.children[side] = Node(position, chr(elements[0][0]), elements[0][1][:position])
                    parent.children[side].children = [element[1] for element in elements]

                    # print(parent.children[side])
                    return

            else:

                next_node = node.get(word)

                # Caso radix não combina

                if not next_node:

                    position = get_intersection(word, node.radix)

                    elements = sorted([(ord(word[position]), word), (ord(node.radix[position]), node)])

                    # Caso root

                    if parent is None:

                        self.root = Node(position, chr(elements[0][0]), word[:position])

                        self.root.children = [element[1] for element in elements]

                        return

                    else:

                        side = parent.children.index(node)
                        # print(side, parent.children)
                        # print(elements)
                        parent.children[side] = Node(position, chr(elements[0][0]), word[:position])
                        parent.children[side].children = [element[1] for element in elements]

                        return

                # Base de iteração

                else:

                    parent = node
                    node = next_node

    def check(self, word):

        if self.root is None:
            return False

        word += '$'

        node = self.root

        while 1:

            if type(node) == str:
                return node == word

            next_node = node.get(word)
            # print(next_node)
            if next_node:

                node = next_node

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

                    self.root = None
                    return

                else:

                    parent.children.remove(node)
                    new_successor = parent.children[0]

                    if grandparent is None:

                        self.root = new_successor
                        del parent

                        return

                    else:

                        index = grandparent.children.index(parent)
                        grandparent.children[index] = new_successor
                        del parent

                        return

            else:

                next_node = node.get(word)

                if parent is None:

                    parent = node
                    node = next_node

                else:

                    grandparent = parent
                    parent = node
                    node = next_node

    def get_derivatives(self, radix):

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
                    return node.get_derivatives()

                next_node = node.get(radix)

                if next_node:
                    node = next_node
                else:
                    return []

    def __repr__(self):
        if self.root is None:
            return "<Empty PatriciaTree object>"
        else:
            return "<PatriciaTree object>\n" + str(self.root)
