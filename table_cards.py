import random

import card
import game_rules

class Table_cards:

    def __init__(self):

        self.cards = list()
        self.decks = game_rules.decks

        for i in range(self.decks):
            self.add_deck()


    def add_deck(self) -> None:

        deck = list()

        
        

        # Espadas/Spades (♠︎)
        deck.append(card.Card("a", "♠︎"))
        deck.append(card.Card("2", "♠︎"))
        deck.append(card.Card("3", "♠︎"))
        deck.append(card.Card("4", "♠︎"))
        deck.append(card.Card("5", "♠︎"))
        deck.append(card.Card("6", "♠︎"))
        deck.append(card.Card("7", "♠︎"))
        deck.append(card.Card("8", "♠︎"))
        deck.append(card.Card("9", "♠︎"))
        deck.append(card.Card("10", "♠︎"))
        deck.append(card.Card("J", "♠︎"))
        deck.append(card.Card("Q", "♠︎"))
        deck.append(card.Card("K", "♠︎"))

        # Copas/Hearts (♥︎)
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

        # Ouros/Diamonds (♦︎)
        deck.append(card.Card("a", "♦︎"))
        deck.append(card.Card("2", "♦︎"))
        deck.append(card.Card("3", "♦︎"))
        deck.append(card.Card("4", "♦︎"))
        deck.append(card.Card("5", "♦︎"))
        deck.append(card.Card("6", "♦︎"))
        deck.append(card.Card("7", "♦︎"))
        deck.append(card.Card("8", "♦︎"))
        deck.append(card.Card("9", "♦︎"))
        deck.append(card.Card("10", "♦︎"))
        deck.append(card.Card("J", "♦︎"))
        deck.append(card.Card("Q", "♦︎"))
        deck.append(card.Card("K", "♦︎"))

        # Paus/Clubs (♣︎)
        deck.append(card.Card("a", "♣︎"))
        deck.append(card.Card("2", "♣︎"))
        deck.append(card.Card("3", "♣︎"))
        deck.append(card.Card("4", "♣︎"))
        deck.append(card.Card("5", "♣︎"))
        deck.append(card.Card("6", "♣︎"))
        deck.append(card.Card("7", "♣︎"))
        deck.append(card.Card("8", "♣︎"))
        deck.append(card.Card("9", "♣︎"))
        deck.append(card.Card("10", "♣︎"))
        deck.append(card.Card("J", "♣︎"))
        deck.append(card.Card("Q", "♣︎"))
        deck.append(card.Card("K", "♣︎"))


        self.cards.extend(deck)
        self.shuffle()
 
    def get_card(self) -> card.Card:
        crd = random.choice(self.cards)
        self.cards.remove(crd)
        return  crd
    

    def shuffle(self):
        random.shuffle(self.cards)
    
    def return_card(self,c) -> None:
        self.cards.append(c)
    
    def return_cards(self,l:list) -> None:
        self.cards.extend(l)



