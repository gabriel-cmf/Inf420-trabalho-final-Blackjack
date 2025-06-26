
import dealer
import card
import card_utils
import game_rules
import table_cards
import math

import player


class Game:

     def __init__(self):
         print("init")
         self.dealer = dealer.Dealer()
         self.cards = table_cards.Table_cards()
         self.player = player.Player()
         
         self.start_wallet = self.wallet =100
         self.bet=0
         self.loss=0
         self.tie=0
         self.win=0
         self.e_blackjack=0
         self.surrender=0
         self.win_streak=0
         
         
     def get_rounds(self)->int:
          return self.loss+self.tie+self.win+self.surrender
     


     def round_info(self)->None:
         print("Rounds: " + str(self.get_rounds()))
         print("Vitorias: " + str(self.win))
         #print("Winstreak: " + str(self.win_streak))
         print("Perdas: " + str(self.loss))
         print("Empates: " + str(self.tie))
         print("Rendimentos: " +str(self.surrender))
         print("Lucro: " + str(self.wallet-self.start_wallet))


     def get_round_inf(self)->list:
         vals = list()
         vals.append(self.get_rounds())
         vals.append(self.win)
         vals.append(self.loss)
         vals.append(self.tie)
         vals.append(self.surrender)
         vals.append(self.e_blackjack)
         return vals



     def clear_scores(self)->None:
          self.win = self.loss = self.tie=0
          self.win_streak=0
          self.wallet=self.start_wallet
          self.surrender=0
          self.e_blackjack=0
     

     def dealer_wins(self,early_bj =False)->None:
          print("Você perdeu!")
          self.clear_cards()
          

          if(not early_bj):
             self.player.r_reward(-1)
             self.loss+=1
          else:
               self.e_blackjack+=1
          #self.win=0

     def player_wins(self,dealer_bust=False)->None:
          print("Você ganhou!")
          self.clear_cards()
          self.win+=1
          self.wallet += (self.bet *1.5) + self.bet
          self.win_streak = max(self.win,self.win_streak)
          if(not dealer_bust):
             self.player.r_reward( 1)

     def player_surrenders(self)->None:
          print("Você se rendeu")
          self.clear_cards()
          self.surrender+=1
          self.wallet += self.bet//2
          self.player.r_reward(-0.5)
          

         


     def both_tied(self)->None:
            print("Empate")
            self.clear_cards()
            self.tie+=1
            self.wallet += self.bet

            self.player.r_reward(0.5)





     #Retorna true se deu bust
     def player_hit(self)->bool:
           c = self.cards.get_card()
           self.player.add_card(c)

           score =card_utils.get_score(self.player.hand)

           if(score>21):
                print("Você deu Bust!")
                return True
           
           return False
     
     def dealer_hit(self)->bool:
           c = self.cards.get_card()
           self.dealer.add_card(c)

           score =card_utils.get_score(self.dealer.hand)

           if(score>21):
                print("Dealer deu Bust!")
                return True
           
           return False

          
     def game_set_training(self,t):
          self.player.set_training(t)

     def print_player_info(self) -> None:
          
          player_str = "Suas cartas: "
          for c in self.player.hand :
              
               player_str += c.get_name()
               player_str += " "
          
          player_str +=  " (" + str(card_utils.get_score(self.player.hand)) + ")"
               
          #print(len(self.dealer.hand))
          print("Carta do dealer: " + self.dealer.peek_card().get_name())
          print(player_str)


     def print_dealer_info(self):
          player_str = "Carta do dealer: "
          for c in self.dealer.hand :
              
               player_str += c.get_name()
               player_str += " "
          
          player_str +=  " (" + str(card_utils.get_score(self.player.hand)) + ")"
          print(player_str)  
     
     def print_final_hands(self)->None:
          print("Mãos finais:")
          player_str = "Suas cartas: "
          for c in self.player.hand :
              
               player_str += c.get_name()
               player_str += " "
          
          player_str +=  " (" + str(card_utils.get_score(self.player.hand)) + ")"

          dealer_str = "Cartas do dealer: "
          for c in self.dealer.hand:
               dealer_str += c.get_name()
               dealer_str+=" "

          dealer_str += " ("  + str(card_utils.get_score(self.dealer.hand)) +   ")"


          print(player_str)
          print(dealer_str)
          
       
     def clear_cards(self):
          self.cards.return_cards(self.player.hand)
          self.player.clear_hand()
          self.cards.return_cards(self.dealer.hand)
          self.dealer.clear_hand()
          

     def play_round(self) ->None:
        
        self.bet = self.wallet//2
        self.wallet -= self.wallet//2
         

        if(game_rules.no_hole_game is  True):
            c = self.cards.get_card()
            self.dealer.add_card(c)

        else:
              c = self.cards.get_card()
              self.dealer.add_card(c)
              c = self.cards.get_card()
              self.dealer.add_card(c)

        c = self.cards.get_card()
        self.player.add_card(c)
        c = self.cards.get_card()
        self.player.add_card(c)


        self.player.update_r_state(card_utils.get_score([self.dealer.peek_card()]))

        player_early_surrender = False
        
        if(game_rules.surrender and  (game_rules.no_hole_game is  True or game_rules.surrender_early)):
             #self.player.update_r_state(card_utils.get_score([self.dealer.peek_card()]))
             p = self.player.do_play()


             if(p==game_rules.surrender_or_hit or p==game_rules.surrender_or_stand):
                  player_early_surrender =True
                  


             pass
        
        if(game_rules.no_hole_game):
            c = self.cards.get_card()
            self.dealer.add_card(c)


        if(self.dealer.early_blackjack()):
             print("Dealer blackjack!")


             if( player_early_surrender==True):
                  self.player_surrenders()
                  return

             self.dealer_wins(not game_rules.surrender_early)
             return
             
        
        print("Sua jogada:")
        player_choice=""
        while(player_choice=="" or player_choice == game_rules.hit):
             self.print_player_info()
             self.player.update_r_state(card_utils.get_score([self.dealer.peek_card()]))
             
             player_choice =self.player.do_play()
             #print("Ação: " + player_choice)
             self.player.r_agent.update_state_action(player_choice)


             if(player_choice is None):
                  print("Erro, ação nula")
                  quit()

             if(player_choice==game_rules.surrender_or_hit and not game_rules.surrender):
                  player_choice==game_rules.hit

             if(player_choice==game_rules.surrender_or_stand and not game_rules.surrender):
                  player_choice==game_rules.stand

             if(player_choice==game_rules.hit):
                  #self.player.update_r_state(card_utils.get_score([self.dealer.peek_card()]))
                  old_val = card_utils.get_score(self.player.hand)
                  bust = self.player_hit()
                  

                  if(bust):
                       self.dealer_wins(False)
                       self.player.r_reward(-((old_val-10)/10))
                       
                       return
                  else:
                       
                       self.player.r_reward(1)
                  
             
             
             
        self.player.update_r_state(card_utils.get_score([self.dealer.peek_card()]))               
     
        self.print_player_info()

        if( game_rules.surrender and (player_choice==game_rules.surrender_or_hit or player_choice==game_rules.surrender_or_stand)):
             self.player_surrenders()
             return
              

        #Dealer    
        dealer_choice=""
        dealer_bust = False
        

        print("Jogada do dealer:")
        while(dealer_choice=="" or dealer_choice == game_rules.hit):
             #self.print_dealer_info()
             self.player.update_r_state(card_utils.get_score(self.dealer.hand))
             dealer_choice = self.dealer.make_play()
             print(dealer_choice)

             if(dealer_choice=="h"):
                  
                  bust = self.dealer_hit()
                  if(bust):
                       dealer_bust=True
                       break
             
             
                  
        
        self.player.update_r_state(card_utils.get_score([self.dealer.peek_card()]))     


        self.print_final_hands()
        if(dealer_bust and card_utils.get_score(self.player.hand) <=21):
             self.player_wins(True)
             return
        
        if(card_utils.get_score(self.player.hand) > card_utils.get_score(self.dealer.hand) ):
            self.player_wins()
            return
        
        if(card_utils.get_score(self.player.hand) < card_utils.get_score(self.dealer.hand) ):
            self.dealer_wins()
            return
        

        if(card_utils.get_score(self.player.hand) == card_utils.get_score(self.dealer.hand) ):
            self.both_tied()
            return


        

                  
                  
                       
             

        

        
         

              
                  
             


     

     
