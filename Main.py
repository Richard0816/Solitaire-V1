import operator
import time
import numpy as np
import pyautogui
from typing import Optional

from Image_recognition import what_card, what_suit, photo_def_card
from Movement_interface import move, click_deck
from Logic import next_move

global board, deck, position_deck, final
board = [[],
         ["x"],
         ["x", "x"],
         ["x", "x", "x"],
         ["x", "x", "x", "x"],
         ["x", "x", "x", "x", "x"],
         ["x", "x", "x", "x", "x", "x"]]
deck = []
position_deck = 0
final = [0, 0, 0, 0]

# starts at (left=385, top=342)
# each blank card is 18 pixels down
# shown cards is 55 pixels down
# left of each card: 385, 554, 723, 892, 1061, 1230, 1399


# Cards are assigned to numbers J = 11, Q = 12, K = 13
# Spades: 0
# Hearts: 1
# Clubs: 2
# Diamonds: 3

# red: odd
# black: even

def first_define():
    # define the board
    for i in range(7):
        photo_def_card(i)

    # define the deck
    deck.append([0, 0])
    for i in range(24):
        if i == 0:
            pyautogui.click(449, 195)
            time.sleep(0.2)
            screenshot = pyautogui.screenshot(region=(556, 113, 29, 47))
            deck.append([what_card(screenshot), what_suit(screenshot)])
        elif i == 1:
            pyautogui.click(449, 195)
            time.sleep(0.2)
            screenshot = pyautogui.screenshot(region=(584, 113, 29, 47))
            deck.append([what_card(screenshot), what_suit(screenshot)])
        else:
            pyautogui.click(449, 195)
            time.sleep(0.2)
            screenshot = pyautogui.screenshot(region=(612, 113, 29, 47))
            deck.append([what_card(screenshot), what_suit(screenshot)])
    pyautogui.click(449, 195)


first_define()
time.sleep(0.8)
