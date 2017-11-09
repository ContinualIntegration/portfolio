# Tic-tac-toe game in Python. Written by continualintegration.com.
print "This is a two player game of tictactoe.  One person can pretend to be the other player."
print "Both players should share a keyboard and monitor."
print "The legend for squares in the grid is as follows: "
print "                                                                "
print "***************************************************************"
print "ltc is left-top-corner, tm is top-middle, rtc is right-top-corner"
print "lm is left-column-middle-row, c is center, mr is middlerow-right-column"
print "lbc is left-bottom-corner, bm is bottom-middle, rbc is right-bottom-corner"
print "***************************************************************"
print "                                                                "
print "Enter a cell based on the legend above."

r = 1
mark = 'z'
goodlist = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

first = raw_input("Player 1, please enter which location you want to mark with X: ")
a = b = c = d = e = f = g = h = i = j = ' '
w, hh = 8, 5;
a, b, c, d, e, f, g, h, i, j = ' ', ' ',' ', ' ',' ', ' ',' ', ' ',' ', ' '
board = [[0 for x in range(w)] for y in range(hh)]

board[1][0]='|'
board[1][1]= a
board[1][2]= '|'
board[1][3]= b
board[1][4]= '|'
board[1][5]= c
board[1][6]= '|'

board[2][0]='|'
board[2][1]= d
board[2][2]= '|'
board[2][3]= e
board[2][4]= '|'
board[2][5]= f
board[2][6]= '|'

board[3][0]='|'
board[3][1]= g
board[3][2]= '|'
board[3][3]= h
board[3][4]= '|'
board[3][5]= i
board[3][6]= '|'


toprow = ''
midrow = ''
bottomrow = ''

def printer(goodlist) :
  board[1][0]='|'
  board[1][1]= goodlist[0]
  board[1][2]= '|'
  board[1][3]= goodlist[1]
  board[1][4]= '|'
  board[1][5]= goodlist[2]
  board[1][6]= '|'

  board[2][0]='|'
  board[2][1]= goodlist[3]
  board[2][2]= '|'
  board[2][3]= goodlist[4]
  board[2][4]= '|'
  board[2][5]= goodlist[5]
  board[2][6]= '|'

  board[3][0]='|'
  board[3][1]= goodlist[6]
  board[3][2]= '|'
  board[3][3]= goodlist[7]
  board[3][4]= '|'
  board[3][5]= goodlist[8]
  board[3][6]= '|'
  toprow = ''
  midrow = ''
  bottomrow = ''
  for x in range(0, 7):
     toprow = toprow + board[1][x]
     midrow = midrow + board[2][x]
     bottomrow = bottomrow + board[3][x]
  print "-------"
  print toprow
  print midrow
  print bottomrow
  print "-------"
  return


def marker(loc, mark, r):
  if (loc == 'ltc'): a=mark; callagain(loc, r)
  elif (loc == 'tm'): b=mark; callagain(loc, r)
  elif (loc == 'tm'): c=mark; callagain(loc, r)
  elif (loc == 'rtc'): d=mark; callagain(loc, r)
  elif (loc == 'lm'): e=mark; callagain(loc, r)
  elif (loc == 'c'): f=mark; callagain(loc, r)
  elif (loc == 'mr'): g=mark; callagain(loc, r)
  elif (loc == 'lbc'): h=mark; callagain(loc, r)
  elif (loc == 'bm'): i=mark; callagain(loc, r)
  elif (loc == 'rbc'): j=mark; callagain(loc, r);
  else: print "************Invalid input******************"; r = r -1;

def checker(goodlist):
  for x3 in range(1,4): #the variable's name is "x3".  This section is for horizontal wins.
    if board[x3][1] == board[x3][3]:
      if board[x3][3] == board[x3][5]:
        if board[x3][5] == 'X': print "Player 1 Wins!!!!!"; var1 = "stop"; quit()
        elif board[x3][5] == 'O': print "Player 2 Wins!!!!!"; var1 = "stop"; quit()
        else: var1 = "go"
  for y3 in range(1,6):   #the variable's name is "y3"   This section is for vertical wins.
    if board[1][y3] == board[2][y3]:
      if board[2][y3] == board[3][y3]:
        if board[3][y3] == 'X': print "Player 1 Wins!!!!!"; var1 = "stop";  quit()
        elif board[3][y3] == 'O': print "Player 2 Wins!!!!!"; var1 = "stop"; quit()
        else: var1 = "go"
  # Diagonal checking below.
  if board[1][1] == board[2][3]:
    if board[2][3] == board[3][5]:
      if board[3][5] == 'X': print "Player 1 Wins!!!!!"; var1 = "stop"; quit()
      elif board[3][5] == 'O': print "Player 2 Wins!!!!!"; var1 = "stop"; quit()
      else: var1 = "go"
 if board[1][5] == board[2][3]:
    if board[2][3] == board[3][1]:
      if board[3][1] == 'X': print "Player 1 Wins!!!!!"; var1 = "stop"; quit()
      elif board[3][1] == 'O': print "Player 2 Wins!!!!!"; var1 = "stop"; quit()
      else: var1 = "go"
  return var1


def playeralt(let, r):
  if checker(goodlist) == "go":
    if r % 2 == 0:
      mark = 'X'
      call2(let, mark, r)
      if aw == "go": print "Player 2, where should an O go?"
    else:
      mark = 'O'
      call2(let, mark, r)
      if aw == "go": print "Player 1, where should an X go?"
  else:
      quit()

def callagain(let, r):
  a = checker(goodlist)
  playeralt(let, r)

def call2(let, mark, r):
  if (let == 'ltc'): subcall2(let, mark, r, 0);
  elif (let == 'tm'): subcall2(let, mark, r, 1); #goodlist[1]=mark;
  elif (let == 'rtc'): subcall2(let, mark, r, 2); #goodlist[2]=mark;
  elif (let == 'lm'): subcall2(let, mark, r, 3);  #goodlist[3]=mark;
  elif (let == 'c'): subcall2(let, mark, r, 4); #goodlist[4]=mark;
  elif (let == 'mr'): subcall2(let, mark, r, 5); #goodlist[5]=mark;
  elif (let == 'lbc'): subcall2(let, mark, r, 6); #goodlist[6]=mark;
  elif (let == 'bm'): subcall2(let, mark, r, 7); #goodlist[7]=mark;
  elif (let == 'rbc'): subcall2(let, mark, r, 8); #goodlist[8]=mark;
  else: print "*****************Invalid input************"; r = r -1;
  printer(goodlist)
  checker(goodlist)
  r += 1
  print "********************************"
  if r % 2 == 0:
    player = "Player 1"; md = 'X'
  else: player = "Player 2"; md = 'O';
  loc = raw_input(player + " please enter which location you want to mark with an " + md + ": ")
  checker(goodlist)
  callagain(loc, r) #marker(loc, mark, r)

def subcall2(let, mark, r, glnum):
  if (goodlist[glnum] == ' '): goodlist[glnum]=mark;
  else:
      print "That square was already taken. Please try again!"
      print "Player with " + mark + " needs to go again."
      if r % 2 == 0:
        player = "Player 1"; md = 'X'
      else: player = "Player 2"; md = 'O';
      loc = raw_input(player + " please enter which location you want to mark with an " + md + ": ")
      checker(goodlist)
      callagain(loc, r)

marker(first, 'X', 0)
