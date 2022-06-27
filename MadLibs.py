# Mad Libs projects
#String concatenation
#d
def userInputInt():
    print("enter a number")
    index = input()
    prntStr = "u entered the number : {}"
    print(prntStr.format(index))

def userInputStr():
    print("enter a word or letter")
    string = input()
    prntStr = "u entered the word/letter : {}"
    print(prntStr.format(string))

if __name__ == '__main__':
    userInputStr()
    userInputInt()