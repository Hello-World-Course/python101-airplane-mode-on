# name length check
def is_name_valid(name):
    if len(name) < 3:
        return False
    return True

# board size check
def is_board_size_valid(board_size):
    if board_size < 1 or board_size >= 26:
        return False
        return True

# number of mines check
def is_number_of_mines_valid(board_size, number_of_mines):
    if number_of_mines < 1 or number_of_mines > ((board_size * board_size) / 2):
        return False
    return True

def register_user (name, board_size, number_of_mines):
    name = str(input("Hello, what's your name?"))
    name = is_name_valid(name)
    if is_name_valid(True):

        board_size = int(input(f" please choose board size, {name}"))
        board_size = is_board_size_valid(board_size)

        if is_board_size_valid(True):
            number_of_mines = int(input(f"for board size {board_size}, choose number of mines to allocate, {name}"))
            number_of_mines = is_number_of_mines_valid(board_size, number_of_mines)

            if is_number_of_mines_valid(False):
                print(f"{name}, you have entered illegal number of mines")
                name, board_size, number_of_mines = None

        else:
            print(f"{name}, you have entered illegal board size")
            name, board_size, number_of_mines = None


    else:
        print("Your name is too short")
        name, board_size, number_of_mines = None


    return name, board_size, number_of_mines





#//////////////////////////////////////////////////////////////////////////////////////////////////////////







