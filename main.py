# start with basic
from os import system
from time import sleep
from copy import deepcopy

# add a go back one step feature -- key: 420 (It's done)
# make step back feature "back" activated -- No
# add a bigger board, -- Done
# change completed to green (try two colors) Challenge levels (white, red, green and red) -- done (1,2,3,4 as levels)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Board():
  def __init__(self, typeGame = 1, difficulty = 5):
    self.typeGame = typeGame
    self.difficulty = difficulty
    self.board = []
    self.history = []
    self.currentHistory = []
    if typeGame == 1:
      # By rows
      for i in range(3):
        self.board.append([".",".","."])
    elif typeGame == 2:
      # By rows
      basicBoard = []

      # row, col boards
      self.currentBoard = [1,1]
      self.currentHistory.append(deepcopy(self.currentBoard))

      for i in range(3):
        basicBoard.append([".",".","."])
      # By boards, then rows
      row = []
      for i in range(3):
        row.append(deepcopy(basicBoard))
      for i in range(3):
        self.board.append(deepcopy(row))
      self.history.append(deepcopy(self.board))
      #self.board = [[basicBoard*3]*3]
  
  def update(self,row,col,ch = "x"):
    #print(self.board)
    #sleep(10)
    if self.typeGame == 1:
      if self.board[row][col] == ".":
        self.board[row][col] = ch
    #print(self.board[2][2])
    #sleep(10)
  
  def change(self,Brow,Bcol,row,col,ch = "x"):
    if self.board[Brow][Bcol][row][col] == ".":
      self.board[Brow][Bcol][row][col] = ch
      return row,col
  
  def show(self):
    # row of boards
    for Brow in range(len(self.board)):
      # row of single board
      for row in range(len(self.board[Brow][0])):
        # col of boards (single board)
        for Bcol in range(len(self.board[Brow])):
          # item of single board
          for col in range(len(self.board[Brow][Bcol][row])):
            if col != 0:
              if self.currentBoard == [Brow,Bcol]:
                print(color.CYAN," | ",color.END,sep = "", end = "")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 3:
                print(color.RED," | ",color.END,sep = "", end = "") 
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 2:
                print(color.GREEN," | ",color.END,sep = "", end = "")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 1:
                if self.board[Brow][Bcol][1][1] == "X":
                  print(color.RED," | ",color.END,sep = "", end = "")
                else:
                  print(color.GREEN," | ",color.END,sep = "", end = "")
              else:
                print(" | ",sep = "", end = "")

              if self.currentBoard == [Brow,Bcol]:
                print(color.CYAN, self.board[Brow][Bcol][row][col], color.END, sep = "", end="")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 3:
                print(color.RED, self.board[Brow][Bcol][row][col], color.END, sep = "", end="")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 2:
                print(color.GREEN, self.board[Brow][Bcol][row][col], color.END, sep = "", end="")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 1:
                if self.board[Brow][Bcol][1][1] == "X":
                  print(color.RED, self.board[Brow][Bcol][row][col], color.END, sep = "", end="")
                else:
                  print(color.GREEN, self.board[Brow][Bcol][row][col], color.END, sep = "", end="")
              else:
                print(self.board[Brow][Bcol][row][col], sep = "", end="")

            else:

              if self.currentBoard == [Brow,Bcol]:
                print(color.CYAN,self.board[Brow][Bcol][row][col], color.END,sep = "", end="")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 3:
                print(color.RED,self.board[Brow][Bcol][row][col], color.END,sep = "", end="")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 2:
                print(color.GREEN,self.board[Brow][Bcol][row][col], color.END,sep = "", end="")
              elif self.board[Brow][Bcol][0][0] == " " and self.difficulty == 1:
                if self.board[Brow][Bcol][1][1] == "X":
                  print(color.RED,self.board[Brow][Bcol][row][col], color.END,sep = "", end="")
                else:
                  print(color.GREEN,self.board[Brow][Bcol][row][col], color.END,sep = "", end="")

              else:
                print(self.board[Brow][Bcol][row][col], sep = "", end="")
            #print(Brow,Bcol,row,col)
            #print()
          if Bcol != 2:
            print("    |    ", end = "")
        print()
        if row != 2:
          for i in range(3):
            if self.currentBoard[0] == Brow and self.currentBoard[1] == i:
              print(color.CYAN,"-"*9,color.END,"",end = "", sep = "")
              if self.currentBoard[1] != 1:
                print(end = "")
            else:
              if self.board[Brow][i][0][0] == " " and self.difficulty == 3:
                print(color.RED,"-"*9,color.END,sep = "",end = "")
              elif self.board[Brow][i][0][0] == " " and self.difficulty == 2:
                print(color.GREEN,"-"*9,color.END,sep = "",end = "")
              elif self.board[Brow][i][0][0] == " " and self.difficulty == 1:
                if self.board[Brow][i][1][1] == "X":
                  print(color.RED,"-"*9,color.END,sep = "",end = "")
                else:
                  print(color.GREEN,"-"*9,color.END,sep = "",end = "")
              else:
                print("-"*9,end = "")
            if i != 2:
              print("    |    ", end = "")
          print()
      if Brow != 2:
        print()
        print("-"*45)
        print()
            
  
  def demonstrate(self):
    #print("\tColumns")
    print("\tTic Tac Toe")
    print("  1     2     3  ")
    for row in range(len(self.board)):
      print("       |     |     ")
      print(row+1,end = " ")
      for col in range(len(self.board[0])):
        if col != 0:
          print("  |  ",self.board[row][col], sep = "", end="")
        else:
          print("  ",self.board[row][col], sep = "", end="")
      #print("   ",row+1, sep = "")
      print("  ")
      print("       |     |     ")
      if row != 2:
        print(" ","-"*17)
  
  def check(self,row,col):
    while (row > 2 or row < 0) or (col > 2 or col < 0) or self.board[row][col] != ".":
        system("clear")
        self.demonstrate()
        """
        if self.board[row][col] != ".":
          col = int(input("Enter UNUSED col: "))-1
          row = int(input("Enter UNUSED row: "))-1
        """
        if (row > 2 or row < 0) or (col > 2 or col < 0):
          col = int(input("Enter VALID col: "))-1
          row = int(input("Enter VALID row: "))-1
        if self.board[row][col] != ".":
          col = int(input("Enter UNUSED col: "))-1
          row = int(input("Enter UNUSED row: "))-1
    return row,col
  
  def checker(self,Brow,Bcol,row,col, turn, back):
    while (row > 2 or row < 0) or (col > 2 or col < 0) or self.board[Brow][Bcol][row][col] != ".":
        system("clear")
        self.show()
        if (row > 2 or row < 0) or (col > 2 or col < 0):
          # add step back here
          col = input("Enter col: ")
          while col == "":
            col = input("Enter col: ")
          col = int(col)-1
          #print(col)
          if col+1 == 420:
            #print(self.history)
            #sleep(10)
            self.board = deepcopy(self.history[len(self.history)-1-back])
            self.currentBoard = deepcopy(self.currentHistory[len(self.currentHistory)-1-back])
            Brow,Bcol = self.currentBoard[0],self.currentBoard[1]
            self.history = deepcopy(self.history[:(len(self.history)-back)])
            self.currentHistory = deepcopy(self.currentHistory[:(len(self.currentHistory)-back)])
            system("clear")
            sleep(1)
            turn -= back
            self.show()
            print("It is player ",turn%2 +1,"'s turn.", sep = "")
            col = int(input("Enter col: "))-1
          row = int(input("Enter VALID row: "))-1
        elif self.board[Brow][Bcol][row][col] != ".":
          # and here
          col = input("Enter col: ")
          while col == "":
            col = input("Enter col: ")
          col = int(col)-1
          #print(col)
          if col+1 == 420:
            #print(self.history)
            #sleep(10)
            self.board = deepcopy(self.history[len(self.history)-1-back])
            self.currentBoard = deepcopy(self.currentHistory[len(self.currentHistory)-1-back])
            Brow,Bcol = self.currentBoard[0],self.currentBoard[1]
            self.history = deepcopy(self.history[:(len(self.history)-back)])
            self.currentHistory = deepcopy(self.currentHistory[:(len(self.currentHistory)-back)])
            system("clear")
            sleep(1)
            turn -= back
            self.show()
            print("It is player ",turn%2 +1,"'s turn.", sep = "")
            col = int(input("Enter UNUSED col: "))-1
          row = int(input("Enter UNUSED row: "))-1
    return row,col, turn
  
  def finishedBoard(self,Brow,Bcol):
    activ = False
    while self.board[Brow][Bcol][0][0] == " ":
      Bcol = int(input("Enter Col of Board to play: "))-1
      # and here
      # nope just wait
      Brow = int(input("Enter Row of Board to play: "))-1
      print()
      while (Brow > 2 or Brow < 0) or (Bcol > 2 or Bcol < 0):
          Bcol = int(input("Enter VALID col: "))-1
        # and here
          Brow = int(input("Enter VALID row: "))-1
      activ = True
    return Brow,Bcol, activ


  
  def score(self):
    # check rows
    for row in self.board:
      if row[0] == row[1] and row[1] == row[2]:
        if row[0] != ".":
          return row[0], False

    # check cols
    cols = [[],[],[]]
    for row in range(len(self.board)):
      for col in range(len(self.board[row])):
        cols[col].append(self.board[row][col])
    for col in cols:
      if col[0] == col[1] and col[1] == col[2]:
        if col[0] != ".":
          return col[0], False
    
    # get top to bottom diagonal
    diagR = [self.board[0][0],self.board[1][1], self.board[2][2]]
    # check it
    if diagR[0] == diagR[1] and diagR[1] == diagR[2]:
      if diagR[0] != ".":
        return diagR[0], False
    # get bottom to top diagonal
    diagL = [self.board[2][0],self.board[1][1], self.board[0][2]]
    if diagL[0] == diagL[1] and diagL[1] == diagL[2]:
      if diagL[0] != ".":
        return diagL[0], False
    
    cnt = 0
    for row in range(len(self.board)):
      for col in range(len(self.board[0])):
        # check if all boxes are filled
        if self.board[row][col] != ".":
          cnt += 1
    if cnt < 9:
      return None, True
    else:
      return "Neither Player", False
    
      
  def score2(self, br,bc):
    board = self.board[br][bc]
    # check rows
    for row in board:
      if row[0] == row[1] and row[1] == row[2]:
        if row[0] != "." and row[0] != " ":
          return row[0]

    # check cols
    cols = [[],[],[]]
    for row in range(len(board)):
      for col in range(len(board[row])):
        cols[col].append(board[row][col])
    for col in cols:
      if col[0] == col[1] and col[1] == col[2]:
        if col[0] != "." and col[0] != " ":
          return col[0]
    
    # get top to bottom diagonal
    diagR = [board[0][0],board[1][1], board[2][2]]
    # check it
    if diagR[0] == diagR[1] and diagR[1] == diagR[2]:
      if diagR[0] != "." and diagR[0] != " ":
        return diagR[0]
    # get bottom to top diagonal
    diagL = [board[2][0],board[1][1], board[0][2]]
    if diagL[0] == diagL[1] and diagL[1] == diagL[2]:
      if diagL[0] != "." and diagL != " ":
        return diagL[0]
    
    ######Check for finished slot
    
    cnt = 0
    for row in range(len(board)):
      for col in range(len(board[0])):
        # check if all boxes are filled
        if board[row][col] != "." and board[row][col] != " ":
          cnt += 1
    if cnt < 9:
      return None
    else:
      return "Neither Player"


  def run(self):
    running = True
    self.demonstrate()
    turn = 0
    while running:
      print("It is player ",turn%2 +1,"'s turn.", sep = "")
      col = int(input("Enter col: "))-1
      row = int(input("Enter row: "))-1
      row,col = self.check(row,col)
      if turn%2 == 0:
        self.update(row,col,"X")
      else:
        self.update(row,col,"O")
      #print(self.board)
      sleep(0)
      system("clear")
      self.demonstrate()
      #print(self.score())
      current, running = self.score()
      turn +=1
    for i in range(3):
      sleep(1)
      system("clear")
      sleep(1)
      self.demonstrate()
    sleep(1)
    system("clear")
    print(current, "Wins!")
  
  def miniscore(self,br,bc,change):
    self.board[br][bc]=[[" "," "," "],[" ",change," "],[" "," "," "]]

  def bigscore(self):
    # rows first
    for br in range(len(self.board)):
      if self.board[br][0]==self.board[br][1] and self.board[br][1] == self.board[br][2]:
        if self.board[br][0][0][0] == " " and self.board[br][0][1][1] != "N":
          return self.board[br][0][1][1], False
    
    # cols next
    cols = [[],[],[]]
    for br in range(len(self.board)):
      for bc in range(len(self.board[0])):
        cols[br].append(self.board[br][bc])
    for i in cols:
      if cols[0] == cols[1] and cols[1] == cols[2] and cols[0][0][0] == " ":
        return cols[0][1][1], False
    
    if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0][0][0] == " ":
      return self.board[0][0][1][1], False

    if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2][0][0] == " ":
      return self.board[0][2][1][1], False

        # add, but busywork
    cnt = 0
    for row in range(len(self.board)):
      for col in range(len(self.board[0])):
        # check if all boxes are filled
        if self.board[row][col][0][0] == " ":
          cnt += 1
    if cnt < 9:
      return None, True
    else:
      return "Neither Player", False




  def play(self):
    running = True
    Brow, Bcol = 1,1
    self.show()
    turn = 0
    while running:
      print("It is player ",turn%2 +1,"'s turn.", sep = "")
      Brow,Bcol,activ = self.finishedBoard(Brow,Bcol)
      if activ == True:
        back = 2
      else:
        back = 1
      activ = False
      col = input("Enter col: ")
      while col == "":
        col = input("Enter col: ")
      col = int(col)-1
      #print(col)
      if col+1 == 420:
        #print(self.history)
        #sleep(10)
        self.board = deepcopy(self.history[len(self.history)-1-back])
        self.currentBoard = deepcopy(self.currentHistory[len(self.currentHistory)-1-back])
        Brow,Bcol = self.currentBoard[0],self.currentBoard[1]
        self.history = deepcopy(self.history[:(len(self.history)-back)])
        self.currentHistory = deepcopy(self.currentHistory[:(len(self.currentHistory)-back)])
        system("clear")
        sleep(1)
        turn -= back
        self.show()
        print("It is player ",turn%2 +1,"'s turn.", sep = "")
        col = int(input("Enter col: "))-1
      row = input("Enter row: ")
      while row == "":
        row = input("Enter col: ")
      row = int(row)-1

      row,col, turn = self.checker(Brow,Bcol,row,col, turn, back)
      
      if turn%2 == 0:
        Brow,Bcol = self.change(Brow,Bcol,row,col,"X")
      else:
        Brow,Bcol = self.change(Brow,Bcol,row,col,"O")

      self.history.append(deepcopy(self.board))

      self.currentBoard = [Brow,Bcol]
      self.currentHistory.append(deepcopy(self.currentBoard))
      for br in range(len(self.board)):
        for bc in range(len(self.board[0])):
          current = self.score2(br,bc)
          print(current)
          if current != None:
            if current != "Neither Player" and current != " ":
              self.miniscore(br,bc,current)
            elif current != " ":
              self.miniscore(br,bc,"N")

      #print(self.board)
      #self.score()
      sleep(0)
      system("clear")
      self.show()
      current, running = self.bigscore()
      #print(self.bigscore())
      #current, running = self.score()
      turn +=1
    if self.typeGame == 1:
      for i in range(2):
        sleep(1)
        system("clear")
        sleep(1)
        self.demonstrate()
      sleep(1)
      system("clear")
      print(current, "Wins!")
    
    elif self.typeGame == 2:
      for i in range(2):
        sleep(1)
        system("clear")
        sleep(1)
        self.show()
      sleep(1)
      system("clear")
      print(current, "Wins!")

board = Board(1)
board.run()
system("clear")
print("Larger is more difficult")
diff = int(input("Enter difficulty (1-4): "))
sleep(1)
system("clear")

board = Board(2,diff)
#board.run()
#board.show()
board.play()


# remove blue in diff 5
