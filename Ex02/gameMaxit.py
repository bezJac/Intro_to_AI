import copy
import random
VIC=10**20 #The value of a winning board (for max)
LOSS=-VIC #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=3 #The length of a winning sequence
COMPUTER=True #Marks the computer's cells on the board
HUMAN=False #Marks the human's cells on the board
SELECTED='x'


def create():
    board=[]
    for i in range(8):
        rand= lambda :random.randrange(-6,16)
        board=board+[[rand() for j in range(8)]]
    return [board,0.00001,HUMAN,64,(random.randrange(0,8),random.randrange(0,8)),(0,0)]


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
    return s[3] ==0


def printState(s):
    for r in range(len(s[0])):
        print("\n -- -- -- -- -- -- -- -- -- -- -- --\n|", end="")
        for c in range(len(s[0][0])):
            if s[0][r][c]=='x':
                print("  |" ,end="")
            elif (r,c)==s[4]:
                print ('$',s[0][r][c],'$ |',end="")
            else:
                print(s[0][r][c]," |",end="")
    print("\n -- -- -- -- -- -- -- -- -- -- -- -- --\n")
    if value(s)==VIC:
        print("Ha ha ha I won!")
    elif value(s)==LOSS:
        print("You did it!")
    elif value(s)==TIE:
        print("It's a TIE")


def inputMove(s):
    printState(s)
    flag=True
    while flag:
        move = int(input("Enter number of places to move: "))
        temp=s[4][1]+move
        if temp<0 or temp> 7 or s[0][s[4][0]][temp]=='x':
            print("Ilegal move.")
        else:
            flag=False
            makeMove(s,s[4][0],temp)


def makeMove(s,r,c):
    if isHumTurn(s):
        s[5][0]+=s[0][r][c]
        lst=[]
        for i in range(8):
            if s[0][r][i]!='x'and s[0][r][i]!=c:
                lst.append(s[0][r][c]-s[0][r][i])
        s[1]=min(lst)
    else:
        s[5][1] += s[0][r][c]

    s[2]=not s[2]
    s[3]-=1



def getNext(s):
    ns=[]
    if isHumTurn(s):
        for i in range(len(s[0])):
            if i!=s[4][1]:
                tmp = copy.deepcopy(s)
                makeMove(tmp, s[4][0], i)
                ns += [tmp]
    else:
        for i in range(len(s[0])):
            if i!=s[4][0]:
                tmp = copy.deepcopy(s)
                makeMove(tmp,i , s[4][1])
                ns += [tmp]

    ns.sort(key=value,reverse=True)

    return ns


printState(create())