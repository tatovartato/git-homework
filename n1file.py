def UniqueLetters(word):
    if not isinstance(word, str):
        return False
    if len(word) == len(set(word)):
        return True
    else:
        return False
print(UniqueLetters(3))