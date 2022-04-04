import copy
import random
VIC=10**20 #The value of a winning board (for max)
LOSS=-VIC #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=8 #The length of a winning sequence
COMPUTER=True #Marks the computer's cells on the board
HUMAN=False #Marks the human's cells on the board



def create():
    board=[]
    for i in range(SIZE):
        rand= lambda :random.randrange(-6,16)
        board=board+[[rand() for j in range(SIZE)]]
    r=random.randrange(0,SIZE)
    c=random.randrange(0,SIZE)
    board[r][c]='x'

    '''
    board=[[1,5,-5],['x',-5,9],[12,8,12]]
    '''
    return [board,0.00001,HUMAN,SIZE*SIZE-1,[r,c],0,0]


def whoIsFirst(s):
#The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : "))==1:
        s[2]=COMPUTER
    else:
        s[2]==HUMAN

def isHumTurn(s):
#Returns True iff it the human's turn to play
    return s[2]==HUMAN

def value(s):
#Returns the heuristic value of s
    return s[1]


def isFinished(s):
#Returns True if the game ended
    return s[3] == 0 or isEmpty(s)


def isEmpty(s):
    if isHumTurn(s):
        r = s[4][0]
        c = s[4][1]
        for i in range(SIZE):
            if s[0][r][i] != 'x' and i!=c :
                return False
        return True
    else:
        r = s[4][0]
        c = s[4][1]
        for i in range(SIZE):
            if s[0][i][c] != 'x' and i != r:
                return False
        return True

def printState(s):
    ln = "-------"
    ln =ln * (SIZE)
    for r in range(len(s[0])):
        print("\n",ln,"\n|", end="")
        for c in range(len(s[0][0])):
            if s[0][r][c]=='x'and not (r==s[4][0] and c==s[4][1]):
                print("      |" ,end="")
            elif r==s[4][0] and c==s[4][1]:
                print (' $**$ |',end="")
            elif len(str(s[0][r][c])) ==1:
                print("  ",s[0][r][c]," |",end="")
            else:
                print(" ", s[0][r][c], " |", end="")
    print("\n",ln,"\n")
    print("your score: ",s[5])
    print("computer's score: ", s[6])

    if isFinished(s):
        if s[6]>s[5]:
            print("Ha ha ha I won!")
        elif s[6]<s[5] :
            print("You did it!")
        else:
            print("It's a TIE")



def inputMove(s):
    printState(s)
    flag=True
    while flag:
        move = int(input("Enter number of places to move: "))
        temp=s[4][1]+move
        if temp<0 or temp> SIZE or s[0][s[4][0]][temp]=='x':
            print("Ilegal move.")
        else:
            flag=False
            makeMove(s,s[4][0],temp)


def makeMove(s,r,c):
    s[4] = [r, c]
    s[3] -=1

    if isHumTurn(s):
        s[5] += s[0][r][c]
    else:
        s[6] += s[0][r][c]
    s[1] = s[6] - s[5]

    s[2] = not s[2]
    s[0][r][c] = 'x'




def getNext(s):
    ns=[]
    if isHumTurn(s):
        for i in range(len(s[0])):
            if i!=s[4][1] and s[0][s[4][0]][i]!='x':
                tmp = copy.deepcopy(s)
                makeMove(tmp, s[4][0], i)
                ns += [tmp]
    else:
        for i in range(len(s[0])):
            if i!=s[4][0] and s[0][i][s[4][1]]!='x':
                tmp = copy.deepcopy(s)
                makeMove(tmp,i , s[4][1])
                ns += [tmp]

    ns.sort(key=value,reverse=True)

    return ns


