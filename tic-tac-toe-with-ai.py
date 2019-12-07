import random


class Player(object):
    pass


class UserPlayer(Player):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        pass


class AIPlayer(Player):
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        pass

def x_wins(fld):
    if (fld[0][0] == fld[0][1] == fld[0][2] == "X") or (fld[1][0] == fld[1][1] == fld[1][2] == "X") or (
            fld[2][0] == fld[2][1] == fld[2][2] == "X"):
        return 1
    elif (fld[0][0] == fld[1][0] == fld[2][0] == "X") or (fld[0][1] == fld[1][1] == fld[2][1] == "X") or (
            fld[0][2] == fld[1][2] == fld[2][2] == "X"):
        return 1
    elif (fld[0][0] == fld[1][1] == fld[2][2] == "X") or (fld[0][2] == fld[1][1] == fld[2][0] == "X"):
        return 1
    else:
        return 0


def o_wins(fld):
    if (fld[0][0] == fld[0][1] == fld[0][2] == "O") or (fld[1][0] == fld[1][1] == fld[1][2] == "O") or (
            fld[2][0] == fld[2][1] == fld[2][2] == "O"):
        return 1
    elif (fld[0][0] == fld[1][0] == fld[2][0] == "O") or (fld[0][1] == fld[1][1] == fld[2][1] == "O") or (
            fld[0][2] == fld[1][2] == fld[2][2] == "O"):
        return 1
    elif (fld[0][0] == fld[1][1] == fld[2][2] == "O") or (
            fld[0][2] == fld[1][1] == fld[2][0] == "O"):
        return 1
    else:
        return 0


def is_empty(fld):
    if fld[0][0] == " " or fld[0][1] == " " or fld[0][2] == " " or fld[1][0] == " " or fld[1][1] == " " or \
            fld[1][2] == " " or fld[2][0] == " " or fld[2][1] == " " or fld[2][2] == " ":
        return 1
    else:
        return 0


def end_game(fld):
    if (x_wins(fld) == 1) and (o_wins(fld) == 0):
        return 1
    elif (x_wins(fld) == 0) and (o_wins(fld) == 1):
        return 0
    elif ((x_wins(fld) == 0) and (o_wins(fld) == 0)) and is_empty(fld) == 0:
        return 2
    else:
        return -1


field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
countX = 0
countO = 0
who = True
what = True

while True:
    try:
        # lst[0] = command, lst[1] = player1, lst[2] = player2
        lst = input("Input command: ").split()
    except lst[0] == "exit":
        quit()
    except len(lst) == 1:
        print("Bad parameters!")

    command = lst[0]
    if len(lst) == 3:
        player1 = lst[1]
        player2 = lst[2]
    if command == "start" and len(lst) == 3:
        if (player1 == "user") and (player2 == "user"):
            plr1 = UserPlayer("X")
            plr2 = UserPlayer("O")
        elif (player1 == "easy") and (player2 == "user"):
            plr1 = AIPlayer("X")
            plr2 = UserPlayer("O")
        elif (player1 == "user") and (player2 == "easy"):
            plr1 = UserPlayer("X")
            plr2 = AIPlayer("O")
        elif (player1 == "easy") and (player2 == "easy"):
            plr1 = AIPlayer("X")
            plr2 = AIPlayer("O")
        else:
            print("Bad parameters!")
            continue

        print("---------")
        print("| " + "     " + " |")
        print("| " + "     " + " |")
        print("| " + "     " + " |")
        print("---------")
        while True:
            if (who == True):
                if player1 == "user":
                    try:
                        a, b = map(int, input("Enter the coordinates: ").split())
                    except ValueError:
                        print("You should enter numbers!")
                        continue
                elif player1 == "easy":
                    print('Making move level "easy"')
                    a = random.randint(1, 3)
                    b = random.randint(1, 3)

                if (1 > a) or (a > 3) or (1 > b) or (b > 3):
                    print("Coordinates should be from 1 to 3!")
                elif (field[abs(b - 3)][abs(a - 1)] == "X") or (field[abs(b - 3)][abs(a - 1)] == "O"):
                    print("This cell is occupied! Choose another one!")
                else:
                    if what == True:
                        field[abs(b - 3)][abs(a - 1)] = "X"
                        what = False
                    else:
                        field[abs(b - 3)][abs(a - 1)] = "O"
                        what = True
                    print("---------")
                    print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
                    print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
                    print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
                    print("---------")
                    countX += 1
                    who = False
                    if end_game(field) == 1:
                        print("X wins")
                        break
                    elif end_game(field) == 0:
                        print("O wins")
                        break
                    elif end_game(field) == 2:
                        print("Draw")
                        break

            else:
                if player2 == "user":
                    try:
                        a, b = map(int, input("Enter the coordinates: ").split())
                    except ValueError:
                        print("You should enter numbers!")
                        continue
                elif player2 == "easy":
                    print('Making move level "easy"')
                    a = random.randint(1, 3)
                    b = random.randint(1, 3)

                if (1 > a) or (a > 3) or (1 > b) or (b > 3):
                    print("Coordinates should be from 1 to 3!")
                elif (field[abs(b - 3)][abs(a - 1)] == "X") or (field[abs(b - 3)][abs(a - 1)] == "O"):
                    print("This cell is occupied! Choose another one!")
                else:
                    if what == True:
                        field[abs(b - 3)][abs(a - 1)] = "X"
                        what = False
                    else:
                        field[abs(b - 3)][abs(a - 1)] = "O"
                        what = True
                    print("---------")
                    print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
                    print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
                    print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
                    print("---------")
                    countO += 1
                    who = True
                    if end_game(field) == 0:
                        print("O wins")
                        break
                    elif end_game(field) == 1:
                        print("X wins")
                        break
                    elif end_game(field) == 2:
                        print("Draw")
                        break

    elif command == "exit":
        break
    else:
        print("Bad parameters!")
        continue
