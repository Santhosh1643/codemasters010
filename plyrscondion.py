def players():
    global X
    player = y
    while True:
        print(f"Player {player}, enter a position to apply {player}: ")
        position = int(input())
        if X[position] == ' ':
            X[position] = player
            draw()
            break
        else:
            print("That position is already taken. Try again.")
    return win()


def win():
    global X
    if (X[1] == X[2] == X[3] != ' ' or
        X[4] == X[5] == X != ' ' or
        X == X == X != ' ' or
        X[1] == X[4] == X != ' ' or
        X[2] == X[5] == X != ' ' or
        X[3] == X == X != ' ' or
        X[1] == X[5] == X != ' ' or
        X[3] == X[5] == X != ' '):
        return True
    else:
        return False


def main():
    start()
    while True:
        if players():
            print(f"Player {y} wins!")
            break
        elif players():
            print(f"Player {z} wins!")
            break
        elif ' ' not in X:
            print("It's a tie!")
            break

if __name__ == '__main__':
    main() 
