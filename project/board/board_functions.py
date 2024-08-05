

def is_on_board(x, y, board):
    if x <= 0 or x > len(board) or 0 >= y or y > len(board):
        return False
    return True

def safe_set_value(x, y, value, board):
    if is_on_board(x, y, board) is True:
        board[x - 1][y - 1] = value
        return True
    return False