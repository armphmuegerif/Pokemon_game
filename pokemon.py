class Pokemon():
    
    #create an intitialization function for each new pokemon
    def __init__(self, name, type, level, moves, attack, defense, total_health):
        
        self.name = name 
        self.type = type 
        self.level = level
        self.moves = moves
        self.attack = attack
        self.defense = defense
        self.total_health = total_health
        # create a string representation of the move set to allow the user to choose a move 
        self.moveset = " (1) {0:>5} \t (2) {1:>5} \n (3) {2:>5} \t (4) {3:>5} \n".format(self.moves[0], self.moves[1], self.moves[2], self.moves[3])
        
    
    #increase the stats of the pokemon after they level up
    def level_up(self, level, attack, defense, total_health):
        pass
        
    #display moves 
    def show_moves(self):
        
        pass
    
    #choose move
    def choose_move(self):
    
        #cast the user's input into an int to be used as the index of the moves array.  Subtract '1' to account for lists starting at 0
        move_int = int((input(self.moveset))) - 1
        
        
    #function to deal damage
    def deal_damage(self, type, move):
        pass
        
    #function to take damge 
    def take_damage():
        pass    
        


squirtle = Pokemon("squirtle", "water", 5, ["tackle", "growl", "-----", "-----"], 10, 15, 15)

print(squirtle.attack)