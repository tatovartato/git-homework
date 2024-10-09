def GetDict(word):
    if not isinstance(word, str):
        return False
    countdict = {}
    for key in word:
        if key in countdict:
            countdict[key] +=1
        else:
            countdict[key] = 1
    return countdict
print(GetDict("tatoo"))
    