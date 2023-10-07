## RUN runner.py to play the game
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    X_count = 0
    O_count = 0
    for row in board[:]:
        for unit in row:
            X_count = X_count + int(unit=="X")
            O_count = O_count + int(unit=="O")
 
    if X_count == O_count:
        return "X"
    elif X_count > O_count:
        return "O"
    
def actions(board):
    possible_actions = []
    for row_no, row in enumerate(board):
        for col_no, unit in enumerate(row):
            if unit==None:
                possible_actions.append((row_no, col_no))
                
    return possible_actions


def result(board, action):
    (x,y) = action
    dummy = deepcopy(board)
    if dummy[x][y] == None:
        dummy[x][y] = player(board)
    else:
        raise Exception("Invalid Move")
        
    return dummy


def winner(board):
    for row in board:
        if sum(unit== "X" for unit in row) ==3:
            return "X"
        elif sum(unit=="O" for unit in row) ==3:
            return "O"
    
    for i in [0,1,2]:
        if sum(row[i]== "X" for row in board) ==3:
            return "X"
        
        if sum(row[i]== "O" for row in board) ==3:
            return "O"
        
    if sum([board[0][0]=="X", board[1][1]=="X", board[2][2]=="X"]) ==3:
        return "X"
    
    if sum([board[0][2]=="X", board[1][1]=="X", board[2][0]=="X"]) ==3:
        return "X"
    
    if sum([board[0][0]=="O", board[1][1]=="O", board[2][2]=="O"]) ==3:
        return "O"
    
    if sum([board[0][2]=="O", board[1][1]=="O", board[2][0]=="O"]) ==3:
        return "O"
    
    return None


def terminal(board):
    None_count=0
    for row in board:
        None_count = None_count + sum(unit==None for unit in row)
    
    if None_count == 0 or winner(board)!=None:
            return True
    else:
        return False


def utility(board):
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            print(move)
            if v == -1:
                return v, move

    return v, move