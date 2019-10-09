from patricia import *
from random import shuffle

def load_dict(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip("\n") for line in file.readlines()]

alphabet = "abcdefghijklmnopqrstuvwxyz"


dictionary = load_dict("./dictionaries/palavras.txt")

new_dictionary = []
problem = False
for word in dictionary:
    for character in word.lower():
        if character not in alphabet:
            problem = True
            break
    if not problem:
        new_dictionary.append(word)
    else:
        problem = False

load = new_dictionary.copy()
check = new_dictionary.copy()
remove = new_dictionary.copy()

shuffle(load)
shuffle(check)
shuffle(remove)

tree = PatriciaTree(load[0])

print("Inserindo...")

for word in load[1:]:
    #print(f"Inserindo {word}...")
    tree.insert(word)
    if not tree.check(word):
        raise ValueError(f"Não encontrei a word {word}!")

print("Verificando...")

for word in check:
    if not tree.check(word):
        raise ValueError("Não consegui verificar!")

print("Removendo...")

# for word in remove[1:]:
#     #print(f"Removendo {word}...")
#     tree.remove(word)
#     if tree.check(word):
#         raise ValueError("wtf")
#
print("Sucesso.")


# p = Arvore("abacate")
'''

p.insert("abaetetuba")
p.insert("abacaxi")
p.check("abacate")
p.check("abacaxi")
p.check("abaetetuba")
p.insert("amanda")

p.insert('chocolate')
p.insert('churros')
p.insert('chocante')
p.insert('chocomovel')'''
