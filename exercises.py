class Game():
    def __init__(self):
        self.turn = 'X'
        self.winner = None
        self.tie = False
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.stats = {'X': 0, 'O': 0, 'ties': 0}


    def play_game(self):
        while not self.winner and not self.tie:
            print("Welcome!")
            self.render()
            print("Let's go!")
            self.get_move()
            self.check_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()

        self.render() #show result 

        if self.winner:
            self.stats[self.winner] += 1
        elif self.tie:
            self.stats['ties'] += 1

        #scoreboard
        print(f"Scoreboard — X: {self.stats['X']}, O: {self.stats['O']}, Ties: {self.stats['ties']}")

        # play again?
        play_again = input("Would you like to play again? (y/n): ").lower()

        if play_again == 'y':
            self.reset_game()
            self.play_game()  #play again

        else:
            print("Good game!")
            
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
            if self.tie:
                print("Tie game!")
            elif self.winner:
                print(f"{self.winner} wins the game!")
            else:
                print(f"It's player {self.turn}'s turn!")

    def render(self):
            self.print_board()
            self.print_message()

    def get_move(self):
        while True: 
            # - Prompt for user
            move = input(f"Enter a valid movie (example: A1): ").lower()

            if move not in self.board:
                 print("invalid input...not on board")
                 continue
            elif self.board[move] is not None:
                print("your opponent is there")
            else:
                 self.board[move]=self.turn
                 break
      

    def check_winner(self): 
        winning_combos = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['c1', 'b2', 'a3']
        ]
        for combo in winning_combos:
             a,b,c=combo #unpack
             if self.board[a] and self.board[a] == self.board[b]==self.board[c]:
                self.winner=self.turn
                break #if all a,b, and c squares have the same character, you won. self.board[a] checks if board is empty 
             
    def check_for_tie(self):
        if self.winner:
             return False
        for move in self.board:
            if self.board[move] is not None:
                 return False 
        self.tie= True
        return True
    
    def switch_turn(self):
        switch = {'X': 'O', 'O': 'X'}
        self.turn=switch[self.turn]

    #new game
    def reset_game(self):
        self.board = {key: None for key in self.board}  # clear board
        self.winner = None
        self.tie = False
        self.turn = 'X'

        
      
game_instance = Game()
print(game_instance.play_game())
