#   @author Alexander Skeba
class Pokemon():
    
    #create an intitialization function for each new pokemon
    def __init__(self, name, type, nature, level, attack, defense, speed, max_health, moves = ["-----","-----","-----","-----"], move_dict={}):
        """
        
        Parameters:
        name (string): Name of Pokemon
        type (string): Type of Pokemon (ex. "water", "fire", "grass")
        nature (string): Nature of Pokemon (ex. "Attack", "Defense", "Speed")
        level (int): Initial level of Pokemon
        attack (int): Attack stat of a pokemon
        defense (int): Defense stat of a pokemon
        speed (int): Speed stat of a pokemon
        max_health (int): Max Health of a pokemon 
        moves (list): Moveset of a pokemon
        move_dict (dict): Dictionary containg moves 
        
        """
        self.name = name 
        self.type = type 
        self.nature = nature
        self.level = level
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.max_health = max_health
        self.moves = moves
        
        self.current_health = max_health
        # create a string representation of the move set to allow the user to choose a move 
        self.moveset = " (1) {0:>5} \t (2) {1:>5} \n (3) {2:>5} \t (4) {3:>5} \n".format(self.moves[0], self.moves[1], self.moves[2], self.moves[3])

        
    
    def __str__(self):
        '''Give a string representation of the pokemon for testing purposes'''
        return f'Stats: \n Name: {self.name} \n Type: {self.type} \n Nature: {self.nature} \n Level: {self.level} \n Attack: {self.attack} \n Defense: {self.defense} \n Speed: {self.speed} \n Max Health: {self.max_health} \n Moves: {self.moves} \n Current Health: {self.current_health} \n'
        
    #increase the stats of the pokemon after they level up
    def level_up(self):
        #set a limit of lv. 100 for each pokemon, if pokemon is already lv 100 exit the level up sequence 
        if self.level <= 100:
            self.level += 1
        else:
            return
        self.attack += 1
        self.defense += 1
        self.speed += 1
        #Check its Nature and level up stats accordingly
        if self.nature == "attack":
            self.attack += 2 
        if self.nature == "defense":
            self.defense += 2
        if self.nature == "speed":
            self.speed += 2 
        
        
    #choose move
    def choose_move(self):
    
        #cast the user's input into an int to be used as the index of the moves array.  Subtract '1' to account for lists starting at 0
        self.move_int = int((input(self.moveset))) - 1
        
        
    #function to deal damage
    def use_move(self, type, move):
        pass
        
        
    #function to take damge 
    def take_damage():
        pass    
    


class Move():
    def __init__(self, name, type, attack, stat_move='None'):
        """
        The Move class creates a move object that holds important information on what a move does
        
        Parameters:
        name (str) Name of the move
        type (str) Type of the move (ex. "water", "grass", fire"
        stat_move (str) String affects the users or oppenents stats (ex. "attack_up", "defense_down")
        attack (int) Attack power of the move
        """
        self.name = name
        self.type = type
        self.stat_move = stat_move
        self.attack = attack
    
    
def generate_Moves():
    '''
    Generates a dictionary where the 'key' is the name of the move, and the 'value' is the Move object
    '''
    
    all_moves = {}
    moves = [['tackle', 'normal', 10],['scratch', 'normal', 10], ['water gun', 'water', 10], ['ember', 'fire', 10], ['vine whip', 'grass', 10]]
    for move in moves:
        all_moves[move[0]] = (Move(move[0],move[1],move[2]))
    return all_moves

    
    
    
squirtle = Pokemon("squirtle", "water", "defense", 5, 10, 15, 10, 15, ["tackle", "growl", "-----", "-----"])
blank = Pokemon("missingo", "none", "none",0, 0, 0, 0 ,0)
