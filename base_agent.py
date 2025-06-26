

class base_agent:

    def __init__(self):

        self.hand = list()
        self.aces=0

    
    def add_card(self,c) -> None:

        if(c.name == "a"):
            self.hand.append(c)
            self.aces+=1
           
        else:
             if(len(self.hand) > 0 and self.hand[len(self.hand)-1].name=="a"):
                 
                 last = self.hand[len(self.hand)-1]
                 self.hand.remove(last)
                 self.hand.append(c)
                 self.hand.append(last)
             else:
                 self.hand.append(c)

    
    def return_card(self):
        last = self.hand[len(self.hand)-1]
        self.hand.remove(last)
        return last
    
    def clear_hand(self):
        self.aces = 0
        self.hand.clear()
        

                 
                 
            