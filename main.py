def print_board(board):
    print("   0   1   2")
    for idx, row in enumerate(board):
        print(f"{idx}  " + " | ".join(row))
        if idx < 2:
            print("  ---|---|---")

def check_winner(board, player):
    # 行のチェック
    for row in board:
        if all([spot == player for spot in row]):
            return True
    # 列のチェック
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # 斜めのチェック
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"{current_player}の番です。行と列を0から2の範囲で選んでください。")

        try:
            row = int(input("行: "))
            col = int(input("列: "))
            if board[row][col] != " ":
                print("そのマスは既に埋まっています。別のマスを選んでください。")
                continue
        except (ValueError, IndexError):
            print("無効な入力です。0から2の範囲で正しい値を入力してください。")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player}の勝利です！")
            break

        if all([spot != " " for row in board for spot in row]):
            print_board(board)
            print("引き分けです！")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
