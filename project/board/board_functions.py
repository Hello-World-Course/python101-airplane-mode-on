

def is_on_board(x, y, board):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False
    return True

def safe_set_value(x, y, value, board):
    if is_on_board(x, y, board) is True:
        board[x][y] = value
        return True
    return False