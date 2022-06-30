# Menachem Heller 305567943
# Bezalel Jacober 312033236


'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''

import random
import math


# returns a random board nXn
def create(n):
    s = list(range(n * n))  # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m = "<>v^"  # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n ** 3):  # makes n^3 random moves to mix the tiles
        if_legal(s, m[random.randrange(4)])
    return [s, ""]  # at the beginning "" is an empty path, later on path
    # contains the path that leads from the initial state to the state


def get_next(x):  # returns a list of the children states of x
    ns = []  # the next state list
    for i in "<>v^":
        s = x[0][:]  # [:] - copies the board in x[0]
        if_legal(s, i)  # try to move in direction i
        # checks if the move was legal and...
        if s.index(0) != x[0].index(0) and \
                (x[1] == "" or x[1][-1] != "><^v"[
                    "<>v^".index(i)]):  # check if it's the first move or it's a reverse move
            ns.append([s, x[1] + i])  # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])


def is_target(x):
    n = len(x[0])  # the size of the board
    return x[0] == list(range(n))  # list(range(n)) is the target state


#############################
def if_legal(x, m):  # gets a board and a move and makes the move if it's legal
    n = int(math.sqrt(len(x)))  # the size of the board is nXn
    z = x.index(0)  # z is the place of the empty tile (0)
    if z % n > 0 and m == "<":  # checks if the empty tile is not in the first col and the move is to the left
        x[z] = x[z - 1]  # swap x[z] and x[z-1]...
        x[z - 1] = 0  # ...and move the empty tile to the left
    elif z % n < n - 1 and m == ">":  # check if the empty tile is not in the n's col and the move is to the right
        x[z] = x[z + 1]
        x[z + 1] = 0
    elif z >= n and m == "^":  # check if the empty tile is not in the first row and the move is up
        x[z] = x[z - n]
        x[z - n] = 0
    elif z < n * n - n and m == "v":  # check if the empty tile is not in the n's row and the move is down
        x[z] = x[z + n]
        x[z + n] = 0


####################################
'''
שאלה 2: 
היוריסטיקה מתקבלת מכיוון שעומדת בדרישות של היוריסטיקה עבור אלגוריתם A*:

H(n)>=0
 מכיוון שמספר הצעדים שידרשו להזזה כדי להגיע למקום החוקי יהיה או אפס (אם הוא נמצא כבר בשורה או בעמודה הרצויה) 
 או גדול ממנו כאשר הוא לא במקום (האופציה המקסימלית היא N-1 כאשר הערך נמצא בשורה או בעמודה הרחוקה ביותר מהמקום הרצוי ) 
 
H(n)<=H*(n)
מכיוון שאנחנו לוקחים את המקסימלי בין מספר הצעדים הנדרשים בין השורות והעמודות תמיד נקבל ערך,
 או קטן  מהערך האמיתי אם נדרשת הוזזה גם בכיוון ההוזזה שלא נבחר, 
או שווה לו אם הערך שלא נבחר היה אפס (כלומר מספר הצעדים האמיתי שנדרש הוא אכן הערך שקיבלנו)


שאלה 3:
:שימוש בקוד בהתחשבות באורך הדרך שנעשה בלבד בלי היוריסטיקה: (uniform cost)  

[[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^<^>v<^'], 1326092, 581287]

Process finished with exit code 0

-------------------------------------------------------------------------

שימוש בהיוריסטיקה הלוקחת בחשבון את מספר הערכים שלא במקום החוקי:

[[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^<^>v<^'], 40175, 16920]

Process finished with exit code 0


---------------------------------------------------------------------------

שימוש בהיוריסטיקה שלוקחת את המקסימלי בין מספר צעדים 
הנדרשים להגעה למקום החוקי בשורות ובעמודות:

[[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^<^>v<^'], 6473, 2608]

Process finished with exit code 0

---------------------------------------------------------------------------


--------------------------------------- לא חלק מדרישות התרגיל -------------------
שימוש בהיוריסטיקה מנהטן:

[[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^^<v>^<'], 4040, 1602]

Process finished with exit code 0'''


def hdistance(s):  # the heuristic value of s
    c = 0
    n = math.sqrt(len(s[0]))  # size of row and col in table
    for i in range(1, len(s[0])):
        index = s[0].index(i)  # get current location of value in the table
        if index != i:
            col = abs(index % n - i % n)  # get number of cols needed to move to get to collect column
            row = abs(int(index / n) - int(i / n))  # get number of cols needed to move to get to correct row
            c += max(col, row)  # add to total distance max value between the two
    return c  # return total distance


'''
def hdistance(s):
    c=0
    for i in range(1,len(s[0])):
        if s[0].index(i)!=i:
            c+=1
    return c
'''
