import game
import sys
import colorama
import statistics
import game_rules
import neural_agent

def main():

    sys.stdout.reconfigure(encoding='utf-8') 
    gm = game.Game()
    colorama.just_fix_windows_console()
    
   
    print("treinamento")
    for i in range(10000):
        print("-----------------------------")
        gm.play_round()
        print("-----------------------------")
        #input("Press Enter to continue...")

    gm.clear_scores()
    gm.game_set_training(False)

    print("Teste")
    results = list()
    for a in range(10):
        

        for i in range(1000):
           print("-----------------------------")
           gm.play_round()
           print("-----------------------------")

        results.append(gm.get_round_inf())
        gm.clear_scores()
        #input("Press Enter to continue...")



    win_list = [x[1] for x in results]
    loss_list = [x[2] for x in results]
    tie_list = [x[3] for x in results]
    surr_list = [x[4] for x in results]
    ebj_list = [x[5] for x in results]
    #print(win_list)
        
    wins=  (statistics.median(win_list)/1000) * 100
    loss= (statistics.median(loss_list) /1000) * 100
    tie= (statistics.median(tie_list) /1000) * 100
    surr= (statistics.median(surr_list) /1000) * 100
    ebj = (statistics.median(ebj_list) /1000) * 100


    wins = round(wins,1)
    loss = round(loss,1)
    tie = round(tie,1)
    surr = round(surr,1)
    ebj = round(ebj,1)
    #for r in results:
        #wins+=r[1]
        #loss+=r[2]
        #tie+=r[3]
        #surr+=r[4]

    #wins=wins/10
    #loss=loss/10
    #tie=tie/10
    #surr=surr/10

    print("Wins: " + str(wins) + "%")
    print("Losses: " + str(loss) + "%")
    print("Ties: " + str(tie) + "%")

    if(game_rules.surrender):
       print("Surrender: " + str(surr) + "%")

    if(not game_rules.surrender_early):
      print("Early blackjack: " + str(ebj) + "%")


    #gm.round_info()
    print( ( (max(win_list) - min(win_list)) /1000 ) * 100)
    print(( (max(loss_list) - min(loss_list)) /1000 ) * 100)
    

    


main()

#n =neural_agent.Neural_agent()