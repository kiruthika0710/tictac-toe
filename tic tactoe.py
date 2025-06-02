def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(space in ['X', 'O'] for space in board)

def play_game():
    board = [str(i+1) for i in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a spot (1-9): ")
        
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Try again.")
            continue

        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("Spot taken. Try another one.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
