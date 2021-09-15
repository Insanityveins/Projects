def splitIt(phrase, charact):
    # split the string at the given character and then return it
    stringList = phrase.split(charact)
    return stringList


def palindrome(word):
    # iterate through the given string backwards and add it to the reverse string and tell if it's a palindrome
    revString = ''
    for x in range(len(word) - 1, -1, -1):
        revString += word[x]
    if revString == word:
        print("Your string is a palindrome.")
    else:
        print("Your string is not a palindrome.")


def changeToNumber(word):
    # puts each letter in a list and then loops throughout the list to display each number value
    list = []
    ordString = ''
    # adds each letter of word to the list
    for x in range(len(word)):
        list.append(word[x])
    # add the num value of each letter to the string along with '-' and leave out '-' for the last one
    for x in range(len(list)):
        ordString = ordString + str(ord(list[x]))
        if x != len(list) - 1:
            ordString = ordString + "-"
    print(ordString)


# get a string from the user and a char to split the string and call splitIt
string = input("Enter a string you would like to split: ")
char = input("Enter the character you want use to split the string: ")
splitString = splitIt(string, char)
print(f"Your split string is {splitString}")

# get a string from the user to see if it's a palindrome
palinString = input("\nEnter a string to test if it's a palindrome: ")
# make the string lowercase so it can be the same if caps are entered in
lowerPalinString = palinString.lower()
palindrome(lowerPalinString)

# get a string to show the numeric value for
numString = input("\nEnter a word to see the numeric value for it: ")
changeToNumber(numString)
