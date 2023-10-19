# Display your ships 
def display_ship_board(board):
    for y in range(board.size):
        line = ""
        for x in range(board.size):
            line += board.ship_board[x][y] + " "
        print(line)

# Display your attacks
def display_attack_board(board):
    # print attack board
    for y in range(board.size):
        line = ""
        for x in range(board.size):
            line += board.attack_board[x][y] + " "
        print(line)

# Display result of attack
def display_result(did_hit):
    if did_hit:
        print("Hit!")
    else:
        print("Miss!")
    print()