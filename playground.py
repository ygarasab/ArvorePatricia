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

print("Inserting...")

for word in load[1:]:
    # print(f"Inserting {word}...")
    tree.insert(word)
    if not tree.check(word):
        raise ValueError(f"Couldn't find {word}!")

print("Verifying...")

for word in check:
    # print(f"Verifying {word}...")
    if not tree.check(word):
        raise ValueError(f"Couldn't verify {word}!")

print("Removing...")

for word in remove:
    # print(f"Removing {word}...")
    tree.remove(word)
    if tree.check(word):
        raise ValueError("Couldn't remove {word}!")

print("Success.")

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
