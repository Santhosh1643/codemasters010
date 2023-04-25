def players():
    player_1=int(input("enter a position to apply x OR o:"))
    while player_1==x:
        print("you had determined position👍")
        input("enter x or o :")
        player_1_postion=player_1.def draw()
            
    player_2=int(input("enter a position to apply x OR o:"))
    while player_2==x:
        print("you had determined position👍")
        input("enter x or o :")
        player_2_postion=player_2.def draw() 

        if  player_1_postion == player_2_postion:
            player_1_postion-=player_1_postion
            
            return player_1
            print("position has already filled")
        elif player_1_postion == player_1_postion:
             player_1_postion-=player_1_postion
             return player_1
             print("position has already filled")
        elif player_2_postion == player_2_postion:
             player_2_postion-=player_2_postion
             return player_2
             print("position has already filled")
        elif player_2_postion == player_1_postion:
             player_2_postion-=player_2_postion
             return player_2
             print("position has already filled")
            rounds_for_player_1+=player_1
            print("player1 have entering",round,"round")
            rounds_for_player_2+=player_2
            print("player2 have entering",round,"round")
            if player_1< len(x[3]):
                print("player_1 had tried all his/her chance")
            elif player_2<len(x[3]):
                print("player_2 had tried all his/her chance")
            else :
                return player()
                
            
