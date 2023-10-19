from game.game_board import GameBoard

def test_strategy(place_ships, attack, size=GameBoard.DEFAULT_SIZE, shipset=GameBoard.DEFAULT_SHIPS) -> int:
    # Set up board using place_ships strategy
    board = GameBoard(size)
    place_ships(board, shipset)

    # Run attack strategy and count number of attacks it takes to win
    num_attacks = 0
    game_ended = False
    while not game_ended:
        # Increment num_attacks
        num_attacks += 1

        # Repeat until attack is valid
        attack_result = 2
        while attack_result == 2:
            # p1 attacks p2
            attack_location = attack(board)
            attack_result = board.attack(board, *attack_location)
        
        # Check if p1 won
        if board.has_lost():
            game_ended = True
    
    return num_attacks
