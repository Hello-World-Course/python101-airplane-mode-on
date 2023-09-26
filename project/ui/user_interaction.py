name = input ("Hello, whats your name?")

board_size = int (input (name + ", please choose board size:"))

board_size_str = str(board_size)

number_of_mines = int (input (name + ", for board size " + board_size_str + ", choose number of mines to allocate:"))

number_of_mines_str = str(number_of_mines)

print(name + ", the board size is: " + board_size_str + ", number of mines is: " + number_of_mines_str + ", ENJOY!")

