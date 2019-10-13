import load_dictionary
from pathlib import Path

DICTIONARY = "master.txt"

def find_palingrams(file):
    path = Path.cwd() / 'palingram' / file
    master = set(load_dictionary.load(path))
    palingrams = []
    for word in master:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in master:
                    palingrams.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in master:
                    palingrams.append((rev_word[:end-i], word))
    return palingrams

palingrams = find_palingrams(DICTIONARY)
palingrams_sorted = sorted(palingrams)
print(f"Number of palingrams = {len(palingrams_sorted)}\n")
# for first, second in palingrams_sorted:
#     print(f"{first} {second}")