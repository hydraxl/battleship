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
    def place_ship(self, length, x, y, orientation) -> bool:
        # positions of each point on the ship
        new_x = x
        new_y = y
        
        # Determine if ship placement is valid
        # Must be entirely finished before any placement begins
        for i in range(length):
            if orientation == self.HORIZONTAL:
                new_x = x + i
            elif orientation == self.VERTICAL:
                new_y = y + i

            # Ship is invalid if orientation is not HORIZONTAL or VERTICAL
            else:
                return False
            
            # Ship is invalid if it intersects another ship or exits the board
            if new_x >= self.size:
                print("ERROR")
                return False
            if new_y >= self.size:
                print("ERROR")
                return False
            if self.ship_board[new_x][new_y] is self.SHIP:
                print("ERROR")
                return False
        
        # Place ship
        for i in range(length):
            if orientation is self.HORIZONTAL:
                new_x = x + i
            elif orientation is self.VERTICAL:
                new_y = y + i
            
            self.ship_board[new_x][new_y] = self.SHIP
        
        return True

    # Returns true if the ship_board contains no ships
    def has_lost(self) -> bool:
        for row in self.ship_board:
            if self.SHIP in row:
                return False
        
        return True

    # Returns 0 if miss, 1 if hit, -1 if invalid
    # Attack is invalid if position has previously been attacked
    def receive_attack(self, x, y) -> int:
        location = self.ship_board[x][y]
        
        if location is self.WATER:
            self.ship_board[x][y] = self.MISS
            return 0
        elif location is self.SHIP:
            self.ship_board[x][y] = self.HIT
            return 1
        else:
            return -1
            
    # Checks if an attack location is valid
    # Returns false if the position has already been attacked
    def validate_attack(self, x, y) -> bool:
        location = self.attack_board[x][y]
        if location is self.WATER:
            return True
        else:
            return False

    # Returns 0 if miss, 1 if hit, -1 if invalid
    # Attack is invalid if position has previously been attacked
    def attack(self, board, x, y) -> int:
        success = board.receive_attack(x, y)
        if success == 0:
            self.attack_board[x][y] = self.MISS
        elif success == 1:
            self.attack_board[x][y] = self.HIT
        
        return success

