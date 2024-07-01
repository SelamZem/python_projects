import random
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def roll_dice():
        min_no= 1
        max_no = 6
        roll_no = random.randint(min_no, max_no)

        return roll_no

class Play():
    def __init__(self):
        self.players = []
        self.scores = []
        self.index = 0
        self.number_players = 0
        self.max_score = 30

    def add_player(self):
 
        self.number_players= int(input("Enter the number of players(2-4):  "))
        self.max_score = int(input("Enter the max number you want to play: "))
        if self.number_players>=2 and self.number_players<=4:
            for i in range(self.number_players):
                player_name = input("Enter your name: ")
                self.players.append(Player(player_name))
                self.scores.append(Player(player_name).score)
                self.current_player= self.players[self.index]
                
        else: 
            print("Please Ente a valid number")
            self.add_player()
  
    def switchPlayer(self):
        if self.index < len(self.players)-1:
            self.index += 1
            self.current_player = self.players[self.index]
        else:
            self.index = 0
            self.current_player = self.players[self.index]

        
    def game_play(self):
    
        while max(self.scores) < self.max_score or self.index != 0:


            while True:
                want_roll = input(f"Would you like to roll {self.current_player} (y)? ").lower()
                if want_roll != 'y':
                    self.switchPlayer()
                    break;

                else:
                    value = Player.roll_dice()
            
                
                if value == 1:
                    self.scores[self.index] = 0
                    print("You rolled 1. Turn done")
                    print("Your score is ", self.scores[self.index])
                    self.switchPlayer()
                    break
                
                elif  self.scores[self.index]+value >= self.max_score:
                        self.scores[self.index]= self.max_score
                        print(f'You have got the max score ', self.players[self.index])
                        self.switchPlayer()
                        break

                else:
                    self.scores[self.index] += value
                    print("You rolled ", value)
                
                print("Your score is ", self.scores[self.index])
        
        Player(self.current_player).score = self.scores[self.index]
    
    def winner(self):
        max_score = max(self.scores)
        number_max = self.scores.count(max_score) #counts how many players got the max score
        if number_max > 1:
            print("Draw!")
        else:    
            winning_index = self.scores.index(max_score)
            print("The winner is ", self.players[winning_index])

    def game(self):
        self.add_player()
        #start the game
        for i in range(self.number_players):
            self.game_play()

        #winner
        self.winner()
      



play1 = Play()
play1.game()