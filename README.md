# Project: Tic-Tac-Toe with AI from [hyperskill.org](https://hyperskill.org/)
## About
Everybody knows this game from childhood. This is the game, where the price of a mistake is too high: it usually costs you the game. You can become a real master of this game by mastering only one possible option, so it also teaches you that simple is always better than complex. What’s the game? Yes, this is Tic-Tac-Toe, also known as noughts and crosses or Xs and Os. It’s meant to be a paper game, but we are programmers, so why not make a game by ourselves? Let’s get started!
## Stages
### Stage 1/5: Initial setup
#### Description
In this project, you'll write a game called Tic-Tac-Toe that you can play with your computer. The computer will have three levels of difficulty - easy, medium, hard.

But, for starters, let's write a program that knows how to work with coordinates and determine the state of the game.

Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:

(1, 3) (2, 3) (3, 3)

(1, 2) (2, 2) (3, 2)

(1, 1) (2, 1) (3, 1)

The program should work in the following way:

Get the 3x3 field from the first input line (it contains 9 symbols containing X, O and _, the latter means it's an empty cell),
Output this 3x3 field with cells before the user's move,
Then ask the user about his next move,
Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input). Since the game always starts with X, if the number of X's and O's on the field is the same, the user should make a move with X, and if X's is one more than O's,  then the user should make a move with O.
Then output the table including the user's most recent move.
Then output the state of the game.
Possible states:

"Game not finished" - when no side has a three in a row but the field has empty cells;
"Draw" - when no side has a three in a row and the field has no empty cells;
"X wins" - when the field has three X in a row;
"O wins" - when the field has three O in a row;
If the user input wrong coordinates, the program should keep asking until the user enters coordinate that represents an empty cell on the field and after that output the field with that move. You should output the field only 2 times - before the move and after a legal move.

### Stage 2/5: Random!
#### Description
Now it is time to make a working game. In this version of the program, the user will be playing as X, and the "easy" level computer will be playing as O. 

Let's make it so that at this level the computer will make random moves. This level will be perfect for those who play this game for the first time! Well, though... You can create a level of difficulty that will always give in and never win the game. You can implement such a level along with "easy" level, if you want, but it will not be tested.

When starting the program, an empty field should be displayed and the first to start the game should be the user as X. Next the computer should make its move as O. And so on until someone will win or there will be a draw.

At the very end of the game you need to print the final result of the game.

### Stage 3/5: Watch 'em fighting
#### Description
It is time to make some variations of the game possible. What if you want to play with a friend and not with AI? What if you get tired of playing the game and want to see a match between two AI? Finally, you need to be able to play either the first move or the second move playing against AI.

Write a menu loop, which can interpret two commands: "start" and "exit".

The command "start" should take two parameters: who will play ‘X’ and who will play ‘O.’ Two parameters are possible for now: "user" to play as a human and "easy" to play as an easy level AI. In the next steps, you will add "medium" and "hard" parameters.

The command "exit" should simply terminate the program.

Do not forget to handle incorrect input!

### Stage 4/5: Intelligent computer
#### Description
Let's write a "medium" level difficulty. Compared to randomly picking a cell to take a move, this level is considerably smarter.

The "medium" level difficulty makes a move using the following process:

If it can win in one move (if it has two in a row), it places a third to get three in a row and win.
If the opponent can win in one move, it plays the third itself to block the opponent to win.
Otherwise, it makes a random move.
Despite the randomness of the third rule, this level is a lot harder to beat. This level stops all simple attempts to beat it due to the second rule, and always wins when it can due to the first rule.

You also should add "medium" parameter to be able to play against this level. And, of course, it should be possible to make "easy" vs "medium" matchup!

### Stage 5/5: The undefeatable...
#### Description
Let's write the "hard" level difficulty.

Compared to the "medium" level difficulty, this level not just go one move ahead to see an immediate win or prevent an immediate loss. This level can see two moves ahead, three moves ahead and so on. Basically, it can see all possible outcomes till the end of the game and choose the best of them considering his opponent also would play perfectly. So, it doesn't rely on the blunders of the opponent, it plays perfectly regardless of the opponent's skill.

The algorithm that implements this is called Minimax. This is the brute force algorithm that maximizes the value of the own position and minimizes the value of the opponent's position. It's not only an algorithm for Tic-Tac-Toe, but for every game with two players with alternate move order, for example, chess. You need to implement it as the "hard" difficulty level. This link will help to understand details.

You also should add "hard" parameter to be able to play against this level.
