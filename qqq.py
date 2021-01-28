# This is for Python 3.  It was written by continualintegration.com
# It requires that a file named list.txt be in the same directory.
""" Written by continualintegration.com.  Usage instructions:
    This program needs to be in the same directory as a file called list.txt.
    You would run the program like this: "python phone.py"
    The content of list.txt can be as follows:

Allen, Paul
Ballmer, Steve
Bell, Gordon
Berners-Lee, Tim
Bosack, Leonard
Brin, Sergey
Ellison, Larry
Gates, Bill
Jobs, Steve
Hopper, Grace
Lerner, Sandy
Li, Bruce
Moore, Gordon
Page, Larry
Torvalds, Linus
Turing, Alan
Watson, Thomas
Wozniack, Steve
Zuckerberg, Mark
"""


def phone():
    pad = """This is the keypad.  Press a number key that corresponds to the
    letter of the name. Enter a minimum of two and a maximum of three numbers.

    1
    2 ABC
    3 DEF
    4 GHI
    5 JKL
    6 MNO
    7 PQRS
    8 TUV
    9 WXYZ
    0"""

    print(" ")
    print(pad)
    prompt = "Please enter the first three letters of the person's last name: "
    first = input(prompt)

    if len(first) < 2:
        print("you entered too few numbers")
        print("Please try again")
        return 'DO_OVER_FLAG'

    if len(first) > 3:
        print("you entered too many numbers")
        print("Please try again")
        return 'DO_OVER_FLAG'

    if first[0] == '0':
        print("0 is not a valid key.")
        print("Please try again.")
        return 'DO_OVER_FLAG'

    if first[0] == '1':
        print("1 is not a valid key.")
        print("Please try again.")
        return 'DO_OVER_FLAG'

    if first[0].isalpha():
        print("enter numbers only")
        print("Please try again.")
        return 'DO_OVER_FLAG'

    if first[1].isalpha():
        print("enter numbers only")
        print("Please try again.")
        return 'DO_OVER_FLAG'

    if len(first) == 3:
        if first[2].isalpha():
            print("enter numbers only")
            print("Please try again.")
            return 'DO_OVER_FLAG'

    print("This was valid input")
    return first


def telparser(astring):
    if astring[0] == '2':
        firstletter = 'ABC'
    if astring[0] == '3':
        firstletter = 'DEF'
    if astring[0] == '4':
        firstletter = 'GHI'
    if astring[0] == '5':
        firstletter = 'JKL'
    if astring[0] == '6':
        firstletter = 'MNO'
    if astring[0] == '7':
        firstletter = 'PQRS'
    if astring[0] == '8':
        firstletter = 'TUV'
    if astring[0] == '9':
        firstletter = 'WXYZ'

    if astring[1] == '2':
        secondletter = 'ABC'
    if astring[1] == '3':
        secondletter = 'DEF'
    if astring[1] == '4':
        secondletter = 'GHI'
    if astring[1] == '5':
        secondletter = 'JKL'
    if astring[1] == '6':
        secondletter = 'MNO'
    if astring[1] == '7':
        secondletter = 'PQRS'
    if astring[1] == '8':
        secondletter = 'TUV'
    if astring[1] == '9':
        secondletter = 'WXYZ'

    if len(astring) > 2:
        if astring[2] == '2':
            thirdletter = 'ABC'
        if astring[2] == '3':
            thirdletter = 'DEF'
        if astring[2] == '4':
            thirdletter = 'GHI'
        if astring[2] == '5':
            thirdletter = 'JKL'
        if astring[2] == '6':
            thirdletter = 'MNO'
        if astring[2] == '7':
            thirdletter = 'PQRS'
        if astring[2] == '8':
            thirdletter = 'TUV'
        if astring[2] == '9':
            thirdletter = 'WXYZ'
        return firstletter, secondletter, thirdletter
    else:
        return firstletter, secondletter


def finder(content):
    goodlist = []
    finallist = []
    try:      # It is easy to forget that the program needs an extra file.
        open('list.txt', 'r') 
    except FileNotFoundError:
        print("")
        print("*********************************")
        print("FATAL ERROR")
        print("You need to create a list.txt file that is in the same directory as this program.")
        print("See this web page: http://www.continualintegration.com/miscellaneous-articles/how-do-you-write-a-python-program-to-simulate-a-dial-by-name-directory/")
        print("Step #1 of the solution in the web page above will help you.")
        print("The program will now exit.")
        quit()
    prebook = open('list.txt', 'r')
    book = prebook.read()
    postbook = book.split('\n')
    postbook = postbook[:-1]
    d00 = str(content[0][0])
    d01 = str(content[0][1])
    d02 = str(content[0][2])
    if len(content[0]) > 3:
        d03 = str(content[0][3])

    for item in postbook:
        item0 = str(item[0])
        # Test 1st letter of last name against each character of 3 letters of 1st key.
        if d00.upper() == item0.upper():
            goodlist.append(item)
        elif d01.upper() == item0.upper():
            goodlist.append(item)
        elif d02.upper() == item0.upper():
            goodlist.append(item)
        else:
            if len(content[0]) > 3:
                if d03.upper() == item0.upper():
                    goodlist.append(item)

    for item in goodlist:
        item1 = str(item[1])
        d10 = str(content[1][0])
        d11 = str(content[1][1])
        d12 = str(content[1][2])
        if len(content[1]) > 3:
            d13 = str(content[1][3])

        # Test 2nd letter of last name against the 3 letters of second key.
        if d10.upper() == item1.upper():
            finallist.append(item)
        elif d11.upper() == item1.upper():
            finallist.append(item)
        elif d12.upper() == item1.upper():
            finallist.append(item)
        else:
            if len(content[1]) > 3:
                if d13.upper() == item1.upper():
                    finallist.append(item)
    if len(finallist) == 0:
        finallist.append("No names matched that entry.")

    return finallist


try:      # It is easy to forget that the program needs an extra file.
    toprint = phone()
except FileNotFoundError:
    print("")
    print("*********************************")
    print("FATAL ERROR")
    print("You need to create a list.txt file that is in the same directory as this program.")
    print("See this web page: http://www.continualintegration.com/miscellaneous-articles/how-do-you-write-a-python-program-to-simulate-a-dial-by-name-directory/")
    print("Step #1 of the solution in the web page above will help you.")
    print("The program will now exit.")
    quit()

while toprint == 'DO_OVER_FLAG':
    toprint = phone()


intermed = telparser(toprint)

r = finder(intermed)
print("We searched for matches and we found ...")
for x in r:
    print(x)
