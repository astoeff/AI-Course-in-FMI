from constants import PLAYER_IS_FIRST_VALUE, COMPUTER_IS_FIRST_VALUE


def read_input_from_console():
    inputted_value = None
    is_inputted_value_valid = inputted_value == PLAYER_IS_FIRST_VALUE or inputted_value == COMPUTER_IS_FIRST_VALUE
    while not is_inputted_value_valid:
        inputted_value = str(input('Enter 1 to be first, 0 otherwize: ' ))
        is_inputted_value_valid = inputted_value == PLAYER_IS_FIRST_VALUE or inputted_value == COMPUTER_IS_FIRST_VALUE
    return inputted_value

def is_player_first(inputted_value):
    return inputted_value == PLAYER_IS_FIRST_VALUE

def main():
    inputted_value = read_input_from_console()
    print(is_player_first(inputted_value))

if __name__ == '__main__':
    main()