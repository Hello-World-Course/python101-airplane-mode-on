def is_name_valid(name):
    return len(name) >= 3

# board size check
def is_board_size_valid(board_size):
    return 1 <= board_size < 26

# number of mines check
def is_number_of_mines_valid(board_size, number_of_mines):
    return  1 <= number_of_mines <= ((board_size * board_size) / 2)

def register_user (name, board_size, number_of_mines):
    name = str(input("Hello, what's your name?"))
    if not is_name_valid(name):
        print("Your name is too short")
        return (None, None, None)


    board_size = int(input(f"please choose board size, {name}"))
    if not is_board_size_valid(board_size):
        print(f"{name}, you have entered illegal board size")
        return (None, None, None)

    number_of_mines = int(input(f"for board size {board_size}, choose number of mines to allocate, {name}"))
    if not is_number_of_mines_valid(board_size, number_of_mines):
        print(f"{name}, you have entered illegal number of mines")
        return (None, None, None)

    return name, board_size, number_of_mines





#//////////////////////////////////////////////////////////////////////////////////////////////////////////







