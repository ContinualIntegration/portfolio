# Tic-tac-toe game in Ruby. Written by continualintegration.com.
# We know Ruby is object-oriented.  Ideally we will re-write this to encapsulate all logic in objects.
puts "This is a two player game of tictactoe.  One person can pretend to be the other player."
puts "Both players should share a keyboard and monitor."
puts "The legend for squares in the grid is as follows: "
puts "                                                                "
puts "***************************************************************"
puts "ltc is left-top-corner, tm is top-middle, rtc is right-top-corner"
puts "lm is left-column-middle-row, c is center, mr is middlerow-right-column"
puts "lbc is left-bottom-corner, bm is bottom-middle, rbc is right-bottom-corner"
puts "***************************************************************"
puts "                                                                "
puts "Enter a cell based on the legend above."
board = Array[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def markboard(pos, play, board)
    if pos == 'ltc' then
      if board[0] == ' ' then
        board[0] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'tm' then
      if board[1] == ' ' then
        board[1] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'rtc' then
     if board[2] == ' ' then
       board[2] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'lm' then
     if board[3] == ' ' then
       board[3] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'c' then
     if board[4] == ' ' then
       board[4] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'mr' then
     if board[5] == ' ' then
       board[5] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'lbc' then
     if board[6] == ' ' then
       board[6] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'bm' then
     if board[7] == ' ' then
       board[7] = play
      else
        puts "That square has already been marked. Please try again."
        maincontrol(play, board)
      end
    elsif pos == 'rbc' then
     if board[8] == ' ' then
       board[8] = play
     end
    end
    return board
end

def prompt(*args)
    print(" Please enter your mark in one position: ")
    pos = gets.chomp
    return pos
end

def boardprinter(board)
  puts "Here is how the board looks now:"
  puts "======="
  topl = "|" + board[0] + "|" + board[1] + "|" + board[2] + "|"
  puts(topl)
  midl = "|" + board[3] + "|" + board[4] + "|" + board[5] + "|"
  puts(midl)
  botl = "|" + board[6] + "|" + board[7] + "|" + board[8] + "|"
  puts(botl)
  puts "======="
  puts " "
end


def legendprinter(counter)
  if counter == 3 then
    puts "***************************************************************"
    puts "ltc is left-top-corner, tm is top-middle, rtc is right-top-corner"
    puts "lm is left-column-middle-row, c is center, mr is middlerow-right-column"
    puts "lbc is left-bottom-corner, bm is bottom-middle, rbc is right-bottom-corner"
    puts "***************************************************************"
  elsif counter == 6 then
    puts "***************************************************************"
    puts "ltc is left-top-corner, tm is top-middle, rtc is right-top-corner"
    puts "lm is left-column-middle-row, c is center, mr is middlerow-right-column"
    puts "lbc is left-bottom-corner, bm is bottom-middle, rbc is right-bottom-corner"
    puts "***************************************************************"
  end
end


def boardcatchecker(board, flag)
    if board[0] != ' ' then
      if board[1] != ' ' then
        if board[2] != ' ' then
          if board[3] != ' ' then
            if board[4] != ' ' then
              if board[5] != ' ' then
                if board[6] != ' ' then
                  if board[7] != ' ' then
                    if board[8] != ' ' then
                      puts "Game over."
                      abort("Cat's game. It was a draw!")
                    end
                  end
                end
              end
            end
          end
        end
      end
    end
end

def boardwinchecker(board)
  if board[0] == board[4] then # check the diagnoal from left top to right bottom corner
    if board[4] == board[8] then
      if board[4] != ' ' then
        lastmessage = "Player " + board[0] + " wins!"
        abort(lastmessage)
      end
    end
  end
  if board[2] == board[4] then # check the diagnoal from right top to left bottom corner
    if board[4] == board[6] then
      if board[6] != ' ' then
        lastmessage = "Player " + board[2] + " wins!"
        abort(lastmessage)
      end
    end
  end
  if board[0] == board[3] then # check the left column
    if board[3] == board[6] then
      if board[6] != ' ' then
        lastmessage = "Player " + board[0] + " wins!"
        abort(last message)
      end
    end
  end
  if board[0] == board[1] then # check the top row
    if board[1] == board[2] then
      if board[0] != ' ' then
        lastmessage = "Player " + board[0] + " wins!"
        abort(lastmessage)
      end
    end
  end
  if board[2] == board[5] then # check right column
    if board[5] == board[8] then
      if board[2] != ' ' then
        lastmessage = "Player " + board[2] + " wins!"
        abort(lastmessage)
      end
    end
  end
  if board[6] == board[7] then # check bottom row
    if board[7] == board[8] then
      if board[8] != ' ' then
        lastmessage = "Player " + board[6] + " wins!"
        abort(lastmessage)
      end
    end
  end
  if board[1] == board[4] then # check middle column
    if board[4] == board[7] then
      if board[1] != ' ' then
        lastmessage = "Player " + board[1] + " wins!"
        abort(lastmessage)
      end
    end
  end
  if board[3] == board[4] then # check middle row
    if board[4] == board[5] then
      if board[3] != ' ' then
        lastmessage = "Player " + board[3] + " wins!"
        abort(lastmessage)
      end
    end
  end
end

def maincontrol(player, board)
  pos = prompt
  board = markboard(pos, player, board)
end


flag = "play"
counter = 0
player="X"
# As of 9/4/19 this while loop is for the counter and alternating the X and O users.
while flag == "play" do
  counter = counter + 1
  mes = player + ", it is your turn."
  print(mes)
  pos = prompt
  board = markboard(pos, player, board)
  boardprinter(board)
  if player == 'X' then
    player = "O"
  else
    player = "X"
  end
  legendprinter(counter) # This will only print once or twice per game.
  boardwinchecker(board) # This will look for a player to win or lose.
  boardcatchecker(board, flag) # This will test if it is a Cat's game or not.
end