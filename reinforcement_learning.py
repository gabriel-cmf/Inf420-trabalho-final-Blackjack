
import game_rules
import random
import player
import card
class Rein_agent:

    def __init__(self, lr=0.1, exp_rate=0.2):
        self.player_Q_Values  = dict()
        self.training = True

        self.actions = [game_rules.hit,game_rules.stand,game_rules.surrender_or_hit,game_rules.surrender_or_stand]


        for a in range(2,22):
            for b in range(1,12):
                for c in [True, False]:
                    self.player_Q_Values[(a,b,c)] = dict()
                    for q in self.actions:
                        
                        if(a==21 and q is game_rules.stand):
                            self.player_Q_Values[(a,b,c)][q] = 1
                            #print("21")
                        else:

                            if(q is game_rules.stand or q is game_rules.hit):
                                self.player_Q_Values[(a,b,c)][q] = 0
                            else:
                                #Surrender desativado
                                self.player_Q_Values[(a,b,c)][q] = -10

                            
                            #print("0")

        
        self.player_state_action = []
        self.state = (0, 0, False)  # initial state
       
        self.end = False
        self.lr = lr
        self.exp_rate = exp_rate

    
    #Obtem uma das ações do gamerules
    def get_action(self) -> str:

        cur = self.state
        action = ""

        print("state: " +str(self.state))
        
        if (cur[0] <= 11 or ( cur[2] is True and cur[0] <=17  ) ):
            print("Force hit")
            return game_rules.hit
        
        if((not cur[2] and cur[0] >=18) or (cur[2] and cur[0] >=19)):
            print("Force stand")
            return game_rules.stand
        

        if(cur[0]==15 and cur[1]>=10):
            print("Forced surrender")
            return game_rules.surrender_or_stand
        
        if(cur[0]==16 and cur[1]>=9):
            print("Forced surrender")
            return game_rules.surrender_or_stand
        
        if(cur[0]==17 and cur[1]==11):
            print("Forced surrender")
            return game_rules.surrender_or_hit
        
        if (random.uniform(0,1) <= self.exp_rate and self.training ):
            action = random.choice(self.actions)
            print("random action: " +action)
        
        else:
            
            #all_dicts = [x for x in self.player_Q_Values.values()]
            #all_dicts = list(all_dicts)

            #all_dicts.sort(key = lambda x: max(x[game_rules.hit],x[game_rules.stand],x[game_rules.surrender_or_stand],x[game_rules.surrender_or_hit]),reverse=True)

            main_dict = self.player_Q_Values[self.state]
            print(main_dict)

            key_list = list(main_dict.keys())

            key_list.sort(key=lambda x:main_dict[x],reverse=True)

            action = key_list[0]

            print("action: " +action + ", " + str(main_dict[action]))








        if(action is None):
            quit()
        return action
        
    

    def has_action(self) -> bool:
        if(len(self.player_state_action) > 0):
            return True
        else:
            return False


    
    def set_state(self,player_score:int,dealer_score:int,aces:bool):

        tup = (player_score,dealer_score,aces)
        self.state=tup

        if(self.has_action()):
            self.update_state_action2()



    def update_state_action(self,a):

        self.player_state_action = [[self.state,a]]

    def update_state_action2(self):
        action = self.player_state_action[0][1]
        self.player_state_action = [[self.state,action]]


    def get_reward(self,val) -> None:

        if(not self.training):
            return

        if(len(self.player_state_action)<=0):
            print("Sem estado sem ação")
            quit()

        for s in self.player_state_action:
            action= s[1]
            state =s[0]

            #print("action: " + action)
            reward = self.player_Q_Values[state][action] + self.lr*(val - self.player_Q_Values[state][action])
            self.player_Q_Values[state][action] = round(reward, 3)

           

            if(game_rules.surrender and 
               self.player_Q_Values[state][game_rules.surrender_or_stand] !=  self.player_Q_Values[state][game_rules.surrender_or_hit]):
                
                min_val = min(self.player_Q_Values[state][game_rules.surrender_or_stand],self.player_Q_Values[state][game_rules.surrender_or_hit])
                self.player_Q_Values[state][game_rules.surrender_or_stand]=min_val
                self.player_Q_Values[state][game_rules.surrender_or_hit]=min_val


            print(str(state) + " , " + str(action) + " , " + str( self.player_Q_Values[state][action]))
