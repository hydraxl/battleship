class Player:
    # Place ships on the board
    def place_ships(board, shipset):
        for i in range(len(shipset)):
            location = (0, i, board.HORIZONTAL)
            board.place_ship(shipset[i], *location)
    
    # Choose a point to attack
    def attack(board):
        return (0, 0)