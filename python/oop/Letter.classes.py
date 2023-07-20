class LetterTests:

    def __init__(self, inputStringOfLetters):
        self.stringOfLetters = inputStringOfLetters

    def testLetter(self, inputLetter):
        if inputLetter.upper() in self.stringOfLetters:
            return True
        else:
            return False


horiSym = LetterTests("BCDEHIKOX")

userLetter = ''

while userLetter != "0":
    userLetter = input("Please enter a single character, 0 to quit: ")
    print("Is horizontally symmetrical: ", horiSym.testLetter(userLetter))
