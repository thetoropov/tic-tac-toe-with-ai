import random


class Strategy:
    pass


class EasyStrategy(Strategy):
    def move(self, field):
        print('Making move level "easy"')
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        return [x, y]


class MediumStrategy(Strategy):
    def reformat(self, best):
        if best[0] == 0 and best[1] == 0:
            coord_ai = [1, 3]
        elif best[0] == 0 and best[1] == 1:
            coord_ai = [2, 3]
        elif best[0] == 0 and best[1] == 2:
            coord_ai = [3, 3]
        elif best[0] == 1 and best[1] == 0:
            coord_ai = [1, 2]
        elif best[0] == 1 and best[1] == 1:
            coord_ai = [2, 2]
        elif best[0] == 1 and best[1] == 2:
            coord_ai = [3, 2]
        elif best[0] == 2 and best[1] == 0:
            coord_ai = [1, 1]
        elif best[0] == 2 and best[1] == 1:
            coord_ai = [2, 1]
        elif best[0] == 2 and best[1] == 2:
            coord_ai = [3, 1]
        return coord_ai

    def move(self, fld, symbol):
        x = 0
        y = 0
        print('Making move level "medium"')
        """
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
                if fld[i][0] != symbol and fld[i][1] != symbol and fld[i][0] != " " and fld[i][1] != " " and fld[i][2] == " ":
                    x = 3
                    y = abs(i - 3)
                    break
                if fld[i][1] != symbol and fld[i][2] != symbol and fld[i][1] != " " and fld[i][2] != " " and fld[i][0] == " ":
                    x = 1
                    y = abs(i - 3)
                    break
                if fld[i][0] != symbol and fld[i][2] != symbol and fld[i][0] != " " and fld[i][2] != " " and fld[i][1] == " ":
                    x = 2
                    y = abs(i - 3)
                    break
                if fld[0][i] != symbol and fld[1][i] != symbol and fld[0][i] != " " and fld[1][i] != " " and fld[2][i] == " ":
                    x = abs(-1 - i)
                    y = 1
                    break
                if fld[1][i] != symbol and fld[2][i] != symbol and fld[1][i] != " " and fld[2][i] != " " and fld[0][i] == " ":
                    x = abs(-1 - i)
                    y = 3
                    break
                if fld[0][i] != symbol and fld[2][i] != symbol and fld[0][i] != " " and fld[2][i] != " " and fld[1][i] == " ":
                    x = abs(-1 - i)
                    y = 2
                    break
                    """
        for i in range(3):
            count1 = count2 = 0
            bestJ = 0
            for j in range(3):
                if fld[i][j] == symbol:
                    count1 += 1
                if fld[i][j] == ' ':
                    count2 += 1;
                    bestJ = j
            if count2 == 1 and count1 == 2:
                x = i
                y = bestJ
                coord_ai = [x, y]
                return self.reformat(coord_ai)
            if count2 == 1 and count1 == 0:
                x = i
                y = bestJ
                coord_ai = [x, y]
                return self.reformat(coord_ai)

        for i in range(3):
            count1 = count2 = 0
            for j in range(3):
                if fld[j][i] == symbol:
                    count1 += 1
                if fld[j][i] == ' ':
                    count2 += 1
                    bestJ = j
            if count2 == 1 and count1 == 2:
                x = bestJ
                y = i
                coord_ai = [x, y]
                return self.reformat(coord_ai)
            if count2 == 1 and count1 == 0:
                x = bestJ
                y = i
                coord_ai = [x, y]
                return self.reformat(coord_ai)

        count1 = count2 = 0
        if fld[0][0] == symbol:
            count1 += 1
        if fld[0][0] == ' ':
            count2 += 1
            bestI = 0
            bestJ = 0
        if fld[1][1] == symbol:
            count1 += 1
        if fld[1][1] == ' ':
            count2 += 1
            bestI = 1
            bestJ = 1
        if fld[2][2] == symbol:
            count1 += 1
        if fld[2][2] == ' ':
            count2 += 1
            bestI = 2
            bestJ = 2
        if count2 == 1 and count1 == 2:
            x = bestI
            y = bestJ
            coord_ai = [x, y]
            return self.reformat(coord_ai)
        if count2 == 1 and count1 == 0:
            x = bestI
            y = bestJ
            coord_ai = [x, y]
            return self.reformat(coord_ai)
        count1 = count2 = 0
        if fld[0][2] == symbol:
            count1 += 1
        if fld[0][2] == ' ':
            count2 += 1
            bestI = 0
            bestJ = 2
        if fld[1][1] == ' ':
            count2 += 1
            bestI = 1
            bestJ = 1
        if fld[1][1] == symbol:
            count1 += 1
        if fld[2][0] == symbol:
            count1 += 1
        if fld[2][0] == ' ':
            count2 += 1
            bestI = 2
            bestJ = 0
        if count2 == 1 and count1 == 2:
            x = bestI
            y = bestJ
            coord_ai = [x, y]
            return self.reformat(coord_ai)
        if count2 == 1 and count1 == 0:
            x = bestI
            y = bestJ
            coord_ai = [x, y]
            return self.reformat(coord_ai)

        x = random.randint(0, 2)
        y = random.randint(0, 2)
        coord_ai = [x, y]
        return self.reformat(coord_ai)


    """ def check_win(self, count_empties, count_my_symbols):
        if count_empties != 1:
            return False
        elif count_my_symbols == 2:
            return True
        else:
            return False

    def is_row_win(self, fld, symbol, row):
        count_empties = 0
        count_my_symbols = 0
        for i in range(3):
            if fld[row][i] == " ":
                count_empties += 1
            if fld[row][i] == symbol:
                count_my_symbols += 1
        return self.check_win(count_empties, count_my_symbols)


    def is_diag_win(self, fld, symbol, diag):
        count_empties = 0
        count_my_symbols = 0
        for i in range(3):
            pass


    def is_column_win(self, fld, symbol, column):
        count_empties = 0
        count_my_symbols = 0
        for i in range(3):
            if fld[i][column] == " ":
                count_empties += 1
            if fld[i][column] == symbol:
                count_my_symbols += 1
        return self.check_win(count_empties,count_my_symbols)
    """


class HardStrategy(Strategy):

    def move(self, fld, symbol):
        print('Making move level "hard"')
        bestScore = -1
        bestI = 0
        bestJ = 0
        for i in range(3):
            for j in range(3):
                if fld[i][j] == " ":
                    score = self.minimax(fld, i, j, 0, symbol)
                    if bestScore == -1 or (bestScore < score):
                        bestScore = score
                        bestI = i
                        bestJ = j
        best = [bestI, bestJ]
        return self.reformat(best)

    def reformat(self, best):
        if best[0] == 0 and best[1] == 0:
            coord_ai = [1, 3]
        elif best[0] == 0 and best[1] == 1:
            coord_ai = [2, 3]
        elif best[0] == 0 and best[1] == 2:
            coord_ai = [3, 3]
        elif best[0] == 1 and best[1] == 0:
            coord_ai = [1, 2]
        elif best[0] == 1 and best[1] == 1:
            coord_ai = [2, 2]
        elif best[0] == 1 and best[1] == 2:
            coord_ai = [3, 2]
        elif best[0] == 2 and best[1] == 0:
            coord_ai = [1, 1]
        elif best[0] == 2 and best[1] == 1:
            coord_ai = [2, 1]
        elif best[0] == 2 and best[1] == 2:
            coord_ai = [3, 1]
        return coord_ai

    def who_wins(self, fld):
        for i in range(3):
            if fld[i][0] == fld[i][1] == fld[i][2] != " ":
                return "wins"
        for i in range(3):
            if fld[0][i] == fld[1][i] == fld[2][i] != " ":
                return "wins"
        if fld[0][0] == fld[1][1] == fld[2][2] != " " or fld[0][2] == fld[1][1] == fld[2][0] != " ":
            return "wins"
        for i in range(3):
            for j in range(3):
                if fld[i][j] == " ":
                    return "game not finished"
        return "draw"

    def minimax(self, fld, curI, curJ, turn, symbol):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for i in range(3):
            for j in range(3):
                board[i][j] = fld[i][j]
        if turn == 0:
            board[curI][curJ] = symbol
        else:
            if symbol == "O":
                board[curI][curJ] = "X"
            else:
                board[curI][curJ] = "O"
        bestScore = -1

        if self.who_wins(board) == "wins":
            if turn == 0:
                return 10
            else:
                return -10
        elif self.who_wins(board) == "draw":
            return 0
        else:
            pass

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    score = self.minimax(board, i, j, abs(turn - 1), symbol)
                    if bestScore == -1 or (turn == 1 and bestScore < score) or (turn == 0 and bestScore > score):
                        bestScore = score
        return bestScore


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


def is_win(fld, symbol):
    for i in range(3):
        if fld[i][0] == fld[i][1] == fld[i][2] == symbol:
            if symbol == "X":
                return "X wins"
            else:
                return "O wins"
    for i in range(3):
        if fld[0][i] == fld[1][i] == fld[2][i] == symbol:
            if symbol == "X":
                return "X wins"
            else:
                return "O wins"
    if fld[0][0] == fld[1][1] == fld[2][2] == symbol or fld[0][2] == fld[1][1] == fld[2][0] == symbol:
        if symbol == "X":
            return "X wins"
        else:
            return "O wins"
    for i in range(3):
        for j in range(3):
            if fld[i][j] == " ":
                return "Game not finished"
    return "Draw"


field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

first_turn_flag = True

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
            if first_turn_flag:
                player1 = create_player(type1, "X")
                coord_player1 = player1.get_move(type1, field)
                a = coord_player1[0]
                b = coord_player1[1]
                if check_params(a, b) == 0:
                    fill(field, a, b, player1.get_symbol())
                    print_field(field)
                    first_turn_flag = False
                    if is_win(field, player1.get_symbol()) != "Game not finished":
                        print(is_win(field, player1.get_symbol()))
                        field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                        first_turn_flag = True
                        break
            else:
                player2 = create_player(type2, "O")
                coord_player2 = player2.get_move(type2, field)
                a1 = coord_player2[0]
                b1 = coord_player2[1]
                if check_params(a1, b1) == 0:
                    fill(field, a1, b1, player2.get_symbol())
                    print_field(field)
                    first_turn_flag = True
                    if is_win(field, player2.get_symbol()) != "Game not finished":
                        print(is_win(field, player2.get_symbol()))
                        field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                        first_turn_flag = True
                        break
    elif command == "exit":
        break
    else:
        print("Bad parameters!")
        continue
