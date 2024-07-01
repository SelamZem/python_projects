#print The game board
class Board:
    def __init__(self):
           self.cells = [["_","_","_"],["_","_","_"],["_","_","_"]]
       
    
    def display(self):
        for rows in self.cells:
            print("----+---+----")
            print("|", end=" ")
            print(" | ".join(map(str,rows)), end = " ")
            print("|")
        print("----+---+----")


class Player:
    def __init__(self, name, symbol):

        self.name = name
        self.symbol = symbol
    
    def move(self):
            choice = int(input(f"{ticktac.current_player.name} choose 1-9: "))
            if(choice>=1 and choice<=9):
                divided = (choice-1)//3
                remainder = (choice-1)%3
                return tuple([divided, remainder])
            else:
                print(f"please input a valid number.")
                return Player.move(self)
    

class Tic_tac_toe:
    def __init__(self,player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else: 
            self.current_player = self.player1
    
    
    def update_cell(self, row, column):
        if self.board.cells[row][column]== "_":
            self.board.cells[row][column] = self.current_player.symbol
            self.switch_player()
        else:
            print("Already taken... please input valid number again")

    def check_winner(self):
        #check the horizontal
        if (self.board.cells[0][0]==self.board.cells[0][1]==self.board.cells[0][2] or self.board.cells[1][0]==self.board.cells[1][1]==self.board.cells[1][2] or self.board.cells[2][0]==self.board.cells[2][1]==self.board.cells[2][2]):
           return True
        #check vertical
        elif (self.board.cells[0][0]==self.board.cells[1][0]==self.board.cells[2][0] or self.board.cells[0][1]==self.board.cells[1][1]==self.board.cells[2][1] or self.board.cells[0][2]==self.board.cells[1][2]==self.board.cells[2][2]):
           return True
        #diagonal
        elif (self.board.cells[0][0]==self.board.cells[1][1]==self.board.cells[2][2] or self.board.cells[2][0]==self.board.cells[1][1]==self.board.cells[0][2]):
           return True
    
    def is_full(self):
        sum = 0
        for rows in self.board.cells:
            for item in rows:
                if item != "_":
                    sum+=1
        if sum==9:
            return True               
    
    def playing(self):
        count = 0
        while True:
            self.board.display()
            row , column = Player.move(self)
            
            count+=1
            if(count>=5):
                if self.check_winner():
                    print(f"{self.current_player.name} has won!")
                    break
        
                if self.is_full():
                    print("Draw!")
                    break
            self.update_cell(row,column)


player1 = Player("abc", "X")
player2 = Player("efg", "O")

ticktac = Tic_tac_toe(player1, player2)
ticktac.playing()