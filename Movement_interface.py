import pyautogui
import time

global board, deck, position_deck, final


def move(starting: int, ending: int):
    """
    0: deck
    [1,7]: Board
    [8,11]: Final

    Main interface to move cards

    IF TAKING FROM THE DECK ASSUMES CORRECT CARD IS IN THE TOP POSITION

    :param starting: an integer from [0,11]
    :param ending: an integer from [0,11]
    :return: None
    """
    global position_deck

    # click the starting card or stack
    if starting == 0:
        pyautogui.click(661, 202)
        deck.pop(position_deck)
        position_deck -= 1
    elif 1 <= starting <= 7:
        if ending > 7:
            pyautogui.click(445 + 173 * (starting - 1), coords_bottom((starting - 1)))
        else:
            pyautogui.click(445 + 173 * (starting - 1), 355 + 18 * board[(starting - 1)].count("x"))
    elif starting > 7:
        if starting == 8:
            pyautogui.click(958, 198)
        elif starting == 9:
            pyautogui.click(1124, 198)
        elif starting == 10:
            pyautogui.click(1295, 198)
        elif starting == 11:
            pyautogui.click(1466, 198)

    time.sleep(0.1)

    # click ending
    if 1 <= ending <= 7:
        pyautogui.click(445 + 173 * ending, 355 + 18 * board[ending].count("x"))
    elif ending > 7:
        if ending == 8:
            pyautogui.click(958, 198)
        elif ending == 9:
            pyautogui.click(1124, 198)
        elif ending == 10:
            pyautogui.click(1295, 198)
        elif ending == 11:
            pyautogui.click(1466, 198)


def click_deck(position: int):
    """
    Clicks the deck until the desired card is the one showing from the deck
    :param position: value of the card position we want
    :return: None
    """
    global position_deck, deck
    clicks = 0
    yes = False
    if position < position_deck:
        clicks = len(deck) - (position_deck + 1) + (position + 1) + 1
        yes = True
    elif position > position_deck:
        clicks = position - position_deck
    for i in range(clicks):
        pyautogui.click(449, 195)
        if i == len(deck) - position_deck and yes:
            time.sleep(0.8)
        time.sleep(0.05)
    position_deck = position


def coords_bottom(column: int):
    """
    :param column:
    :return:y coordinate of the bottom of the column
    """
    if 355 + 18 * board[column].count("x") + 55 * (len(board[column]) - board[column].count("x") - 1) < 782:
        return 355 + 18 * board[column].count("x") + 55 * (len(board[column]) - board[column].count("x") - 1)
    else:
        return 782
