from human_player import *
from play_game import *
from test_strategy import *

p1 = HumanPlayer()
p2 = HumanPlayer()
#play_game(p1, p2)

result = test_strategy(p1.place_ships, p2.attack)
print(f"Attack strategy took {result} attacks to defeat ship strategy")