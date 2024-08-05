
def parse_cmd(command):
    parse_cmd = command.split(" ")
    input_command = parse_cmd[0]
    parametrs = parse_cmd[1]
    split_parametrs = [parametrs[0]], [ord(parametrs[1]) - ord("A") + 1]
    return parse_cmd, split_parametrs








