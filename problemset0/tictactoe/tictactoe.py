"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
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
    movecount = 0
    for row in board:
        movecount += row.count(X) + row.count(O)
    #If the number of moves is 0 ie first turn or odd
    if movecount % 2 == 0:
        return X
    else:
        return O
        

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for rowindex, row in enumerate(board):
        for boxindex, box in enumerate(row):
            if box is EMPTY:
                actions.add((rowindex, boxindex))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    if action not in actions(board):
        raise NameError('Invalid Action')
    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check rows and columns
    for index in range(3):
        #Rows
        if board[index][0] == board[index][1] == board[index][2] != EMPTY:
            return board[index][0]
        #Columns
        if board[0][index] == board[1][index] == board[2][index] != EMPTY:
            return board[0][index]
    #Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != EMPTY) or (board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return board[1][1]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None and len(actions(board)) != 0:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    util = {X:1,O:-1,None:0}
    return util[winner(board)]

def minvalue(board, a=-math.inf, b=math.inf):
    if terminal(board):
        return utility(board)
    v = math.inf
    avail_actions = actions(board)
    for action in avail_actions:
        v = min(v, maxvalue(result(board, action), a, b))
        b = (min(b, v))
        if b < a:
            break
    return v
    
def maxvalue(board, a=-math.inf, b=math.inf):
    if terminal(board):
        return utility(board)
    v = -math.inf
    avail_actions = actions(board)
    for action in avail_actions:
        v = max(v, minvalue(result(board, action), a, b))
        a = (max(a, v))
        if a > b:
            break
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    avail_actions = actions(board)
    if player(board) == X:
        optimal_action = ()
        v = -math.inf
        for action in avail_actions:
            vnew = minvalue(result(board, action)) 
            if vnew > v:
                optimal_action = action
                v = vnew
    else:
        optimal_action = ()
        v = math.inf
        for action in avail_actions:
            vnew = maxvalue(result(board, action)) 
            if vnew < v:
                optimal_action = action
                v = vnew
    return optimal_action
