name = str(input("Hello, what's your name?"))

# name length check
if len(name) < 3:
    print("Your name is too short")
    name = None
else:
    try:
        board_size = int(input(f"{name}, please choose board size (between 1 and 25): "))

        # board size check
        if board_size < 1 or board_size >= 26:
            print(f"{name}, you have entered illegal board size")
            board_size = None
        else:
            try:
                number_of_mines = int(
                    input(f"{name}, for board size {board_size}, choose number of mines to allocate: "))

                # number of mines check
                if number_of_mines < 1 or number_of_mines > (board_size * board_size) / 2:
                    print(f"{name}, you have entered illegal number of mines")
                    number_of_mines = None
                else:
                    print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}, ENJOY!")
            except ValueError:
                print(f"{name}, you have entered illegal number of mines")
                number_of_mines = None

    except ValueError:
        print(f"{name}, you have entered illegal board size")
        board_size = None
