
import base_agent
import card
import card_utils
import game_rules

class Dealer(base_agent.base_agent):


    def __init__(self):
         super().__init__()



    def peek_card(self) -> card.Card:
        return self.hand[0]
    
    def early_blackjack(self) -> bool:

        if(len(self.hand)>=2):

            if(self.peek_card().name == "10" or self.peek_card().name.isalpha() ):
                score = card_utils.get_score(self.hand)

                if(score==21):
                    return True
                else:
                    return False



        
        return False
    

    def make_play(self)->str:


        score = card_utils.get_score(self.hand)

        if(score < 17):
            return game_rules.hit
            

        else:
            if(card_utils.soft_17(self.hand)):

                if(game_rules.soft17_hit):
                    return game_rules.hit
                    

                else:
                    return game_rules.stand
                    
            else:
                return game_rules.stand
                





        


        
    

