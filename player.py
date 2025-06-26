
import base_agent
import card
import card_utils
import game_rules
from reinforcement_learning import Rein_agent
import neural_agent

MANUAL =1
REINFORCERMENT =2
NEURAL=3

class Player(base_agent.base_agent):


    

    def __init__(self):
        super().__init__()
        self.r_agent = Rein_agent()
        self.mode = REINFORCERMENT
        self.n_agent = None

        if(self.mode == NEURAL):
            self.n_agent = neural_agent.Neural_agent()

        

    def do_play(self) -> str:

        if(self.mode==MANUAL):
            return self.manual_play()
        
        if(self.mode==REINFORCERMENT):
            return self.r_agent.get_action()
        
        if(self.mode==NEURAL):
            return self.n_agent.get_action()
        

    
    def manual_play(self)->str:

        inp = input("Sua jogada: ")

        if(inp=='s'):
            return game_rules.stand
        
        if(inp=='h'):
            return game_rules.hit
        
        if(inp=='us'):
            return game_rules.surrender_or_stand
        
        if(inp=='uh'):
            return game_rules.surrender_or_hit
    
    

    def update_r_state(self,dc):

        if(self.mode==MANUAL):
            return
        
        if(self.mode==REINFORCERMENT):
           self.r_agent.set_state(card_utils.get_score(self.hand),dc,card_utils.is_soft(self.hand))
        
        if(self.mode==NEURAL):
            self.n_agent.update_state(card_utils.get_score(self.hand),dc,card_utils.is_soft(self.hand))

    def r_reward(self,val):
        if(self.mode!=REINFORCERMENT):
            return
        
        self.r_agent.get_reward(val)


    def early_surrender(self)->bool:
        return False
    
    def set_training(self,t):
        self.r_agent.training=t


    

    

    
