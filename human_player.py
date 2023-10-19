from player import Player
from point import Point
from game_board import VERTICAL, HORIZONTAL
import ui

class HumanPlayer(Player):
    # Asks a human player to place ships
    def place_ships(self, board, shipset):
        for ship in shipset:
            ui.display_ship_board(board)
            valid_input = False
            while not valid_input:
                print(f"Your next ship is {ship} squares.")
                print("Where would you like to place it?")
                x = int(input("x: "))
                y = int(input("y: "))
                position = Point(x, y)
                orientation = input("orientation (vertical/horizontal): ").lower()
                if orientation == "vertical":
                    orientation = VERTICAL
                elif orientation == "horizontal":
                    orientation = HORIZONTAL
                
                valid_input = board.place_ship(ship, position, orientation)
                if not valid_input:
                    print("I'm sorry, your ship cannot be placed there")

    # Asks a human player to attack
    def attack(self, board) -> Point:
        is_valid = False
        position = None
        while not is_valid:
            print("Where would you like to attack?")
            x = int(input("x: "))
            y = int(input("y: "))
            position = Point(x, y)
            is_valid = board.validate_attack(position)
            if not is_valid:
                print("You cannot attack a location you've already attacked.")
        
        return position
        