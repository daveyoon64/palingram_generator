import load_dictionary
from pathlib import Path

FILE = "master.txt"
path = Path.cwd() / "palingram" / FILE

word_list = load_dictionary.load(path)
palindrome_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindrome_list.append(word)
print(f"Number of palindromes found: {len(palindrome_list)}\n")
print(*palindrome_list, sep='\n')