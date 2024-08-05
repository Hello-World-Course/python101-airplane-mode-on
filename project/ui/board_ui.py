
def parse_cmd(command):
    parse_cmd = command.split(" ")
    input_command = parse_cmd[0]
    parametrs = parse_cmd[1]
    split_parametrs = [parametrs[0]], [ord(parametrs[1]) - ord("A") + 1]
    return parse_cmd, split_parametrs





def is_on_board(x, y, board):
    if x <= 0 or x > len(board) or 0 >= y or y > len(board):
        return False
    return True

def safe_set_value(x, y, value, board):
    if is_on_board(x, y, board) is True:
        board[x - 1][y - 1] = value
        return True
    return False






