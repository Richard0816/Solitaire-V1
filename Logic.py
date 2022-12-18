global board, deck, position_deck, final


def next_move() -> list:
    """
    :return: A list of lists, planning out the sequence of moves
    """

    list_of_moves = generate_moves()

    best_move_set = pick_moves(list_of_moves)

    return best_move_set


def generate_moves():
    """
    :return: A list of all possible moves that we can make to uncover a card
        eg/ [[[0,1], [2,3]], [[0,4]]]
    """

    move_lst = []

    # Check each column
    for i in range(7):
        if can_uncover(i):
            move_lst = move_lst + find_ways_to_uncover_unknown(i)

    return move_lst


def can_uncover(column: int) -> bool:
    """
    :param column: which column are we checking
    :return: True if there is an unknown card, False otherwise
    """
    return "x" in board[column]


def pick_moves(moveset: list) -> list:
    """
    :param moveset: list of all possible moves
    :return: The best possible moves out of the list of moves
        smallest number of moves
    """

    acc = moveset[0]

    for i in moveset:
        if len(i) < len(acc):
            acc = i

    return acc


def find_ways_to_uncover_unknown(column: int) -> list:
    """
    same as find_ways_to_uncover with default as the top shown card
    """

    moves = find_ways_to_uncover(column, board[column].count("x"))

    return moves


def find_ways_to_uncover(column: int, position) -> list:
    """
    :param position: postion of the card we are trying to move out of the way
        /ex. "x", "x", 6, 5
                     ^
                    position 2

    :param column: integer describing which column we wish to uncover
    :return: a matrix with each list with a length of two describing sequences of moves
        /ex. [[0,1], [2,3]]

    For the column we are trying to uncover, work backwards to find a way to uncover the card

    if we are trying to move a 5, we look for a 6, if we can't find one we look for 7 and then a 6 etc.
    """

    # define what card we are trying to move out of the way
    card_to_uncover = board[position]

    if cant_find_larger(card_to_uncover, column):
        return []

    # Make a compressed tree that generates sequences of moves
    # Chose the move set with the lowest move count

    moves = make_tree_for_moves(card_to_uncover, column)

    return moves


def top_shown(column: int):
    """
    :param column: integer describing which column to assess
    :return: a card of form [Number/Face, Suit]

    assumes that there is something to uncover
    """

    for i in range(len(board[column])):
        if i != "x" and i != [0, 0]:
            return board[column][i]
    return [0, 0]


def cant_find_larger(card, column) -> bool:
    """
    :param column: column of the original card
    :param card: Card we are comparing [Number/Face, Suit]
    :return: True if there is a larger card or blank space, False otherwise
    """
    for i in range(7):
        if i != column:
            for j in range(len(board[i])):
                if board[i][j] == [0, 0]:
                    return False
                if board[i][j] != "x":
                    if board[i][j][0] > card[0] and (board[i][j][0] - card[0]) % 2 == (board[i][j][1] - card[1]) % 2:
                        return False
    return True


def make_tree_for_moves(card, column) -> list:
    """
    :param card: Card that we are trying to stack [Number/Face, Suit]
    :param column: Column we are trying to move the card into
    :return: A list of possible move sets
        eg/ [[[0,1], [2,3]], [[0,4]]]
    """

    result = []

    card_to_look_for = [(card[0] + 1) % 14, (card[1] + 1) % 2]

    coords = look_for_x(card_to_look_for)

    if coords is None:
        return []

    for i in range(len(coords)):
        spec = coords[i]
        if spec[0] < 7:
            if spec[1] == len(board[spec[0]]):
                result.append
        elif spec[0] == 7:
            ...
        elif spec[0] > 7:
            ...

    return result


def look_for_x(card) -> list:
    """
    :param card: The card specified that we are looking for [Number/Face, Suit]
    :return: A list of coordinates
        /eg. [[0,1], [8,10]]
        /eg. [[column, row]]

    returns a list with max len = 2

    columns on the board are numbered 0-6

    deck is numbered 7

    final positions are numbered 8-11
    8 - spades
    9 - hearts
    10 - clubs
    11 - diamonds
    """

    lst = []

    for i in range(7):
        for j in range(len(board[i])):
            acc = board[i][j]
            if acc != "x":
                if acc[0] == card[0] and acc[1] % 2 == card[1] % 2:
                    lst.append([i, j])

    for i in range(len(deck)):
        acc = deck[i]
        if acc[0] == card[0] and acc[1] % 2 == card[1] % 2:
            lst.append([7, i])

    x = card[1] % 2

    if final[x] > card[0]:
        lst.append([8 + x, card[0]])

    if final[x + 1] > card[0]:
        lst.append([9 + x, card[0]])

    return lst


'''
def look_for_x_on_board_bottom(x: int, suit: int):
    """
    :param x: int describing what kind of card we are looking for
    :param suit: int describing the suit of the card mod 2
    :return: a list of integers containing columns
        /ex. [0, 1, 2, 3]
    """
    # only care about the colour of the suit
    colour = suit % 2

    result = []

    for i in range(7):
        if board[i][-1][0] == x and board[i][-1][1] % 2 == colour:
            result.append([i, -1])

    return result


def look_for_x_on_board_else():
    pass
'''
