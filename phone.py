
# Written by continualintegration.com
# This is for Python version 2.
""" Written by continualintegration.com.  Usage instructions:
    This program needs to be in the same directory as a file called list.txt.
    The content of list.txt can be as follows (with the last line being
    "Zuckerberg, Mark"):

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

	# Use "python phone.py" to run this program.

"""
import re


def phone():
    pad = """This is the keypad.
    Press a number key that corresponds to the letter of the name.
    Enter a minimum of two and a maximum of three numbers.

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

    print pad
    first = raw_input("Please enter the first three letters of the person's last name: ")

    prebook = open('list.txt', 'r')
    book = prebook.read()
    postbook = book.split('\n')
    global i;
    i = -1

    def presearch(digit, i):   #Digit is the key they entered.
	intermediate = []
	finvar = "initial"
	if (digit == '0'):
	  finvar = "***Invalid key error!!!  0 has no letters associated with it. ABORTIVE ERROR"
	elif digit == '1':
	  finvar = "***invalid key error!!!  1 has no letters associated with it. ABORTIVE ERROR."
	elif digit == '2':
	  prevar1 = search('A', i)
	  prevar2 = search('B', i)
	  prevar3 = search('C', i)
	  if (prevar1 == []):
	      if (prevar2 == []):
		  if (prevar3 == []):
		      if (i == 0): place = 'first'
		      if (i == 1): place = 'second'
		      if (i == 3): place = 'third'
		      finvar = '***No name found that starts with an "A", "B", or "C" in the ' + place + ' letter.'
	  if (prevar1 != []): intermediate.extend(prevar1)
	  if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	  if (prevar3 != []): intermediate.extend(prevar3)
	  finvar = intermediate

	elif digit == '3':
	    prevar1 = search('D', i)
	    prevar2 = search('E', i)
	    prevar3 = search('F', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (i == 0): place = 'first'
			if (i == 1): place = 'second'
			if (i == 3): place = 'third'
			finvar = '***No name found that starts with an "D", "E", or "F" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    finvar = intermediate

	elif digit == '4':
	    prevar1 = search('G', i)
	    prevar2 = search('H', i)
	    prevar3 = search('I', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (i == 0): place = 'first'
			if (i == 1): place = 'second'
			if (i == 3): place = 'third'
			finvar = '***No name found that starts with an "G", "H", or "I" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    finvar = intermediate

	elif digit == '5':
	    prevar1 = search('J', i)
	    prevar2 = search('K', i)
	    prevar3 = search('L', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (i == 0): place = 'first'
			if (i == 1): place = 'second'
			if (i == 3): place = 'third'
			finvar = '***No name found that starts with an "J", "K", or "L" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    finvar = intermediate

	elif digit == '6':
	    prevar1 = search('M', i)
	    prevar2 = search('N', i)
	    prevar3 = search('O', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (i == 0): place = 'first'
			if (i == 1): place = 'second'
			if (i == 3): place = 'third'
			finvar = '***No name found that starts with an "M", "N", or "O" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    finvar = intermediate

	elif digit == '7':
	    prevar1 = search('P', i)
	    prevar2 = search('Q', i)
	    prevar3 = search('R', i)
	    prevar4 = search('S', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (prevar4 == []):
			    if (i == 0): place = 'first'
			    if (i == 1): place = 'second'
			    if (i == 3): place = 'third'
			    finvar = '***No name found that starts with an "P", "Q", "R", or "S" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    if (prevar4 != []): intermediate.extend(prevar4)
	    finvar = intermediate

	elif digit == '8':
	    prevar1 = search('T', i)
	    prevar2 = search('U', i)
	    prevar3 = search('V', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (i == 0): place = 'first'
			if (i == 1): place = 'second'
			if (i == 3): place = 'third'
			finvar = '***No name found that starts with an "T", "U", or "V" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    finvar = intermediate

	elif digit == '9':
	    prevar1 = search('W', i)
	    prevar2 = search('X', i)
	    prevar3 = search('Y', i)
	    prevar4 = search('Z', i)
	    if (prevar1 == []):
		if (prevar2 == []):
		    if (prevar3 == []):
			if (i == 0): place = 'first'
			if (i == 1): place = 'second'
			if (i == 3): place = 'third'
			finvar = '***No name found that starts with an "W", "X", "Y", or "Z" in the ' + place + ' letter.'
	    if (prevar1 != []): intermediate.extend(prevar1)
	    if (prevar2 != []): intermediate.extend(prevar2)  # Append would preserve groupings by first letter
	    if (prevar3 != []): intermediate.extend(prevar3)
	    if (prevar4 != []): intermediate.extend(prevar4)
	    finvar = intermediate

	else: print "You cannot enter letters.  You must enter numbers only."
	if finvar == []: finvar = "***No names were found."
	return finvar

    def search(letter, pos):  # Take two parameters a string of 0 to 2 characters and the letter it is searching for
	potential = []
	for line in book.splitlines():
	    if (line[pos] == letter):
	        potential.append(line)
	return potential


    def secondkeyreducer(shortlist, seckey):  # should rename to getnames
	potentiala = []
	ee = len(shortlist)
	x = 0
	while (x < ee):
	    name = shortlist[x]  # name in shortlist:
	    if name == '*': x = x + ee  # get out of while loop if no names were found
	    tt = eliminator(name, seckey, 1)
	    if (tt == 'MARK'): potentiala.append(name)
	    elif (tt == 'FAILED'): quit()
	    else: print ""  # "not adding a name because of 2nd or 3rd key"
	    x = x + 1
	return potentiala

    def thirdkeyreducer(shortlist, thirdkey):  #should rename to getnames
	potentiala = []
	ee = len(shortlist)
	x = 0
	while (x < ee):
	    name = shortlist[x]  # name in shortlist:
	    tt = eliminator(name, thirdkey, 2)
	    if (tt == 'MARK'): potentiala.append(name)
	    elif (tt == 'FAILED'): quit()
	    else: print ""  # "not adding a name because of 2nd or 3rd key"
	    x = x + 1
	if potentiala == []:
	    print "No names were found by the spelling of that name."
	    phone()
	else: print ""  # potentiala #print all potential matches
	return potentiala

    def eliminator(name, seckey, itera):
	val = 'REMOVE'
	if name != '*':
	    if seckey == '0': val = 'FAILED'
	    if seckey == '1': val = 'FAILED'
	    if seckey == '2':
		if name[itera].upper() in ['A', 'B', 'C']: val = 'MARK'
	    if seckey == '3':
		if name[itera].upper() in ['D', 'E', 'F']: val = 'MARK'
	    if seckey == '4':
		if name[itera].upper() in ['G', 'H', 'I']: val = 'MARK'
	    if seckey == '5':
		if name[itera].upper() in ['J', 'K', 'L']: val = 'MARK'
	    if seckey == '6':
		if name[itera].upper() in ['M', 'N', 'O']: val = 'MARK'
	    if seckey == '7':
		if name[itera].upper() in ['P', 'Q', 'R', 'S']: val = 'MARK'
	    if seckey == '8':
		if name[itera].upper() in ['T', 'U', 'V']: val = 'MARK'
	    if seckey == '9':
		if name[itera].upper() in ['W', 'X', 'Y', 'Z']: val = 'MARK'
	return val

    inivar = first[0]
    firstlist = presearch(inivar, 0)
    cc = len(firstlist)

    if len(first) < 2:
	print "you entered too few numbers"
	print "try again"
	phone()

    if len(first) > 3:
	print "you entered too many numbers"
	print "try again"
	phone()

    if first[0].isalpha():
	print "enter numbers only"
	print "Call back again."
	phone()

    if first[1].isalpha():
	print "enter numbers only"
	print "Call back again."
	phone()

    if len(first) == 3:
	if first[2].isalpha():
	    print "enter numbers only"
	    print "Call back again."
	    phone()

    yt = first[1]
    secondlist = secondkeyreducer(firstlist, yt)

    if len(first) == 3:
	   zt = first[2]
	   thirdlist = thirdkeyreducer(secondlist, zt)
	   return thirdlist
    else:
	  return secondlist


toprint = phone()
print toprint
