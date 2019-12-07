import random


class Strategy:
    pass


class EasyStrategy(Strategy):
    def move(self, field):
        print('Making move level "easy"')
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        coord_ai = [x, y]
        return coord_ai


class MediumStrategy(Strategy):
    def move(self, fld, symbol):
        x = 0
        y = 0
        count = 0
        for i in range(3):
            if fld[i][0] == fld[i][1] == symbol and fld[i][2] == " ":
                x = 3
                y = abs(i - 3)
                count += 1
                break
            if fld[i][1] == fld[i][2] == symbol and fld[i][0] == " ":
                x = 1
                y = abs(i - 3)
                count += 1
                break
            if fld[i][0] == fld[i][2] == symbol and fld[i][1] == " ":
                x = 2
                y = abs(i - 3)
                count += 1
                break
            if fld[0][i] == fld[1][i] == symbol and fld[2][i] == " ":
                x = abs(-1 - i)
                y = 1
                count += 1
                break
            if fld[1][i] == fld[2][i] == symbol and fld[0][i] == " ":
                x = abs(-1 - i)
                y = 3
                count += 1
                break
            if fld[0][i] == fld[2][i] == symbol and fld[1][i] == " ":
                x = abs(-1 - i)
                y = 2
                count += 1
                break

        if fld[0][0] == fld[1][1] == symbol and fld[2][2] == " ":
            x = 3
            y = 1
            count += 1
        elif fld[0][0] == fld[2][2] == symbol and fld[1][1] == " ":
            x = 2
            y = 2
            count += 1
        elif fld[1][1] == fld[2][2] == symbol and fld[0][0] == " ":
            x = 1
            y = 3
            count += 1
        elif fld[2][0] == fld[1][1] == symbol and fld[0][2] == " ":
            x = 3
            y = 3
            count += 1
        elif fld[2][0] == fld[0][2] == symbol and fld[1][1] == " ":
            x = 2
            y = 2
            count += 1
        elif fld[1][1] == fld[0][2] == symbol and fld[2][0] == " ":
            x = 1
            y = 1
            count += 1
        elif fld[0][0] == fld[1][1] != symbol and fld[0][0] == fld[1][1] != " " and fld[2][2] == " ":
            x = 3
            y = 1
            count += 1
        elif fld[0][0] == fld[2][2] != symbol and fld[0][0] == fld[2][2] != " " and fld[1][1] == " ":
            x = 2
            y = 2
            count += 1
        elif fld[1][1] == fld[2][2] != symbol and fld[1][1] == fld[2][2] != " " and fld[0][0] == " ":
            x = 1
            y = 3
            count += 1
        elif fld[2][0] == fld[1][1] != symbol and fld[2][0] == fld[1][1] != " " and fld[2][0] == " ":
            x = 3
            y = 3
            count += 1
        elif fld[2][0] == fld[0][2] != symbol and fld[2][0] == fld[0][2] != " " and fld[1][1] == " ":
            x = 2
            y = 2
            count += 1
        elif fld[1][1] == fld[0][2] != symbol and fld[1][1] == fld[0][2] != " " and fld[2][0] == " ":
            x = 1
            y = 1
            count += 1
        if count == 0:
            for i in range(3):
                if fld[i][0] != symbol and fld[i][1] != symbol and fld[i][2] == " ":
                    x = 3
                    y = abs(i - 3)
                    break
                if fld[i][1] != symbol and fld[i][2] != symbol and fld[i][0] == " ":
                    x = 1
                    y = abs(i - 3)
                    break
                if fld[i][0] != symbol and fld[i][2] != symbol and fld[i][1] == " ":
                    x = 2
                    y = abs(i - 3)
                    break
                if fld[0][i] != symbol and fld[1][i] != symbol and fld[2][i] == " ":
                    x = abs(-1 - i)
                    y = 1
                    break
                if fld[1][i] != symbol and fld[2][i] != symbol and fld[0][i] == " ":
                    x = abs(-1 - i)
                    y = 3
                    break
                if fld[0][i] != symbol and fld[2][i] != symbol and fld[1][i] == " ":
                    x = abs(-1 - i)
                    y = 2
                    break
        print('Making move level "medium"')
        if x == 0 and y == 0:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
        coord_ai = [x, y]
        return coord_ai


class HardStrategy(Strategy):
    def move(self, fld, symbol):
        pass


class Player(object):
    symbol = ""

    def __init__(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol


class UserPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, level, field):
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
            coord_user = [x, y]
            return coord_user
        except ValueError:
            print("You should enter numbers!")


class AiPlayer(Player):
    strategy = Strategy()
    level = ""

    def __init__(self, level, symbol):
        super().__init__(symbol)
        if level == "easy":
            strategy = EasyStrategy()
        if level == "medium":
            strategy = MediumStrategy()
        if level == "hard":
            strategy = HardStrategy()

    def get_move(self, level, field):
        if level == "easy":
            strategy = EasyStrategy()
            return strategy.move(field)
        if level == "medium":
            strategy = MediumStrategy()
            return strategy.move(field, self.get_symbol())
        if level == "hard":
            strategy = HardStrategy()
            return strategy.move(field, self.get_symbol())


def print_field(fld):
    print("---------")
    print("| " + fld[0][0] + " " + fld[0][1] + " " + fld[0][2] + " |")
    print("| " + fld[1][0] + " " + fld[1][1] + " " + fld[1][2] + " |")
    print("| " + fld[2][0] + " " + fld[2][1] + " " + fld[2][2] + " |")
    print("---------")


def is_row_fill(fld, row_number, symbol):
    row = [" ", " ", " "]
    for i in range(3):
        row[i] = fld[i][row_number]
    return count(row, symbol) == 3


def is_col_fill(fld, col_number, symbol):
    col = [" ", " ", " "]
    for i in range(3):
        col[i] = fld[col_number][i]
    return count(col, symbol) == 3


def is_diag1_fill(fld, symbol):
    diag = [fld[0][0], fld[1][1], fld[2][2]]
    return count(diag, symbol) == 3


def is_diag2_fill(fld, symbol):
    diag = [fld[2][0], fld[1][1], fld[0][2]]
    return count(diag, symbol) == 3


def count(lst, symbol):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == symbol:
            counter += 1
    return counter


def detect_game(fld):
    for i in range(3):
        if is_row_fill(fld, i, "X"):
            return "X wins"
        if is_row_fill(fld, i, "O"):
            return "O wins"
        if is_col_fill(fld, i, "X"):
            return "X wins"
        if is_col_fill(fld, i, "O"):
            return "O wins"
    if is_diag1_fill(fld, "X") or is_diag2_fill(fld, "X"):
        return "X wins"
    if is_diag1_fill(fld, "O") or is_diag2_fill(fld, "O"):
        return "O wins"
    empty_squares = 0
    for i in range(3):
        empty_squares += count(fld[i], " ")
    if empty_squares == 0:
        return "Draw"
    else:
        return "Game not finished"


def create_player(type, symbol):
    type = type.lower()
    if type == "easy" or type == "medium" or type == "hard":
        return AiPlayer(type, symbol)
    if type == "user":
        return UserPlayer(symbol)


def check_params(a, b):
    if (1 > a) or (a > 3) or (1 > b) or (b > 3):
        print("Coordinates should be from 1 to 3!")
    elif (field[abs(b - 3)][abs(a - 1)] == "X") or (field[abs(b - 3)][abs(a - 1)] == "O"):
        print("This cell is occupied! Choose another one!")
    else:
        return 0


def fill(fld, x, y, symbol):
    field[abs(y - 3)][abs(x - 1)] = symbol


def turn():
    pass


field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
who = True

while True:
    try:
        lst = input("Input command: ").split()
    except lst[0] == "exit":
        quit()
    except len(lst) == 1:
        print("Bad parameters!")
    command = lst[0]
    if len(lst) == 3:
        type1 = lst[1]
        type2 = lst[2]
    if command == "start" and len(lst) == 3:
        print_field(field)
        while True:
            if (who == True):
                player1 = create_player(type1, "X")
                coord_player1 = player1.get_move(type1, field)
                a = coord_player1[0]
                b = coord_player1[1]
                if check_params(a, b) == 0:
                    fill(field, a, b, player1.get_symbol())
                    print_field(field)
                    who = False
                    if detect_game(field) != "Game not finished":
                        print(detect_game(field))
                        break
            else:
                player2 = create_player(type2, "O")
                coord_player2 = player2.get_move(type2, field)
                a1 = coord_player2[0]
                b1 = coord_player2[1]
                if check_params(a1, b1) == 0:
                    fill(field, a1, b1, player2.get_symbol())
                    print_field(field)
                    who = True
                    if detect_game(field) != "Game not finished":
                        print(detect_game(field))
                        field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                        break
    elif command == "exit":
        break
    else:
        print("Bad parameters!")
        continue
