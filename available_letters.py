def getAvailableLetters(lettersGuessed):
    all_str = 'abcdefghijklmnopqrstuvwxyz'
    ava_ltrs = ''
    for i in all_str:
        if i not in lettersGuessed:
            ava_ltrs += i
    return ava_ltrs

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))