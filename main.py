from ai.human import *
from game.play_game import *
from game.test_strategy import *

p1 = Human()
p2 = Human()
#play_game(p1, p2)

result = test_strategy(p1.place_ships, p2.attack)
print(f"Attack strategy took {result} attacks to defeat ship strategy")