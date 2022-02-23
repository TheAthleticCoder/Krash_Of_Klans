# We create game constants here

import colorama
from colorama import Fore, Back, Style,init

#Time
FPS = 90
T = 1/FPS

#Board dimensions
ROWS_V = 20
COLS_V = 20

#King position
X_KING = 1
Y_KING = 1
HP_KING = 100

#Wall class
ROWS_W = 1
COLS_W = 1
HP_WALL = 10
WALLS = [[10,10,10],[10,11,10]]

#Town Hall
X_TH = 12
Y_TH = 12
HP_TH = 10
CHAR_TH = '| T |'
TH_BLOCKS = [[X_TH,Y_TH],[X_TH,Y_TH+1],[X_TH,Y_TH+2],[X_TH,Y_TH+3],[X_TH+1,Y_TH],[X_TH+1,Y_TH+1],[X_TH+1,Y_TH+2],[X_TH+1,Y_TH+3],
[X_TH+2,Y_TH],[X_TH+2,Y_TH+1],[X_TH+2,Y_TH+2],[X_TH+2,Y_TH+3]]

#Spawn locations
X_SPAWN = [ROWS_V-2,1,ROWS_V-2]
Y_SPAWN = [2,COLS_V-2,COLS_V-2]

#clock
clock = 0