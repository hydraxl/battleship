class GameBoard:
    # Types of squares
    WATER = "w"
    HIT = "h"
    MISS = "m"
    SHIP = "s"

    # Types of orientations
    VERTICAL = "v"
    HORIZONTAL = "h"

    # Default game settings
    DEFAULT_SHIPS = [3, 4, 4, 5]
    DEFAULT_SIZE = 10

    def __init__(self, size=DEFAULT_SIZE):
        self.size = size
        self.ship_board = [[self.WATER for i in range(size)] for j in range(size)]
        self.attack_board = [[self.WATER for i in range(size)] for j in range(size)]

    # Returns True if ship placement is valid, False if ship is invalid
    def place_ship(self, length, position, orientation) -> bool:
        # Determine if ship placement is valid
        for i in range(length):
            x = position["x"]
            y = position["y"]
            if orientation == self.HORIZONTAL:
                x += i
            elif orientation == self.VERTICAL:
                y += i

            # Ship is invalid if orientation is not HORIZONTAL or VERTICAL
            else:
                return False
            
            # Ship is invalid if it intersects another ship or exits the board
            if x >= self.size:
                print("ERROR")
                return False
            if y >= self.size:
                print("ERROR")
                return False
            if self.ship_board[x][y] is self.SHIP:
                print("ERROR")
                return False
        
        # Place ship
        for i in range(length):
            x = position["x"]
            y = position["y"]
            if orientation is self.HORIZONTAL:
                x += i
            elif orientation is self.VERTICAL:
                y += i
            
            self.ship_board[x][y] = self.SHIP
        
        return True

    # Returns true if the ship_board contains no ships
    def has_lost(self) -> bool:
        for row in self.ship_board:
            if self.SHIP in row:
                return False
        
        return True

    # Returns 0 if miss, 1 if hit, -1 if invalid
    # Attack is invalid if position has previously been attacked
    def receive_attack(self, position) -> int:
        location = self.ship_board[position["x"]][position["y"]]
        
        if location is self.WATER:
            self.ship_board[position["x"]][position["y"]] = self.MISS
            return 0
        elif location is self.SHIP:
            self.ship_board[position["x"]][position["y"]] = self.HIT
            return 1
        else:
            return -1
            
    # Checks if an attack location is valid
    # Returns false if the position has already been attacked

    def validate_attack(self, position) -> bool:
        location = self.attack_board[position["x"]][position["y"]]
        if location is self.WATER:
            return True
        else:
            return False

    # Returns 0 if miss, 1 if hit, -1 if invalid
    # Attack is invalid if position has previously been attacked
    def attack(self, board, position) -> int:
        success = board.receive_attack(position)
        if success == 0:
            self.attack_board[position["x"]][position["y"]] = self.MISS
        elif success == 1:
            self.attack_board[position["x"]][position["y"]] = self.HIT
        
        return success

