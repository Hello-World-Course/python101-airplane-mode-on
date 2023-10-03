def is_name_valid(name):
    if len(name) > 2:
        return True



def is_board_size_valid(board_size):
    if 0 < board_size <= 26:
        return True




def is_number_of_mines_valid(board_size, number_of_mines):
    if 0 < number_of_mines <= board_size / 2:
        return True




def register_user():
    player_name = input("Hello, what's your name?")
    if not is_name_valid(player_name):
        print("Your name is too short")
        player_name = None


    board_size = input(player_name + ", please choose board size:")
    if not is_board_size_valid(int(board_size)):
        print(player_name, "you entered illegal board size")
        board_size = None

    number_of_mines = input(player_name + ", for board size " + board_size + ", choose number of mines to allocate:")
    if not is_number_of_mines_valid(int(board_size), int(number_of_mines)):
        print(player_name, "you entered illegal number of mines")
        number_of_mines = None

    return player_name, int(board_size), int(number_of_mines)

player_name, board_size, mines_num = register_user()
if player_name:
    print(f"Registered Player: {player_name}, Board Size: {board_size}, Number of Mines: {mines_num}")