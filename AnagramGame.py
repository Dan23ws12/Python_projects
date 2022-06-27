# Anagram game where an anagram is given and the user is supposed to guess what the original word
# is given a few hints
import random

def readFile(filename):
    """

    :param filename: name of a file
    :return: returns a list all the words in a file
    prerequisite: the file must have one word per line

    """
    wordList = []
    with open(filename, "r") as file:
        for line in file:
            if line != "":
                wordList.append(line[:-1].lower())
    return wordList

def play(wordlist):
    """

    :param wordlist: a list of strings
    :return: Nothing
    """
    replay = "y"
    while (replay == "y") and (len(wordlist) > 0):
        word = random.choice(wordlist)  # a random word
        tempSet = set(wordlist)
        tempSet.discard(word)
        wordlist = list(tempSet)
        print(shuffle(word))
        print("guess the original word")
        guess(word)
        if len(wordlist) > 0:
            replay = input("press y if u want to play again")



def shuffle(word):
    """
    returns an anagram of a given word by shuffling it
    """
    lst = list(word)
    while True:
        random.shuffle(lst)
        shuffled = "".join(lst)
        if shuffled != word:
            return shuffled

def guess(word):
    """
    :param word: any non-empty string
    :return: nothing
    this method is given a word and prompts the user to guess said word by giving
    a limited number of hints
    """
    hint1 = "first character is " + word[0]
    hint2 = "last character is " + word[-1]
    charPos = random.randint(1, len(word) - 1)
    hint3 = "the " + str(charPos) + "th character is " + word[charPos]
    noHintsToGive = 2  # the user can get a max of 2 hints
    noHintsGiven, newGuess = 0, ""
    lstHints = [hint1, hint2, hint3]  # a list of 3 hints
    while newGuess != word:
        if noHintsToGive > noHintsGiven:
            hint = random.choice(lstHints)
            tempSet = set(lstHints)
            tempSet.discard(hint)
            lstHints = list(tempSet)
            noHintsToGive += 1
            newGuess = input(hint).lower()
        else:
            newGuess = input("wrong answer try again").lower()


if __name__ == "__main__":
    play(readFile("anagram.txt"))