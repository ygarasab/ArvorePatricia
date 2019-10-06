class Char():
    def __init__(self, char, pre_char=None):
        self.char = char
        self.pre_char = pre_char
        self.next_chars = []
        self.is_final = False
    
     def __eq__(self, other):
        if isinstance(other,Character): 
            return self.character == other.character and self.previous_character == other.previous_character and self.next_characters == other.next_characters
        elif isinstance(other,str): 
            return self.character == other
        else: 
            return False
    
    def __str__(self):
        return str(self.char)

class PatriciaTree():
    def __init__(self, *args):
        self.root = None
        self.n_words = 1
        for arg in args:
            self.insert(arg)


    def insert(self, word):
        if not self.root:
            self.root = Char(None)
        cur_char = self.root
        for letter in word:
            if letter in cur_char.next_chars:
                cur_char.next_chars[cur_char.next_chars.index(letter)]
            else:
                cur_char.next_chars.append(Char(letter, cur_char))
                for index in range(len(cur_char.next_chars)):
                    if cur_char.next_chars[index].char == letter:
                        cur_char = cur_char.next_chars[index]
                        break

        if cur_char.is_final == False:
            cur_char.is_final = True
            self.n_words += 1

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

p = PatriciaTree('corno')
