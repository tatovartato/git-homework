def ReversString(word):
    if not isinstance(word, str):
        return False
    reversestring = ""
    for i in word:
        reversestring = i + reversestring
    return reversestring
print(ReversString("nika maaaaaas"))
    