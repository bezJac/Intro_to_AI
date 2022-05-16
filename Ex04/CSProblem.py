# Menachem Heller 305567943
# Bezalel Jacober  312033236


# SUDOKU
import math

# import CSPSolver
# board - The variables' value are in a list of the (N*N)*(N*N) board cells
#            (a vector representing a mat.).
# an empty cell contains 0.
#
# d - The domains are a list of lists - the domain of every var.
#
# The state is a list of 2 lists: the vars. and the domains.

N = 0


def create(fpath='sudoku.txt'):
    global N
    board = read_board_from_file(fpath)  # get the current board
    N = int(len(board) ** 0.25)
    d = []

    # create a domain for each var in the board
    for i in range(len(board)):
        # if var already has a value assigned, only the current value is in domain
        if board[i] != 0:
            d.append([board[i]])  # add current var domain to the list of domains

        # var is currently unassigned with a value
        else:
            temp = list(range(1, (N*N)+1))  # create domain with all default values
            for j in list_of_constraining_vars(board, i):  # get all vars influencing current var
                if board[j] in temp:  # remove from the domain the values of the influencing vars
                    temp.remove(board[j])
            d.append(temp)  # add current var i's domain to the list of domains

    p = [board, d]  # state containing the board and the list of domains
    return p


def list_of_constraining_vars(board, v):
    # Returns a list of non-free vars. whose value will influence
    # the domain of v
    r = list(range(N ** 4))  # get size of board
    r.remove(v)  # remove v from board
    l = []
    for i in r:  # loop through board , add to the list all non-free vars that will be influenced by v since their value
        # in return influence v's domain
        if board[i] != 0 and not is_consistent(board, v, i, 1, 1):
            l += [i]
    return l  #


def read_board_from_file(fpath):
    f = open(fpath, "r")
    board = []
    s = f.readline()
    while s != "":
        for i in s.split():
            board += [int(i)]
        s = f.readline()
    f.close()
    return board


def domain(problem, v):
    # Returns the domain of v
    return problem[1][v][:]


def domain_size(problem, v):
    # Returns the domain size of v
    return len(problem[1][v])


def assign_val(problem, v, x):
    # Assigns x in var. v
    problem[0][v] = x


def get_val(problem, v):
    # Returns the val. of v
    return problem[0][v]


def erase_from_domain(problem, v, x):
    # Erases x from the domain of v
    problem[1][v].remove(x)


def get_list_of_free_vars(problem):
    # Returns a list of vars. that were not assigned a val.
    l = []
    for i in range(len(problem[0])):
        if problem[0][i] == 0:
            l += [i]
    return l


def is_solved(problem):
    # Returns True iff the problem is solved
    for i in range(len(problem[0])):
        if problem[0][i] == 0:
            return False
    return True


def is_consistent(problem, v1, v2, x1, x2):
    # return True , if the assignment of x1 to v1,x2 to v2
    # is consistent and does not violate any of the constraints
    # in sudoku the constraints are -> equal values cannot be in same row, cell, or block (of N*N), on the board

    if x1 != x2:  # values are not equal -assignment consistent with constraints return True
        return True

    # values are equal:

    # (index of var in the board) % (length of a row in the board) gets the index of column on board
    # where var is located
    col1 = v1 % (N ** 2)
    col2 = v2 % (N ** 2)
    if col1 == col2:  # if both vars are in same column - constraint is violated - return False
        return False

    # (index of var in the board) // (length of a row in the board) gets the index of row on board
    # where var is located
    row1 = v1 // (N ** 2)
    row2 = v2 // (N ** 2)
    if row1 == row2:  # if both vars are in same row - constraint is violated - return False
        return False

    # row % N  = number of rows current row is removed from row beginning the block of the given row
    # if both var's row index after subtraction of the difference from block beginning  are equal - both vars are in
    # same block from the row perspective
    # column % N  = number of columns current column is removed from column beginning the block of the given column
    # if both var's column index after subtraction of the difference from block beginning  are equal - both vars are in
    # same block from the column perspective
    # if both conditions are met , vars are actually in the same block - constraint is violated - return False
    if row1 - (row1 % N) == row2 - (row2 % N) and col1 - (col1 % N) == col2 - (col2 % N):
        return False

    # vars are not in same row, column, or block - no constraints are violated by assignment - return True
    return True


# Returns True iff v1=x1 and v2=x2 is consistent with all constraints
# your code here

def list_of_influenced_vars(problem, v):
    # Returns a list of free vars. whose domain will be
    # influenced by assigning a val. to v
    r = list(range(N ** 4))
    r.remove(v)
    l = []
    for i in r:
        if problem[0][i] == 0 and not is_consistent(problem, v, i, 1, 1):
            l += [i]
    return l


def present(problem, solved=False):
    print()
    if solved:
        print("SOLVED:")
    for i in range(len(problem[0])):
        if i % (N * N) == 0 and i != 0:
            print('||', end='')
            print()
        if i % (N * N * N) == 0:
            print('===================================')
        if i % N == 0:
            print('||', end='')
        x = str(problem[0][i])
        pad = (math.ceil(math.log(N * N, 10)) - len(x))
        print(pad * " ", x, pad * " ", end="")
    print('||\n===================================')
