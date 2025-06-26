import random
import card




def get_score(cards:list) -> int:
    score = 0
    for c in cards:

        is_face = (c.name=="J" or c.name=="Q" or c.name=="K")
        is_ace = (c.name=="a")
    
        if(not is_face and not is_ace):
            score += int(c.name)

        else:
            #Aces must be last
            if(is_ace):

                if(score+11 >= 22):
                    score+=1
                else:
                    score+=11
            else:
                score+=10

                


    return score




def is_soft(cards:list) -> bool:
    aces = 0
    score=0
    for c in cards:
        is_face = (c.name=="J" or c.name=="Q" or c.name=="K")
        is_ace = (c.name=="a")
    
        if(not is_face and not is_ace):
            score += int(c.name)

        else:
            #Aces must be last
            if(is_ace):
                aces+=1
                if(score+11 >= 22):
                    score+=1
                    return False
                else:
                    score+=11
                    
            else:
                score+=10


    if(aces>0):
        return True    
    return False
    
    


def soft_17(cards:list) -> bool:


    if(get_score(cards)!=17):
        return False
    
    for c in cards:
        if(c.name=='a'):
            return True
        
    return False


def get_all_dealers_cards() -> list:
    
    deck = list()
    deck.append(card.Card("a", "♥︎"))
    deck.append(card.Card("2", "♥︎"))
    deck.append(card.Card("3", "♥︎"))
    deck.append(card.Card("4", "♥︎"))
    deck.append(card.Card("5", "♥︎"))
    deck.append(card.Card("6", "♥︎"))
    deck.append(card.Card("7", "♥︎"))
    deck.append(card.Card("8", "♥︎"))
    deck.append(card.Card("9", "♥︎"))
    deck.append(card.Card("10", "♥︎"))
    deck.append(card.Card("J", "♥︎"))
    deck.append(card.Card("Q", "♥︎"))
    deck.append(card.Card("K", "♥︎"))

    return deck


