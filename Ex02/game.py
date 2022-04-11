import copy
import random

SIZE = 8  # size of rows and columns in board
COMPUTER = True  # Marks the computer's turn to play
HUMAN = False  # Marks the human's turn to play

def create():
    # initialize a game with a new board
    board = []
    for i in range(SIZE):  # board contains N =SIZE list each one comtaining N =Size values
        rand = lambda: random.randrange(-6, 16)  # set values to random integers in given range
        board = board + [[rand() for j in range(
            SIZE)]]  # use list comprehension to initialize the values to random integers in given range
    r = random.randrange(0, SIZE)  # pick random row index for game starting cell
    c = random.randrange(0, SIZE)  # pick random column index for game starting cell
    board[r][c] = 'x'  # mark game starting cell's value as deleted

    # each state holds : [game board , heuristic value of state , turn , number of cells left in board to pick,
    # currently picked cell indexes in a list , total point accumulated by user , total points accumulated by computer]
    return [board, 0.00001, HUMAN, SIZE * SIZE - 1, [r,c], 0, 0]  # initialize first state


def whoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[2] = COMPUTER
    else:
        s[2] == HUMAN


def isHumTurn(s):
    # Returns True iff it the human's turn to play
    return s[2] == HUMAN


def value(s):
    # Returns the heuristic value of s
    return s[1]


def isFinished(s):
    # Returns True if the game ended
    # game ends if one of following accures:
    # 1) no cells left in board to pick from
    # 2) current marked cell's row ( if it's the human's turn), or cell ( if it's the computer's turn) are empty
    return s[3] == 0 or isEmpty(s)


def isEmpty(s):
    # check if current marked cell's row is empty, for human turn , or column is empty for computer turn
    r = s[4][0]  # get the row index of current selected cell from state
    c = s[4][1]  # get the column index of current selected cell from state
    if isHumTurn(s):  # for human turn , check row
        for i in range(SIZE):  # for all cells in row except currently picked one check:
            if s[0][r][i] != 'x' and i != c:  # if cell has a value , row is not empty, return false
                return False
        return True  # loop was exited , all cells are marked as deleted , row is empty, return true
    else:  # for computer's turn check column
        for i in range(SIZE):  # for all cells in column except currently picked one check:
            if s[0][i][c] != 'x' and i != r:  # if cell has a value , row is not empty, return false
                return False
        return True  # loop was exited , all cells are marked as deleted , row is empty, return true


def printState(s):
    # print the current board game
    ln = "-------"
    ln = ln * (SIZE)
    for r in range(len(s[0])):
        print("\n", ln, "\n|", end="")
        for c in range(len(s[0][0])):
            if s[0][r][c] == 'x' and not (r == s[4][0] and c == s[4][1]):  # cell was already picked print a blank space
                print("      |", end="")
            elif r == s[4][0] and c == s[4][1]:  # cell is the currently picked cell , print marker to identify it
                print(' $**$ |', end="")
            elif len(str(s[0][r][c])) == 1:  # print cells with values
                print("  ", s[0][r][c], " |", end="")  # single digit positive values
            else:
                print(" ", s[0][r][c], " |", end="")  # double digit or negative values
    print("\n", ln, "\n")
    print("your score: ", s[5])  # print current human score
    print("computer's score: ", s[6])  # print current computer score

    if isFinished(s):  # if game has finished print result of game
        if s[6] > s[5]:  # computer's total point is greater than human's total
            print("Ha ha ha I won!")
        elif s[6] < s[5]:  # human's total point is  greater than computer's  total
            print("You did it!")
        else:  # total point of human and computer is equal
            print("It's a TIE")


def inputMove(s):
    # move marker to a cell on the currently picked cell row for human player
    printState(s)  # print current state
    flag = True
    while flag:
        move = int(input("Enter number of columns to move, positive number for right, negative for left: "))
        if move == 0:
            print("zero is an invalid input")
        else:
            temp = s[4][1] + move  # calculate index of column user wants to move to on same row
            if temp < 0 or temp >= SIZE or s[0][s[4][0]][temp] == 'x':  # check if index is beyond boundaries of board or cell has already been picked
                print("Ilegal move.")  # move is illegal get input again from user
            else:  # move is legal
                flag = False  # set flag end input loop
                makeMove(s, s[4][0], temp)  # move marker to requested cell

'''
היורסטיקה הנבחרת היא: סכום הנקודות שצבר המחשב פחות סכום הנקודות שצבר השחקן.
ההיגיון הוא: שיש ענין שיהיה ערך מספרי כלשהו עבור כל מצב, 
כלומר כאשר אין מוטיבציה לחשב צעדים קדימה אלא לתת ערך למצב הלוח ברגע זה. 
כשנשתמש ביוריסטיקה שנבחרה הערך הגבוה ביותר יחשב לנו את הבחירה המוצלחת ביותר עבור המחשב, ולהפך עבור השחקן
'''


def makeMove(s, r, c):
    # make a move in the game
    s[4] = [r, c]  # update current selected cell indexes
    s[3] -= 1  # subtract 1 from total cell's left in board to pick from
    if isHumTurn(s):  # if it's the human's turn
        s[5] += s[0][r][c]  # add value of picked cell to human's total
    else:  # if it's the computer's turn
        s[6] += s[0][r][c]  # add value of picked cell to human's total
    s[1] = s[6] - s[5]  # heuristic value of a state set as the computer's current total score minus the human current
    # total score
    s[2] = not s[2]  # switch turn between Human (== True) and Computer ( ==False)
    s[0][r][c] = 'x'  # mark selected cell as deleted


def getNext(s):
    # get list of next possible move , used for computer's AI
    ns = []
    if isHumTurn(s): # if current turn is human's:
        for i in range(len(s[0])): # for all available cells in current picked cell row:
            if i != s[4][1] and s[0][s[4][0]][i] != 'x': # if cell is not the current picked one and is not empty
                tmp = copy.deepcopy(s) # copy the state
                makeMove(tmp, s[4][0], i) # send copy to make move function to execute the move
                ns += [tmp] # add the move ( state ) to the next state list
        ns.sort(key=value) # sort move by heuristic value in ascending order (human is min)

    else: # if current turn is computer's:
        for i in range(len(s[0])): # for all available cells in current picked cell column:
            if i != s[4][0] and s[0][i][s[4][1]] != 'x':# if cell is not the current picked one and is not empty
                tmp = copy.deepcopy(s) # copy the state
                makeMove(tmp, i, s[4][1])# send copy to make move function to execute the move
                ns += [tmp] # add the move ( state ) to the next state list

        ns.sort(key=value, reverse=True) # sort move by heuristic value in descending order (computer is max)

    return ns
