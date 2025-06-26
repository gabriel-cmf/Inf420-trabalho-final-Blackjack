import random



class Card:

    def __init__(self,n,s):
        self.name=n
        self.suit =s

    def print_name(self):
        print(self.name+self.suit)

    def get_name(self)->str:
        text = self.name+self.suit
        return text
