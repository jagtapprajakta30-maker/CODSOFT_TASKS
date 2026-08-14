import math


def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if all(cell != " " for cell in board):
        return "Draw"

    return None


def minimax(board, depth, is_maximizing):
    result = check_winner(board)

    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():

    board = [" "] * 9

    print("================================")
    print("       TIC-TAC-TOE AI")
    print("================================")

    print("You are X")
    print("AI is O")

    print("\nBoard positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:

        # -------------------------
        # HUMAN MOVE
        # -------------------------

        try:
            position = int(input("\nEnter your position (1-9): "))

        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if position < 1 or position > 9:
            print("Please enter a number between 1 and 9.")
            continue

        position -= 1

        if board[position] != " ":
            print("That position is already occupied.")
            continue

        board[position] = "X"

        print_board(board)

        result = check_winner(board)

        if result == "X":
            print("🎉 Congratulations! You win!")
            break

        if result == "Draw":
            print("It's a draw!")
            break

        # -------------------------
        # AI MOVE
        # -------------------------

        print("🤖 AI is thinking...")

        ai_position = best_move(board)

        board[ai_position] = "O"

        print(f"AI selected position: {ai_position + 1}")

        print_board(board)

        result = check_winner(board)

        if result == "O":
            print("🤖 AI wins!")
            break

        if result == "Draw":
            print("It's a draw!")
            break


play_game()