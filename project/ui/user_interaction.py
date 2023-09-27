name = "None"
name = input("Hello, whats your name?")

if len(name) < 3:
    name = "None"
    print("Your name is too short")

else:
    board_size = "None"
    board_size = int(input(name + ", please choose board size:"))

    if board_size <= 0 or board_size >= 26:
        board_size = "None"
        print(name, " you entered illegal board size")
    else:
        board_size_str = str(board_size)
        number_of_mines = "None"
        number_of_mines = int(input(name + ", for board size " + board_size_str + ", choose number of mines to allocate:"))

        if number_of_mines <= 0 or number_of_mines > board_size / 2:
            number_of_mines = "None"
            print(name, "you entered illegal number of mines")
        else:
            number_of_mines_str = str(number_of_mines)
            print(name + ", the board size is: " + board_size_str + ", number of mines is: " + number_of_mines_str + ", ENJOY!")
