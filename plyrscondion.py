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
            return player_1
            print("position has already filled")
        elif player_1_postion == player_1_postion:
             return player_1
             print("position has already filled")
        elif player_2_postion == player_2_postion:
             return player_2
             print("position has already filled")
        elif player_2_postion == player_1_postion:
             return player_2
             print("position has already filled")
