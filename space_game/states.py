from enum import Enum


class GameState(str, Enum):
    INTRO = "intro"
    MENU = "menu"
    ACT_ONE = "akt1"
    ENDING = "ending"
