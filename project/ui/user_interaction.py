# name length check
def is_name_valid(name):
    if len(name) < 3:
        return None
    return name

# board size check
def is_board_size_valid(board_size):
    if board_size < 1 or board_size >= 26:
        return None
    return board_size

# number of mines check
def is_number_of_mines_valid(board_size, number_of_mines):
    if number_of_mines < 1 or number_of_mines > ((board_size * board_size) / 2):
        return None
    return number_of_mines

def register_user (name, board_size, number_of_mines):
    name = str(input("Hello, what's your name?"))
    name = is_name_valid(name)
    if name is not None:

        board_size = int(input(f" please choose board size, {name}"))
        board_size = is_board_size_valid(board_size)

        if board_size is not None:
            number_of_mines = int(input(f"for board size {board_size}, choose number of mines to allocate, {name}"))
            number_of_mines = is_number_of_mines_valid(board_size, number_of_mines)

            if number_of_mines is None:
                print(f"{name}, you have entered illegal number of mines")
        else:
            print(f"{name}, you have entered illegal board size")

    else:
        print("Your name is too short")

    return name, board_size, number_of_mines





#//////////////////////////////////////////////////////////////////////////////////////////////////////////







