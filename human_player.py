from player import Player
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
                orientation = input("orientation (vertical/horizontal): ").lower()
                if orientation == "vertical":
                    orientation = board.VERTICAL
                elif orientation == "horizontal":
                    orientation = board.HORIZONTAL
                location = (x, y, orientation)
                valid_input = board.place_ship(ship, *location)
                if not valid_input:
                    print("I'm sorry, your ship cannot be placed there")

    # Asks a human player to attack
    def attack(self, board):
        is_valid = False
        while not is_valid:
            print("Where would you like to attack?")
            x = int(input("x: "))
            y = int(input("y: "))
            pos = (x, y)
            is_valid = board.validate_attack(*pos)
            if not is_valid:
                print("You cannot attack a location you've already attacked.")
        
        return pos
        