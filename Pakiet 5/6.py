wordsList = ['autokar', 'okno', 'auto', 'kusza', 'armia', 'odlew']
def checkA(wordsList):
    if wordsList[0] == "a":
        return True
    return False
def out(f):
    for x in f:
        print(x)

filtered = filter(checkA, wordsList)
out(filtered)