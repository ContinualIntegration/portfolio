'''
Title: emailgetter.py
Summary: returns email addresses in a ready to use format.
This program takes a text file with email addresses that are separate by spaces and carriage returns.  
It returns to the screen email addresses with semicolons after them.

Usage instructions: Put this file in a directory with a source text file.  Call the source file email.txt.
Taken from continualintegration.com
'''

with open('email.txt', 'r') as a:
        for b in a:
                if '@' in b:   #operate only on lines with "@"
                        c = b.split()  #split up words on line
                        for d in c:    #iterate through characters of words
                                if '@' in d:  #if email address,
                                        print d+';' #print email address
