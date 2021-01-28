'''
Summary: This is a program that reads a flat file that is merely a list of books.
Each line of the input file has a book with information about the book.
This line data is separated by colons.

The output of this program shows the ISBN number and the number of authors that the book has.

Usage instructions: change /tmp/newbooks.txt below to the location and name of the input file.
Then run the program with no parameters like this:

$ python authorCounter.py

The input file must be in the correct format.  Here is a sample format:

      isbn123:Brave New World:SCIFI:10-12-2015:huxley
      isbn789:1984:FICTION:10-12-2015:orwell
      isbn333:Habits of the Heart:NONFICTION:9-17-2007:bellah,madsen,sullivan,swidler,tipton

This program assumes that the input file conforms to the template.  For example, there can be no blank lines.
There can be one extraneous comma at the end of the authors' list in that section.
Taken from continualintegration.com
'''

print "ISBN = number of authors"

x = open("/tmp/newbooks.txt", "r")
for line in x:
        sections = line.split(":")
        part1 = sections[0]
        partLast = sections[-1]
        comCount = partLast.count(',')
        endOfS = partLast[-2:-1]
        if endOfS == ',':
                numOfAuthors = comCount
        else:
                numOfAuthors = comCount + 1
        print part1 + ' = %s' % numOfAuthors
