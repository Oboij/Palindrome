__author__ = 'Simon, Eddie, Mikael'

def isPalindrome(input):
    if input.__len__() < 3:
        return False
    length = input.__len__() / 2 + 1
    input.__len__()
    while length > 0:
       if input[0 + length] == input[input.__len__() - length - 1]:
           length = length -1
       else:
           return False
    return True
    print(input.__len__())

def refineString(input):
    input = input.lower()
    i = 0
    while i < input.__len__():

       if not input[i].isalpha():
           input = input[:i] + input[i + 1:]
           i -=1
       i += 1

    return input

def countPalindrome(input):
    counter = 0
    i = 0
    j = 0
    while i < input.__len__():
        while j <= input.__len__():
            if isPalindrome(input[i: j]):
                counter += 1
            j += 1
        j = i
        i += 1


    return counter

def readStringFromFile(filePath):
    file = open(filePath, 'r')
    return file.read()

def chooseUserInput():
    print "Do you want to read a palindrome from a File or user Input? (F/I): "
    while True:
        choice = raw_input()
        if choice == "":
            break
        if choice == 'F' or choice == 'f':
            return True
        elif choice == 'I' or choice == 'i':
            return False
        else:
            print "Wrong input. Please type again. (F/I)"



print("Type if to check if the word is a Palindrome, press Enter to exit")
while True:
    choice = chooseUserInput()
    if choice == True:
        input = raw_input()
        if input == "":
            break
        input = readStringFromFile(input)
        input = refineString(input)
        print("Number of palindromes: " + str(countPalindrome(input)))
    else:
        input = raw_input()
        if input == "":
            break
        input = refineString(input)
        print("Number of palindromes: " + str(countPalindrome(input)))

#   if isPalindrome(input) == True:
#        print("It is a Palindrome")
#    else:
#        print("It is not a Palindrome")

