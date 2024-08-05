
def parse_cmd(command):
    parse_cmd = command.split(" ")
    input_command = parse_cmd[0]
    if len(parse_cmd) > 1:
        parameters = parse_cmd[1:]
        if len(parameters) == 1 and len(parameters[0]) == 2:
            split_parameters = [parameters[0][0]], [ord(parameters[0][1]) - ord("A") + 1]
        else:
            split_parameters = parameters
    else:
        split_parameters = []
    return input_command, parameters

command = '"test", [\'1\', \'23\', \'4\', \'5\', \'67\', \'8\']'


print(parse_cmd(command))
