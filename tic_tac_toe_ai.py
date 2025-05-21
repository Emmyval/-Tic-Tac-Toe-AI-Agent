import math
import random

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Define game board
def create_board():
    return [EMPTY for _ in range(9)]

# Print board
def print_board(board):
    for i in range(3):
        print("|".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-----")

# Check for winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check for tie
def is_tie(board):
    return all(cell != EMPTY for cell in board)

# Get available moves
def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]

# Minimax algorithm for AI move decision
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, HUMAN):
        return -1
    elif is_tie(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Best move for AI
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'.")
    current_player = HUMAN if random.choice([True, False]) else AI

    while True:
        print_board(board)

        if check_winner(board, HUMAN):
            print("🎉 You win!")
            break
        elif check_winner(board, AI):
            print("🤖 AI wins!")
            break
        elif is_tie(board):
            print("😐 It's a tie!")
            break

        if current_player == HUMAN:
            move = int(input("Enter your move (0-8): "))
            if board[move] == EMPTY:
                board[move] = HUMAN
                current_player = AI
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is thinking...")
            move = get_best_move(board)
            board[move] = AI
            current_player = HUMAN

# Call the main game loop
if __name__ == "__main__":
    play_game()
