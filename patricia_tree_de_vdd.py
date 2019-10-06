class Node():
    def __init__(self, advance, compare_w, left=None, right=None):
        self.advance  = advance
        self.compare_w = compare_w
        self.left = left
        self.right = right

    def __str__(self):
        return str('adv: {}, cw: {}'.format(self.advance, self.compare_w))

class PatriciaTree():
    def __init__(self, *args):
        self.root = None
        self.n_words = 1
        for arg in args:
            self.insert(*args)


    def insert(self, word, word2=None):
        if not self.root:
            if not word2:
                raise ValueError('No root, need two arguments for first insertion.')
            for i in range(min([len(word), len(word2)])):
                if word[i] == word2[i]:
                    continue
                else:
                    if word[i] < word2[i]:
                        self.root = Node(i, word[i], word, word2 )
                    else:
                        self.root = Node(i, word[i], word2, word )

                

    def check(self, word):
        if not self.root:
            raise ValueError('The tree is empty.')
        cur_char = self.root
        for letter in word:
            if letter in cur_char.next_chars:
                cur_char = cur_char.next_chars[cur_char.next_chars.index(letter)]
            else:
                return False
        return cur_char.is_final

p = PatriciaTree('corno', 'corro')