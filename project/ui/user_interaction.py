def is_name_valid(player_name):
    if len(player_name) > 2:
        return True
    else:
        return False

def is_board_size_valid(board_size):
    if 0 < board_size <= 26:
        return True
    else:
        return False

def is_number_of_mines_valid(board_size, number_of_mines):
    if 0 < number_of_mines <= ((board_size ** 2) / 2):
        return True
    else:
        return False

def register_user():
    player_name = input("Hello, what's your name?")
    if not is_name_valid(player_name):
        print("Your name is too short")
        player_name = None
        return None, None, None


    board_size = int(input(player_name + ", please choose board size:"))
    if not is_board_size_valid(board_size):
        print(player_name + ", you have entered illegal board size")
        board_size = None
        return None, None, None


    number_of_mines = int(input(player_name + ", for board size " + str(board_size) + ", choose number of mines to allocate:"))
    if not is_number_of_mines_valid((board_size), (number_of_mines)):
        print(player_name + ", you have entered illegal number of mines")
        number_of_mines = None
        return None, None, None


    return player_name, board_size, number_of_mines


