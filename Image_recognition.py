import pyautogui
import time

global board, deck, position_deck, final


def what_card(n) -> int:
    """
    :param n: photo
    :return: integer describing the suit
    """
    if pyautogui.locate('A Red.png', n, confidence=0.8):
        return 1
    elif pyautogui.locate('2 Red.png', n, confidence=0.9):
        return 2
    elif pyautogui.locate('K Red.png', n, confidence=0.8):
        return 13
    elif pyautogui.locate('Q Red.png', n, confidence=0.9):
        return 12
    elif pyautogui.locate('10 Red.png', n, confidence=0.9):
        return 10
    elif pyautogui.locate('3 Red.png', n, confidence=0.9):
        return 3
    elif pyautogui.locate('4 Red.png', n, confidence=0.9):
        return 4
    elif pyautogui.locate('5 Red.png', n, confidence=0.8):
        return 5
    elif pyautogui.locate('6 Red.png', n, confidence=0.8):
        return 6
    elif pyautogui.locate('7 Red.png', n, confidence=0.9):
        return 7
    elif pyautogui.locate('8 Red.png', n, confidence=0.8):
        return 8
    elif pyautogui.locate('9 Red.png', n, confidence=0.8):
        return 9
    elif pyautogui.locate('J Red.png', n, confidence=0.9):
        return 11
    elif pyautogui.locate('J Black.png', n, confidence=0.8):
        return 11
    elif pyautogui.locate('A Black.png', n, confidence=0.9):
        return 1
    elif pyautogui.locate('2 Black.png', n, confidence=0.9):
        return 2
    elif pyautogui.locate('3 Black.png', n, confidence=0.9):
        return 3
    elif pyautogui.locate('4 Black.png', n, confidence=0.9):
        return 4
    elif pyautogui.locate('5 Black.png', n, confidence=0.9):
        return 5
    elif pyautogui.locate('6 Black.png', n, confidence=0.9):
        return 6
    elif pyautogui.locate('7 Black.png', n, confidence=0.9):
        return 7
    elif pyautogui.locate('8 Black.png', n, confidence=0.9):
        return 8
    elif pyautogui.locate('9 Black.png', n, confidence=0.9):
        return 9
    elif pyautogui.locate('10 Black.png', n, confidence=0.8):
        return 10
    elif pyautogui.locate('Q Black.png', n, confidence=0.9):
        return 12
    elif pyautogui.locate('K Black.png', n, confidence=0.9):
        return 13
    else:
        return 0


def what_suit(n) -> int:
    """
    :param n: photo
    :return: integer describing the suit
    """
    if pyautogui.locate('__Clubs.png', n, confidence=0.9):
        return 2
    elif pyautogui.locate('__Spades.png', n, confidence=0.8):
        return 0
    elif pyautogui.locate('__Hearts.png', n, confidence=0.8):
        return 1
    elif pyautogui.locate('__Diamonds.png', n, confidence=0.8):
        return 3


def photo_def_card(i):
    board[i].pop()
    screenshot = pyautogui.screenshot(region=(386 + round(169.6 * i), 345 + board[i].count("x") * 18, 29, 47))
    x = what_suit(screenshot)
    while x == None:
        time.sleep(0.1)
        screenshot = pyautogui.screenshot(region=(386 + round(169.6 * i), 345 + board[i].count("x") * 18, 29, 47))
        x = what_suit(screenshot)
    board[i].append([what_card(screenshot), x])
