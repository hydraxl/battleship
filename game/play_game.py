from game.game_board import GameBoard
import interface.text_ui as text_ui

def play_game(p1, p2, size=GameBoard.DEFAULT_SIZE, shipset=GameBoard.DEFAULT_SHIPS):
    # Set up boards
    p1_board = GameBoard(size)
    p2_board = GameBoard(size)

    # Both players place their ships
    p1.place_ships(p1_board, shipset)
    p2.place_ships(p2_board, shipset)

    # Both players attack until someone wins
    winner = None
    while True:
        # Repeat until attack is valid
        attack_result = 2
        while attack_result == 2:
            # p1 attacks p2
            text_ui.display_attack_board(p1_board)
            attack_location = p1.attack(p1_board)
            attack_result = p1_board.attack(p2_board, *attack_location)
        text_ui.display_result(attack_result)
        
        # Check if p1 won
        if p2_board.has_lost():
            winner = 1
            break
        
        # Repeat until attack is valid
        attack_result = 2
        while attack_result == 2:
            # p2 attacks p1
            text_ui.display_attack_board(p2_board)
            attack_location = p2.attack(p2_board)
            attack_result = p2_board.attack(p1_board, *attack_location)
        text_ui.display_result(attack_result)
        
        # Check if p2 won
        if p1_board.has_lost():
            winner = 2
            break

    # Congratulate the winner    
    if winner == 1:
        print("Congrats to player 1!")
    elif winner == 2:
        print("Congrats to player 2!")
    else:
        print("Something went wrong.")

