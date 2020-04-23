"""
Tic Tac Toe Player
"""

import math
X = "X"
O = "O"

Turn = None
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #done@p
    global Turn
    if(Turn == X):
        Turn=O
    elif(Turn == O):
        Turn=X
    else:
        startp=0
        for i in range(3):
            for j in range(3):
                if (board[i][j] == None):
                    startp +=1
        if(startp==9):
            Turn=X

    #print("player:",Turn)
    return Turn

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #done@p
    move=[]
    for i in range(3):
        for j in range(3):
            if (board[i][j] == None):
                move.append((i,j))

    return move
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #done@p
    for i in range(3):
        for j in range(3):
            if ((i,j)== action):
                board[i][j] = Turn
    return board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #done@p
    winner=None
    if(utility(board)==1):
        winner=X
    elif(utility(board)==-1):
        winner=O
    elif(utility(board)==0):
        winner=None
    else:
        print("winner error")
    return winner
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #done@p
    a=[(0,0),(0,1),(0,2)]
    b=[(1,0),(1,1),(1,2)]
    c=[(2,0),(2,1),(2,2)]
    d=[(0,0),(1,1),(2,2)]
    e=[(2,0),(1,1),(0,2)]
    f=[(0,0),(1,0),(2,0)]
    g=[(0,1),(1,1),(2,1)]
    h=[(0,2),(1,2),(2,2)]
    #SOLUTION STATE
    z=[a,b,c,d,e,f,g,h]
    x=[]
    o=[]
    none=0
    over= None
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                x.append((i,j))
                for w in z:
                    if(set(w).issubset(set(x))):
                        over=True

            elif (board[i][j] == O):
                o.append((i,j))
                for w in z:
                    if((set(w).issubset(set(o)))):
                        over=True
            elif (board[i][j] == None):
                none+=1

    if(over==None and none==0):
        #print("overed")
        over=True
    else:
        if(over==None and none>0):
            over=False


    #print("terminal:",over)
    return over
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #done@p
    a=[(0,0),(0,1),(0,2)]
    b=[(1,0),(1,1),(1,2)]
    c=[(2,0),(2,1),(2,2)]
    d=[(0,0),(1,1),(2,2)]
    e=[(2,0),(1,1),(0,2)]
    f=[(0,0),(1,0),(2,0)]
    g=[(0,1),(1,1),(2,1)]
    h=[(0,2),(1,2),(2,2)]
    #SOLUTION STATE
    z=[a,b,c,d,e,f,g,h]
    x=[]
    o=[]
    none=0
    win=None
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                x.append((i,j))
                for w in z:
                    if(set(w).issubset(set(x))):
                        win=1

            elif (board[i][j] == O):
                o.append((i,j))
                for w in z:
                    if((set(w).issubset(set(o)))):
                        win=-1
            elif (board[i][j] == None):
                none+=1
    if(win==None and none==0):
        win=0
    else:
        if(win==None and none>0):
            win=None  #error state


    #print("utlity:",win)
    return win
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    global Turn
    preTurn=Turn
    prev=[]
    for i in range(3):
        for j in range(3):
            prev.append(board[i][j])
    #print("START board",prev)
    q=[]
    if Turn==X:
        print("x turns")
        q.append(Max(board))
    else:
        print("O turns")
        q.append(Min(board))

    for i in range(3):
        for j in range(3):
            board[i][j] = prev[0]
            prev.remove(prev[0])
    #print("IS these starting board",board)
    Turn=preTurn
    for h,j in q:
        l=j
    print("Turn:",Turn)
    print("optimum sol:",j)
    return j

def Min(board):
    #print("============================================min board opens")

    prev=[]
    for i in range(3):
        for j in range(3):
            prev.append(board[i][j])

    decisionlist=[]
    finallist=[]
    k=0
    global Turn
    Turn=O
    for i,j in actions(board):
        Turn=O
        board=result(board, (i,j))
        print("board min",board)
        if(terminal(board)==True):
            if(utility(board)==1):
                decisionlist.append((1,(i,j)))
                #print("board value is 1")

            elif(utility(board)==0):
                decisionlist.append((0,(i,j)))
                #print("board value is 0")

            elif(utility(board)==-1):
                decisionlist.append((-1,(i,j)))
                #print("board value is -1")

        else:
            r=[]
            r.append(Max(board))
            for y,g in r:
                decisionlist.append((y,(i,j)))
        k=0
        for i in range(3):
            for j in range(3):
                board[i][j] = prev[k]
                k+=1
        #print(board,"<<<<<<<<<",k,"<<<<<<<<",prev)



    print("min",decisionlist)
    finallist=min(decisionlist,key = lambda i: i[0])
    print("Turn:",Turn)
    print("finallist:",finallist)

    #print("============================================min board close")
    return finallist

def Max(board):
    #print("---------------------------------------------max board opens")

    prev=[]
    for i in range(3):
        for j in range(3):
            prev.append(board[i][j])

    decisionlist=[]
    finallist=[]
    k=0
    global Turn
    Turn=X
    for i,j in actions(board):
        Turn=X
        board=result(board, (i,j))
        print("board max",board)
        if(terminal(board)==True):
            if(utility(board)==1):
                decisionlist.append((1,(i,j)))
                #print("board value is 1")

            elif(utility(board)==0):
                decisionlist.append((0,(i,j)))
                #print("board value is 0")

            elif(utility(board)==-1):
                decisionlist.append((-1,(i,j)))
                #print("board value is -1")

        else:
            r=[]
            r.append(Min(board))
            for y,g in r:
                decisionlist.append((y,(i,j)))
        k=0
        for i in range(3):
            for j in range(3):
                board[i][j] = prev[k]
                k+=1
        #print(board,">>>>>>>>>",k,">>>>>>>>",prev)


    print("max",decisionlist)
    finallist=max(decisionlist,key = lambda i: i[0])
    print("Turn:",Turn)
    print("finallist:",finallist)

    #print("---------------------------------------------max board close")
    return finallist
