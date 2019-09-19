/*  Written by www.continualintegration.com
Usage instructions: name this file tictactoe.groovy
Run it by using this: groovy tictactoe.groovy
*/

@groovy.transform.Canonical
class Program {   //create an object of nine strings. These will hold an "X" or an "O".  They represent the squares of the tictactoe board.
    String tl = ""
    String tm = ""
    String tr = ""
    String ml = ""
    String mm = ""
    String mr = ""
    String bl = ""
    String bm = ""
    String br = ""
}

programsv1 = new Program( " ", " ", " ", " ", " ", " ", " ", " ", " ")

def legend = { param2 -> println "***-------This is the legend for the grid -----***"
    println "tl is top-left square; tm is top-middle square"
    println "tr is top-right square; ml is middle-left square"
    println "mm is the center square; mr is the middle-right square"
    println "bl is the bottom-left square; bm is the bottom-middle square"
    println "br is the bottom-right square"
    println "***--------------------------------------------***"
              }

def current = { param1 -> println "Here is the current board:";
    println "_______";
    println "|${programsv1.tl}|${programsv1.tm}|${programsv1.tr}|";
    println "|${programsv1.ml}|${programsv1.mm}|${programsv1.mr}|";
    println "|${programsv1.bl}|${programsv1.bm}|${programsv1.br}|";
    println "-------";
   }

def inputter = { playermark -> def input = System.console().readLine "Player ${playermark} should decide where to make an ${playermark}: "
  varval = input
  return varval
  }

def checker = { varplace, programsv1, playermark -> if (programsv1."${varplace}" in ["X", "O"]) {  //check if empty or not
  println "That square has already been marked.  Please choose an empty square"
  return "GOELSEWHERE"}
  else{ return "PROCEED" }}

// below will check if square was entered according to the legend.  below closure does the change if the move was valid
def coolreal = { varplace, programsv1, playermark -> if (varplace in ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]) {
    z = checker.call(varplace, programsv1, playermark)
    if (z == "PROCEED") {programsv1."${varplace}" = "${playermark}"
                         return "NONEXIT"}
    else {varplace = inputter(playermark) //request valid input a second time
        if (varplace in ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]) {
           z = checker.call(varplace, programsv1, playermark)
           if (z == "PROCEED") {programsv1."${varplace}" = "${playermark}"
                                return "NONEXIT" }}}}
  else { println "Invalid input.  Please enter a square according to the legend."
    varplace = inputter(playermark) //request valid input a second time
        if (varplace in ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"]) {
           z = checker.call(varplace, programsv1, playermark)
           if (z == "PROCEED") {programsv1."${varplace}" = "${playermark}"
                                return "NONEXIT" }}}}

def cool = { varplace, programsv1, playermark -> t = coolreal.call(varplace, programsv1, playermark)
  if (t != "NONEXIT") { t = coolreal.call(varplace, programsv1, playermark)
    if (t != "NONEXIT") { t = coolreal.call(varplace, programsv1, playermark)
      if (t != "NONEXIT") { t = coolreal.call(varplace, programsv1, playermark)
        if (t != "NONEXIT") { t = coolreal.call(varplace, programsv1, playermark)
          if (t != "NONEXIT") {
            println " "
            println "*******************************************"
            println " "
            println "Too many failed attempts at entering a valid, empty square. Program exiting."
            return "EXIT" }}}}}}

def checkifgo = { programsv1 -> flagdone = "UNSET" as String
   if (programsv1."tl" == programsv1."tm") { if (programsv1."tm" == programsv1."tr") { if (programsv1."tm" != " ") {
    flagdone = "SET"
    println "GAME OVER."
    println "Player ${programsv1.tl} wins! (See the top horizontal three in a row)." } } }
   if (flagdone == "UNSET") { if (programsv1."ml" == programsv1."mm") { if (programsv1."mm" == programsv1."mr") { if (programsv1."ml" != " ") {
    flagdone = "SET"
    println "GAME OVER."
    println "Player ${programsv1.ml} wins! (See the middle horizontal three in a row)."} } } }
   if (flagdone == "UNSET") { if (programsv1."bl" == programsv1."bm") { if (programsv1."bm" == programsv1."br") { if (programsv1."bl" != " ") {
      flagdone = "SET"
      println "GAME OVER."
      println "Player ${programsv1.bl} wins! (See the lower horizontal three in a row)."} } } }
   if (flagdone == "UNSET") { if (programsv1."tl" == programsv1."mm") { if (programsv1."mm" == programsv1."br") { if (programsv1."tl" != " ") {
      flagdone = "SET"
      println "GAME OVER."
      println "Player ${programsv1.tl} wins! (See the diagonal three in a row)."} } } }
   if (flagdone == "UNSET") { if (programsv1."tr" == programsv1."mm") { if (programsv1."mm" == programsv1."bl") { if (programsv1."tr" != " ") {
       flagdone = "SET"
       println "GAME OVER."
       println "Player ${programsv1.bl} wins! (See the diagonal three in a row)."} } } }
   if (flagdone == "UNSET") { if (programsv1."tr" == programsv1."mr") { if (programsv1."mr" == programsv1."br") { if (programsv1."tr" != " ") {
       flagdone = "SET"
       println "GAME OVER."
       println "Player ${programsv1.tr} wins! (See the right vertical three in a row)."} } } }
   if (flagdone == "UNSET") { if (programsv1."tl" == programsv1."ml") { if (programsv1."ml" == programsv1."bl") { if (programsv1."tl" != " ") {
       flagdone = "SET"
       println "GAME OVER."
       println "Player ${programsv1.ml} wins! (See the left vertical three in a row)."} } } }
   if (flagdone == "UNSET") { if (programsv1."tm" == programsv1."mm") { if (programsv1."mm" == programsv1."bm") { if (programsv1."tm" != " ") {
       flagdone = "SET"
       println "GAME OVER."
       println "Player ${programsv1.tm} wins! (See the middle vertical three in a row)."} } } }
   return flagdone
}

//vertical ways of winning
legend.call()
current.call()
playermark = "X"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

playermark = "O"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

playermark = "X"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

playermark = "O"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

legend.call()

playermark = "X"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark ) == "EXIT") { return }
current.call()

varfin = checkifgo.call(programsv1)
if (varfin == "SET") { return }

playermark = "O"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

varfin = checkifgo.call(programsv1)
if (varfin == "SET") { return }

playermark = "X"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

varfin = checkifgo.call(programsv1)
if (varfin == "SET") { return }

playermark = "O"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

varfin = checkifgo.call(programsv1)
if (varfin == "SET") { return }

playermark = "X"
varplace = inputter(playermark)
if (cool.call(varplace, programsv1, playermark) == "EXIT") { return }
current.call()

varfin = checkifgo.call(programsv1)
if (varfin == "UNSET") { println "Cat's game aka tie game"
println "GAME OVER." } 