from point import Point
    
class Player:
    # Place ships on the board
    def place_ships(board, shipset):
        for i in range(len(shipset)):
            location = Point(0, i)
            board.place_ship(shipset[i], location, board.HORIZONTAL)
    
    # Choose a point to attack
    def attack(board) -> Point:
        return Point(0, 0)