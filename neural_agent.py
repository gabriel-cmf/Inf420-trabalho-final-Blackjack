from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout
from keras.metrics import Accuracy,BinaryAccuracy,CategoricalAccuracy
import pandas as pd
import card_utils
import game_rules
from keras.utils import to_categorical
import numpy as np



class Neural_agent :




    def get_ideal_move(self,player:int,dealer:int,soft:bool)->str:

        if((player <= 11) or (soft is True and player <= 17)):
            return game_rules.hit
        
        if((soft is False and player >= 18) or (soft is True and player >= 19)):
            print('stand')
            return game_rules.stand
        

        if(soft is False):

            if(player==15 and dealer>=10):
                return game_rules.surrender_or_hit
            
            if(player==16 and dealer>=9):
                return game_rules.surrender_or_hit
            
            if(player==17 and dealer>=11):
                return game_rules.surrender_or_stand
            
            if(player == 12):
                if(dealer >=4 and dealer <=6):
                    return game_rules.stand
                
                else:
                    return game_rules.hit
                
            if(player >=13 and player <= 14):
                if(dealer <=6):
                    return game_rules.stand
                
                else:
                    return game_rules.hit
                
            if(player == 15 and dealer <= 10):
                if(dealer <=6):
                    return game_rules.stand
                
                else:
                    return game_rules.hit
                
            if(player == 16 and dealer <= 9):
                if(dealer <=6):
                    return game_rules.stand
                
                else:
                    return game_rules.hit
                
            if(player == 17 and dealer <= 11):
               return game_rules.stand

        else:
            if(player == 18):
                if(dealer <= 8):
                    return game_rules.stand
                
                else:
                    return game_rules.hit
                
        
        print(player)
        print(dealer)
        print(soft)
        
                
            

    def __init__(self):

        #Game values
        self.player_val=0
        self.dealer_val=0
        self.aces=False
        

        self.model = pd.DataFrame()

        self.conv_dict = dict()
        self.conv_dict[game_rules.hit] = 0
        self.conv_dict[game_rules.stand] = 1
        self.conv_dict[game_rules.surrender_or_hit] = 2
        self.conv_dict[game_rules.surrender_or_stand] = 3


        self.action_dict = {value: key for key, value in self.conv_dict.items()}


        print(self.action_dict.values())


        player_hands = list()
        dealer_card = list()
        soft_hand = list()
        ideal_move = list()


        for a in range(2,22):
            for b in range (2,12):
                for c in [True,False]:
                    player_hands.append(a)
                    dealer_card.append(b)
                    soft_hand.append(c)
                    r = self.get_ideal_move(a,b,c)
                    try:
                       ideal_move.append(self.conv_dict[r])
                    except:
                        print(r)
                        quit()

        self.model["player_hand"] = player_hands
        self.model["dealer_card"] = dealer_card
        self.model["soft"] = soft_hand
        self.model["ideal_move"] = ideal_move


        self.model["player_hand"]  = np.asarray(self.model["player_hand"]).astype("float32")
        self.model["dealer_card"]  = np.asarray(self.model["dealer_card"]).astype("float32")
        self.model["soft"]  = np.asarray(self.model["soft"]).astype("float32")
        self.model["ideal_move"]  = np.asarray(self.model["ideal_move"]).astype("float32")

        print("Model done")

        

        x_cols = [c for c in self.model.columns if c!= "ideal_move"]

        x_train = self.model[x_cols]
        x_train.astype("float32")
        y_train = self.model["ideal_move"]
        #y_train = pd.get_dummies(y_train)
        y_train = to_categorical(y_train)
        

        print(x_train.shape)
        print(y_train.shape)

        self.neural_net = Sequential()
        self.neural_net.add(Dense(64, activation='relu'))
        self.neural_net.add(Dense(512, activation='relu'))
        self.neural_net.add(Dense(256, activation='relu'))
        self.neural_net.add(Dense(32, activation='relu'))
        self.neural_net.add(Dense(4, activation='softmax'))
        self.neural_net.compile(loss='categorical_crossentropy', optimizer='adam')
        self.neural_net.fit(x_train, y_train, epochs=40, batch_size=256, verbose=1)

        y_pred = self.neural_net.predict(x_train)
        print(y_pred[200])
        acu = CategoricalAccuracy()
        acu.update_state(y_train,y_pred)
        
        print(acu.result())
        

    

    def update_state(self,player_score:int,dealer_score:int,acesx:bool) -> None:
        self.player_val=player_score
        self.dealer_val=dealer_score
        self.aces=acesx

    def get_action(self) -> str:


        state = np.array([self.player_val,self.dealer_val,self.aces]).reshape(1,-1)
        y_pred = self.neural_net.predict(state)
        
      
        y_pred = list(list(y_pred)[0])




        

        inx = y_pred.index(max(y_pred))
        #print(y_pred)
        print(self.action_dict[inx])
        #quit()

        return self.action_dict[inx]

        



        

        



        





