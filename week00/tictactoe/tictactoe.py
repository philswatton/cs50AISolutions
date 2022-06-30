"""
Tic Tac Toe Player
"""
import copy
import math

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
    # Count variables
    x = 0
    o = 0

    # Loop over board, counting number of xs and ys
    for row in board:
        for value in row:
            if value == X:
                x += 1
            if value == O:
                o += 1

    # If x = o, x's turn. If x > o, O's turn
    if x == o:
        return X
    if x > o:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # list of actions
    act = []

    # Loop over board
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act.append((i, j))

    # Return list
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    new_board = copy.deepcopy(board)  # avoid overwriting the old board
    new_board[action[0]][action[1]] = p
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Loop over rows
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] is not None:
            return board[i][0]

    # Loop over columns
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check the first diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    # Check the second diagonal
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner if code reaches this point
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check if there is a winner
    w = winner(board)
    if w is not None:
        return True

    # Check if the board still has empty places
    e = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                e += 1
    if e == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Get winner
    w = winner(board)

    # Calculate utility based on winner
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # If terminal return none
    if terminal(board):
        return None

    # Get player
    p = player(board)

    # Best action
    best_act = None

    # Call maximiser
    if p == X:
        util = -2
        for action in actions(board):
            new_util = minimise(result(board, action))
            if new_util > util:
                util = new_util
                best_act = action

    # Call minimiser
    if p == O:
        util = 2
        for action in actions(board):
            new_util = maximise(result(board, action))
            if new_util < util:
                util = new_util
                best_act = action

    # Return
    return best_act


# Maximiser - maximise the minimum possible utility
def maximise(board):

    # If terminal, return the final utility
    if terminal(board):
        return utility(board)

    # Else, search the space
    util = -2
    for action in actions(board):
        new_util = minimise(result(board, action))
        if new_util > util:
            util = new_util
    return util


# Maximiser - maximise the minimum possible utility
def minimise(board):

    # If terminal, return the final utility
    if terminal(board):
        return utility(board)

    # Else, search the space
    util = 2
    for action in actions(board):
        new_util = maximise(result(board, action))
        if new_util < util:
            util = new_util
    return util
