# Tic Tac Toe game

# Hold tic tac toe layout
tic_tac_toe = [["    ", " A ", " B ", " C "],
               ["1:  ", "   ", "   ", "   "],
               ["2:  ", "   ", "   ", "   "],
               ["3:  ", "   ", "   ", "   "]]


# Different players
players = [1, 2]

def print_tic_tac_toe():
    """
    :return: string representing the expected game layout
    """
    tac_toe_print = ""
    for line in tic_tac_toe:
        # add column separators
        tac_toe_print += ' | '.join(line)
        tac_toe_print += '\n'
        # add row seperator
        if line != tic_tac_toe[-1]:
            tac_toe_print += " _ _ _ _ _ _ _ _ _ _ _ \n"

    return tac_toe_print


def place_symbol(player, coordinates):
    """

    :param player: current player (1 or 2)
    :param coordinates: user coordinates inputted
    :return: True if coordinate not occupied already
    """

    global tic_tac_toe

    if player == 1:
        symbol = ' X '
    else:
        symbol = ' O '

    # Get nested list index coordinates
    x_axis = int(coordinates[1])
    # dictionary map user input to index
    y_axis_translation = {"A": 1, "B": 2, "C": 3}
    y_axis = y_axis_translation[coordinates[0].strip().upper()]

    # check if coordinates already contain player symbol
    if tic_tac_toe[x_axis][y_axis] == " X " or tic_tac_toe[x_axis][y_axis] == " O ":
        return False

    # if available
    else:
        tic_tac_toe[x_axis][y_axis] = symbol
        return True


def check_won():
    """
    For each symbol - checks if won horizontally, vertically,
    or diagonally
    - using set() to check contains only 1 symbol
    """
    for symbol in [" X ", " O "]:

        # Horizontally
        # - not include first row and column (coordinates)
        for line in tic_tac_toe[1:]:
            if set(line[1:]) == set([symbol]):
                return True

        # Vertically
        # - not include first row and column (coordinates)
        for column in range(len(tic_tac_toe) - 1):
            vertical = []
            for line in tic_tac_toe[1:]:
                vertical.append(line[column + 1])
            if set(vertical) == set([symbol]):
                return True

        # Diagonally
        main_diagonal = []  # top left to bottom right
        for i in range(len(tic_tac_toe) - 1):
            # + 1 to avoid first row and column (grid coordinates)
            main_diagonal.append(tic_tac_toe[i + 1][i + 1])

        counter_diagonal = []  # top right to bottom left
        for j in range(len(tic_tac_toe) - 1):
            # + 1 to avoid first row and column (grid coordinates)
            counter_diagonal.append(tic_tac_toe[j + 1][(len(tic_tac_toe) - 2) - j + 1])

        if set(main_diagonal) == set([symbol]) or set(counter_diagonal) == set([symbol]):
            return True

    return False


def check_draw():
    """
    checks if an unallocated square is present
    """
    for line in tic_tac_toe[1:]:
        for item in line:
            if item == "   ":
                return False
    return True


def switch_player(current_player):
    """
    Switches player pointer to other player
    """
    for player in players:
        if player != current_player:
            current_player = player
            return current_player


# Greetings and initial Rules of the game
print("WELCOME TO TIC TAC TOE!\n\n"
      "Player 1 places 'X'\nand Player 2 places 'O'\n"
      "\nSpecify the placement of your symbol using the Letter "
      "and number coordinates as shown below")

print("Specify the LETTER FIRST then the NUMBER\nFor example: 'A3")
print(print_tic_tac_toe())


# While loop to keep game running
player = players[0]
game_continue = True
while game_continue:

    # Get Input
    user_input = input(f"\nPlayer {player} to move:\n").upper()

    # If input is valid
    if user_input[0] in ["A", "B", "C"] and user_input[1] in ["1", "2", "3"]:

        # if coordinate is available - place symbol in coordinate
        if place_symbol(player, user_input):
            print(print_tic_tac_toe())

            # if player has won
            if check_won():
                print(f"GAME OVER!\nPlayer {player} has won the Game!")
                print(print_tic_tac_toe())
                player_continue = input("Continue (Y or N)?").lower()
                if player_continue == 'n':
                    game_continue = False

            # if it is a draw
            elif check_draw():
                print(f"GAME OVER!\nNeither player has won. . .!\n")
                print(print_tic_tac_toe())
                player_continue = input("Continue (Y or N)?").lower()
                if player_continue == 'n':
                    game_continue = False

            # otherwise next players turn
            else:
                player = switch_player(player)

        # Coordinate unavailable
        else:
            print("Coordinate already taken")

    # Non valid input
    else:
        print("Input was incorrect - Specify the LETTER FIRST then the NUMBER\nFor example: 'A3")
