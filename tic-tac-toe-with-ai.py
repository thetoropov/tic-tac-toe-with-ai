x = input("Enter cells: ")
print("---------")
print("| " + x[0] + " " + x[1] + " " + x[2] + " |")
print("| " + x[3] + " " + x[4] + " " + x[5] + " |")
print("| " + x[6] + " " + x[7] + " " + x[8] + " |")
print("---------")
field = [[x[0], x[1], x[2]], [x[3], x[4], x[5]], [x[6], x[7], x[8]]]
countX = 0
countO = 0
for i in range(3):
    for j in range(3):
        if field[i][j] == "X":
            countX += 1
        if field[i][j] == "O":
            countO += 1


def XWin(field):
    if (field[0][0] == field[0][1] == field[0][2] == "X") or (field[1][0] == field[1][1] == field[1][2] == "X") or (
            field[2][0] == field[2][1] == field[2][2] == "X"):
        return 1
    elif (field[0][0] == field[1][0] == field[2][0] == "X") or (field[0][1] == field[1][1] == field[2][1] == "X") or (
            field[0][2] == field[1][2] == field[2][2] == "X"):
        return 1
    elif (field[0][0] == field[1][1] == field[2][2] == "X") or (field[0][2] == field[1][1] == field[2][0] == "X"):
        return 1
    else:
        return 0


def OWin(field):
    if (field[0][0] == field[0][1] == field[0][2] == "O") or (field[1][0] == field[1][1] == field[1][2] == "O") or (
            field[2][0] == field[2][1] == field[2][2] == "O"):
        return 1
    elif (field[0][0] == field[1][0] == field[2][0] == "O") or (field[0][1] == field[1][1] == field[2][1] == "O") or (
            field[0][2] == field[1][2] == field[2][2] == "O"):
        return 1
    elif (field[0][0] == field[1][1] == field[2][2] == "O") or (
            field[0][2] == field[1][1] == field[2][0] == "O"):
        return 1
    else:
        return 0


def IsEmpty(field):
    if field[0][0] == "_" or field[0][1] == "_" or field[0][2] == "_" or field[1][0] == "_" or field[1][1] == "_" or \
            field[1][2] == "_" or field[2][0] == "_" or field[2][1] == "_" or field[2][2] == "_":
        return 1
    else:
        return 0


def EndGame(field):
    if (XWin(field) == 1) and (OWin(field) == 0):
        return ("X wins")
    elif (XWin(field) == 0) and (OWin(field) == 1):
        return ("O wins")
    elif ((XWin(field) == 0) and (OWin(field) == 0)) and IsEmpty(field) == 0:
        return ("Draw")
    else:
        return ("Game not finished")


while True:
    if (countX == countO):
        try:
            a, b = map(int, input("Enter the coordinates: ").split())
        except ValueError:
            print("You should enter numbers!")
            continue
        if (1 > a) or (a > 3) or (1 > b) or (b > 3):
            print("Coordinates should be from 1 to 3!")
        elif (field[abs(b - 3)][abs(a - 1)] == "X") or (field[abs(b - 3)][abs(a - 1)] == "O"):
            print("This cell is occupied! Choose another one!")
        else:
            field[abs(b - 3)][abs(a - 1)] = "X"
            print("---------")
            print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
            print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
            print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
            print("---------")
            countX += 1
            if EndGame(field) == "X wins":
                print("X wins")
                break
            elif EndGame(field) == "Draw":
                print("Draw")
                break
            elif EndGame(field) == "Game not finished":
                print("Game not finished")
                break
    else:
        try:
            a, b = map(int, input("Enter the coordinates: ").split())
        except ValueError:
            print("You should enter numbers!")
            continue
        if (1 > a) or (a > 3) or (1 > b) or (b > 3):
            print("Coordinates should be from 1 to 3!")
        elif (field[abs(b - 3)][abs(a - 1)] == "X") or (field[abs(b - 3)][abs(a - 1)] == "O"):
            print("This cell is occupied! Choose another one!")
        else:
            field[abs(b - 3)][abs(a - 1)] = "O"
            print("---------")
            print("| " + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
            print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
            print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
            print("---------")
            countO += 1
            if EndGame(field) == "O wins":
                print("O wins")
                break
            elif EndGame(field) == "Draw":
                print("Draw")
                break
            elif EndGame(field) == "Game not finished":
                print("Game not finished")
                break
