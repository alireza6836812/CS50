import math
from copy import deepcopy

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
    nX = 0
    nO = 0

    for i in board:
        nX = i.count(X) + nX
        nO = i.count(O) + nO

    if nX <= nO:
        return (X)
    else:
        return (O)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    move = set()
    p1 = enumerate(board)
    for i, j in p1:
        p2 = enumerate(j)
        for k, l in p2:
            if l == None:
                p1.add((i, k))

    return (p1)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    move = player(board)
    new = deepcopy(board)

    if board[i][j] != None:
        raise (Exception)
    else:
        new[i][j] = move

    return (new)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        for i in board:
            if i == [player] * 3:
                return (player)

        for i in range(3):
            j = [board[x][i] for x in range(3)]
            if j == [player] * 3:
                return (player)

        if [board[i][i] for i in range(0, 3)] == [player] * 3:
            return (player)

        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return (player)
    return (None)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return (True)
    for i in board:
        if EMPTY in i:
            return (False)
    return (True)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)

    if win == X:
        return (1)
    elif win == O:
        return (-1)
    else:
        return (0)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        move1 = ()
        if terminal(board):
            return (utility(board), move1)
        else:
            p = -5
            actions = actions(board)
            for action in actions:
                minval = min_value(result(board, action))[0]
                if minval > p:
                    p = minval
                    move1 = action
            return (v, move1)

    def min_value(board):
        move1 = ()
        if terminal(board):
            return utility(board), move1
        else:
            p = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < p:
                    p = maxval
                    move1 = action
            return (p, move1)

    theplayer = player(board)

    if terminal(board):
        return (None)

    if theplayer == X:
        return (max_value(board)[1])

    else:
        return (min_value(board)[1])
