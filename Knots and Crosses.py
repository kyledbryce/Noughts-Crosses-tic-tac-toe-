def print_grid_reference():
    print("     |     |     ")
    print("  7  |  8  |  9  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  4  |  5  |  6  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  1  |  2  |  3  ")
    print("     |     |     ")
    print("\n\n")


def horizontal_line():
    print("-----------------")


def an_empty_row():
    print("     |     |     ")
    print("     |     |     ")
    print("     |     |     ")


def O__():
    print(" OOO |     |     ")
    print("O   O|     |     ")
    print(" OOO |     |     ")


def OO_():
    print(" OOO | OOO |     ")
    print("O   O|O   O|     ")
    print(" OOO | OOO |     ")


def O_O():
    print(" OOO |     | OOO ")
    print("O   O|     |O   O")
    print(" OOO |     | OOO ")


def OOO():
    print(" OOO | OOO | OOO ")
    print("O   O|O   O|O   O")
    print(" OOO | OOO | OOO ")


def OOX():
    print(" OOO | OOO | \ / ")
    print("O   O|O   O|  X  ")
    print(" OOO | OOO | / \ ")


def OXO():
    print(" OOO | \ / | OOO ")
    print("O   O|  X  |O   O")
    print(" OOO | / \ | OOO ")


def O_X():
    print(" OOO |     | \ / ")
    print("O   O|     |  X  ")
    print(" OOO |     | / \ ")


def OX_():
    print(" OOO | \ / |     ")
    print("O   O|  X  |     ")
    print(" OOO | / \ |     ")


def OXX():
    print(" OOO | \ / | \ / ")
    print("O   O|  X  |  X  ")
    print(" OOO | / \ | / \ ")


def X__():
    print(" \ / |     |     ")
    print("  X  |     |     ")
    print(" / \ |     |     ")


def XO_():
    print(" \ / | OOO |     ")
    print("  X  |O   O|     ")
    print(" / \ | OOO |     ")


def X_O():
    print(" \ / |     | OOO ")
    print("  X  |     |O   O")
    print(" / \ |     | OOO ")


def XOO():
    print(" \ / | OOO | OOO ")
    print("  X  |O   O|O   O")
    print(" / \ | OOO | OOO ")


def XOX():
    print(" \ / | OOO | \ / ")
    print("  X  |O   O|  X  ")
    print(" / \ | OOO | / \ ")


def XXO():
    print(" \ / | \ / | OOO ")
    print("  X  |  X  |O   O")
    print(" / \ | / \ | OOO ")


def X_X():
    print(" \ / |     | \ / ")
    print("  X  |     |  X  ")
    print(" / \ |     | / \ ")


def XX_():
    print(" \ / | \ / |     ")
    print("  X  |  X  |     ")
    print(" / \ | / \ |     ")


def XXX():
    print(" \ / | \ / | \ / ")
    print("  X  |  X  |  X  ")
    print(" / \ | / \ | / \ ")


def _O_():
    print("     | OOO |     ")
    print("     |O   O|     ")
    print("     | OOO |     ")


def __O():
    print("     |     | OOO ")
    print("     |     |O   O")
    print("     |     | OOO ")


def _OO():
    print("     | OOO | OOO ")
    print("     |O   O|O   O")
    print("     | OOO | OOO ")


def _OX():
    print("     | OOO | \ / ")
    print("     |O   O|  X  ")
    print("     | OOO | / \ ")


def _XO():
    print("     | \ / | OOO ")
    print("     |  X  |O   O")
    print("     | / \ | OOO ")


def __X():
    print("     |     | \ / ")
    print("     |     |  X  ")
    print("     |     | / \ ")


def _X_():
    print("     | \ / |     ")
    print("     |  X  |     ")
    print("     | / \ |     ")


def _XX():
    print("     | \ / | \ / ")
    print("     |  X  |  X  ")
    print("     | / \ | / \ ")


def print_bottom_row():

    o_position = top_row_o_position
    x_position = top_row_x_position

    if 1 in o_position and 2 in o_position and 3 in o_position:
        OOO()
    elif 1 in x_position and 2 in x_position and 3 in x_position:
        XXX()
    elif 1 not in (o_position or x_position) and 2 not in (o_position or x_position) and 3 not in (o_position or x_position):
        an_empty_row()
    elif 1 in o_position and 2 in o_position and 3 in x_position:
        OOX()
    elif 1 in o_position and 2 in o_position and 3 not in (x_position or o_position):
        OO_()
    elif 1 in o_position and 3 in o_position and 2 in x_position:
        OXO()
    elif 1 in o_position and 3 in o_position and 2 not in (x_position or o_position):
        O_O()
    elif 2 in o_position and 3 in o_position and 1 in x_position:
        XOO()
    elif 2 in o_position and 3 in o_position and 1 not in (x_position or o_position):
        _OO()
    elif 1 in o_position and 2 not in (x_position or o_position) and 3 not in (x_position or o_position):
        O__()
    elif 2 in o_position and 1 not in (x_position or o_position) and 3 not in (x_position or o_position):
        _O_()
    elif 3 in o_position and 1 not in (x_position or o_position) and 2 not in (x_position or o_position):
        __O()
    elif 1 in o_position and 2 in x_position and 3 in x_position:
        OXX()
    elif 2 in o_position and 1 in x_position and 3 in x_position:
        XOX()
    elif 3 in o_position and 1 in x_position and 2 in x_position:
        XXO()
    elif 1 in o_position and 2 in x_position and 3 not in (x_position or o_position):
        OX_()
    elif 2 in o_position and 1 in x_position and 3 not in (x_position or o_position):
        XO_()
    elif 3 in o_position and 1 in x_position and 2 not in (x_position or o_position):
        X_O()
    elif 1 in o_position and 3 in x_position and 2 not in (x_position or o_position):
        O_X()
    elif 2 in o_position and 3 in x_position and 1 not in (x_position or o_position):
        _OX()
    elif 3 in o_position and 2 in x_position and 1 not in (x_position or o_position):
        _XO()
    elif 1 in x_position and 2 not in (x_position or o_position) and 3 not in (x_position or o_position):
        X__()
    elif 2 in x_position and 1 not in (x_position or o_position) and 3 not in (x_position or o_position):
        _X_()
    elif 3 in x_position and 1 not in (x_position or o_position) and 2 not in (x_position or o_position):
        __X()
    elif 1 in x_position and 2 in x_position and 3 not in (x_position or o_position):
        XX_()
    elif 1 in x_position and 3 in x_position and 2 not in (x_position or o_position):
        X_X()
    else:
        _XX()


def print_middle_row():

    o_position = mid_row_o_position
    x_position = mid_row_x_position

    for i, number in enumerate(o_position):
        if number == 4:
            o_position[i] = 1
        elif number == 5:
            o_position[i] = 2
        elif number == 6:
            o_position[i] = 3

    for i, number in enumerate(x_position):
        if number == 4:
            x_position[i] = 1
        elif number == 5:
            x_position[i] = 2
        elif number == 6:
            x_position[i] = 3

    if 1 in o_position and 2 in o_position and 3 in o_position:
        OOO()
    elif 1 in x_position and 2 in x_position and 3 in x_position:
        XXX()
    elif 1 not in (o_position or x_position) and 2 not in (o_position or x_position) and 3 not in (o_position or x_position):
        an_empty_row()
    elif 1 in o_position and 2 in o_position and 3 in x_position:
        OOX()
    elif 1 in o_position and 2 in o_position and 3 not in (x_position or o_position):
        OO_()
    elif 1 in o_position and 3 in o_position and 2 in x_position:
        OXO()
    elif 1 in o_position and 3 in o_position and 2 not in (x_position or o_position):
        O_O()
    elif 2 in o_position and 3 in o_position and 1 in x_position:
        XOO()
    elif 2 in o_position and 3 in o_position and 1 not in (x_position or o_position):
        _OO()
    elif 1 in o_position and 2 not in (x_position or o_position) and 3 not in (x_position or o_position):
        O__()
    elif 2 in o_position and 1 not in (x_position or o_position) and 3 not in (x_position or o_position):
        _O_()
    elif 3 in o_position and 1 not in (x_position or o_position) and 2 not in (x_position or o_position):
        __O()
    elif 1 in o_position and 2 in x_position and 3 in x_position:
        OXX()
    elif 2 in o_position and 1 in x_position and 3 in x_position:
        XOX()
    elif 3 in o_position and 1 in x_position and 2 in x_position:
        XXO()
    elif 1 in o_position and 2 in x_position and 3 not in (x_position or o_position):
        OX_()
    elif 2 in o_position and 1 in x_position and 3 not in (x_position or o_position):
        XO_()
    elif 3 in o_position and 1 in x_position and 2 not in (x_position or o_position):
        X_O()
    elif 1 in o_position and 3 in x_position and 2 not in (x_position or o_position):
        O_X()
    elif 2 in o_position and 3 in x_position and 1 not in (x_position or o_position):
        _OX()
    elif 3 in o_position and 2 in x_position and 1 not in (x_position or o_position):
        _XO()
    elif 1 in x_position and 2 not in (x_position or o_position) and 3 not in (x_position or o_position):
        X__()
    elif 2 in x_position and 1 not in (x_position or o_position) and 3 not in (x_position or o_position):
        _X_()
    elif 3 in x_position and 1 not in (x_position or o_position) and 2 not in (x_position or o_position):
        __X()
    elif 1 in x_position and 2 in x_position and 3 not in (x_position or o_position):
        XX_()
    elif 1 in x_position and 3 in x_position and 2 not in (x_position or o_position):
        X_X()
    else:
        _XX()


def print_top_row():

    o_position = bottom_row_o_position
    x_position = bottom_row_x_position

    for i, number in enumerate(o_position):
        if number == 7:
            o_position[i] = 1
        elif number == 8:
            o_position[i] = 2
        elif number == 9:
            o_position[i] = 3

    print("")

    for i, number in enumerate(x_position):
        if number == 7:
            x_position[i] = 1
        elif number == 8:
            x_position[i] = 2
        elif number == 9:
            x_position[i] = 3

    if 1 in o_position and 2 in o_position and 3 in o_position:
        OOO()
    elif 1 in x_position and 2 in x_position and 3 in x_position:
        XXX()
    elif 1 not in (o_position or x_position) and 2 not in (o_position or x_position) and 3 not in (o_position or x_position):
        an_empty_row()
    elif 1 in o_position and 2 in o_position and 3 in x_position:
        OOX()
    elif 1 in o_position and 2 in o_position and 3 not in (x_position or o_position):
        OO_()
    elif 1 in o_position and 3 in o_position and 2 in x_position:
        OXO()
    elif 1 in o_position and 3 in o_position and 2 not in (x_position or o_position):
        O_O()
    elif 2 in o_position and 3 in o_position and 1 in x_position:
        XOO()
    elif 2 in o_position and 3 in o_position and 1 not in (x_position or o_position):
        _OO()
    elif 1 in o_position and 2 not in (x_position or o_position) and 3 not in (x_position or o_position):
        O__()
    elif 2 in o_position and 1 not in (x_position or o_position) and 3 not in (x_position or o_position):
        _O_()
    elif 3 in o_position and 1 not in (x_position or o_position) and 2 not in (x_position or o_position):
        __O()
    elif 1 in o_position and 2 in x_position and 3 in x_position:
        OXX()
    elif 2 in o_position and 1 in x_position and 3 in x_position:
        XOX()
    elif 3 in o_position and 1 in x_position and 2 in x_position:
        XXO()
    elif 1 in o_position and 2 in x_position and 3 not in (x_position or o_position):
        OX_()
    elif 2 in o_position and 1 in x_position and 3 not in (x_position or o_position):
        XO_()
    elif 3 in o_position and 1 in x_position and 2 not in (x_position or o_position):
        X_O()
    elif 1 in o_position and 3 in x_position and 2 not in (x_position or o_position):
        O_X()
    elif 2 in o_position and 3 in x_position and 1 not in (x_position or o_position):
        _OX()
    elif 3 in o_position and 2 in x_position and 1 not in (x_position or o_position):
        _XO()
    elif 1 in x_position and 2 not in (x_position or o_position) and 3 not in (x_position or o_position):
        X__()
    elif 2 in x_position and 1 not in (x_position or o_position) and 3 not in (x_position or o_position):
        _X_()
    elif 3 in x_position and 1 not in (x_position or o_position) and 2 not in (x_position or o_position):
        __X()
    elif 1 in x_position and 2 in x_position and 3 not in (x_position or o_position):
        XX_()
    elif 1 in x_position and 3 in x_position and 2 not in (x_position or o_position):
        X_X()
    else:
        _XX()


def if_o_wins_end_game():
    global game_concluded
    if 1 in result_list_for_o and 2 in result_list_for_o and 3 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    if 4 in result_list_for_o and 5 in result_list_for_o and 6 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    elif 7 in result_list_for_o and 8 in result_list_for_o and 9 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    elif 1 in result_list_for_o and 4 in result_list_for_o and 7 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    elif 2 in result_list_for_o and 5 in result_list_for_o and 8 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    elif 3 in result_list_for_o and 6 in result_list_for_o and 9 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    elif 1 in result_list_for_o and 5 in result_list_for_o and 9 in result_list_for_o:
        print("\n\n\n\n\nWell done " + Player_O + " , you won!")
        game_concluded = True
    else:
        if 3 in result_list_for_o and 5 in result_list_for_o and 7 in result_list_for_o:
            print("\n\n\n\n\nWell done " + Player_O + " , you won!")
            game_concluded = True


def if_x_wins_end_game():
    global game_concluded
    if 1 in result_list_for_x and 2 in result_list_for_x and 3 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    elif 4 in result_list_for_x and 5 in result_list_for_x and 6 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    elif 7 in result_list_for_x and 8 in result_list_for_x and 9 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    elif 1 in result_list_for_x and 4 in result_list_for_x and 7 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    elif 2 in result_list_for_x and 5 in result_list_for_x and 8 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    elif 3 in result_list_for_x and 6 in result_list_for_x and 9 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    elif 1 in result_list_for_x and 5 in result_list_for_x and 9 in result_list_for_x:
        print("\n\n\n\n\nWell done " + Player_X + " , you won!")
        game_concluded = True
    else:
        if 3 in result_list_for_x and 5 in result_list_for_x and 7 in result_list_for_x:
            print("\n\n\n\n\nWell done " + Player_X + " , you won!")
            game_concluded = True


def update_lists_for_x_positions():
    result_list_for_x.append(player_x_latest_number)
    if player_x_latest_number in (1, 2, 3):
        top_row_x_position.append(player_x_latest_number)
    elif player_x_latest_number in (4, 5, 6):
        mid_row_x_position.append(player_x_latest_number)
    else:
        bottom_row_x_position.append(player_x_latest_number)


def update_lists_for_o_positions():
    result_list_for_o.append(player_o_latest_number)
    if player_o_latest_number in (1, 2, 3):
        top_row_o_position.append(player_o_latest_number)
    elif player_o_latest_number in (4, 5, 6):
        mid_row_o_position.append(player_o_latest_number)
    else:
        bottom_row_o_position.append(player_o_latest_number)


def would_you_like_to_play_again():
    global play_game
    question_answered = False
    while not question_answered:
        play_again = input("\n\n\n\nWould you like to play again? Y/N: ").lower()
        if play_again in ("y", "yes"):
            play_game = True
            question_answered = True
        elif play_again in ("n", "no"):
            play_game = False
            question_answered = True
        else:
            print("\n\n\n\nPlease choose only Y or N")


def if_draw_end_game():
    global game_concluded
    if len(result_list_for_o + result_list_for_x) == 9:
        print("\n\n\nIt was a draw.")
        game_concluded = True


def clear_screen():
    for i in range(50):
        print()


def position_of_O_validated():
    global player_o_latest_number
    valid_number_choice = False
    while not valid_number_choice:
        raw_input_o = input(Player_O + ", please enter a number from the reference grid to lay down your naught: ")
        if raw_input_o.isdigit():
            player_o_latest_number = int(raw_input_o)
            if player_o_latest_number in used_numbers:
                print("\nThat number has already been chosen. Try again.")
            elif player_o_latest_number not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                print("\nThat was not a valid choice. See the grid above")
            else:
                used_numbers.append(player_o_latest_number)
                valid_number_choice = True
        else:
            print("\nPlease only enter numbers, between 1 & 9!")

def position_of_X_validated():
    global player_x_latest_number
    valid_number_choice = False
    while not valid_number_choice:
        raw_input_x = input(Player_X + ", please enter a number from the reference grid to lay down your cross: ")
        if raw_input_x.isdigit():
            player_x_latest_number = int(raw_input_x)
            if player_x_latest_number in used_numbers:
                print("\nThat number has already been chosen. Try again.")
            elif player_x_latest_number not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                print("\nThat was not a valid choice. See the grid above")
            elif str(player_x_latest_number) not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("\nThat was not a valid choice. See the grid above")
            else:
                used_numbers.append(player_x_latest_number)
                valid_number_choice = True
        else:
            print("\nPlease only enter numbers, between 1 & 9!")


play_game = True
while play_game:

    clear_screen()
    print("NOUGHTS & CROSSES\n\n\n\n\n\n")
    Player_O = input("Player O, please enter your name: ")
    Player_X = input("Player X, please enter your name: ")

    used_numbers = []

    top_row_o_position = []
    top_row_x_position = []
    mid_row_o_position = []
    mid_row_x_position = []
    bottom_row_o_position = []
    bottom_row_x_position = []

    result_list_for_o = []
    result_list_for_x = []
    player_o_latest_number = []
    player_x_latest_number = []

    clear_screen()
    print_grid_reference()
    game_concluded = False
    while not game_concluded:

        position_of_O_validated()
        update_lists_for_o_positions()
        clear_screen()
        print_grid_reference()

        print_top_row()
        horizontal_line()
        print_middle_row()
        horizontal_line()
        print_bottom_row()

        if_o_wins_end_game()
        if_draw_end_game()

        if game_concluded:
            would_you_like_to_play_again()
            break

        position_of_X_validated()
        update_lists_for_x_positions()
        clear_screen()
        print_grid_reference()

        print_top_row()
        horizontal_line()
        print_middle_row()
        horizontal_line()
        print_bottom_row()

        if_x_wins_end_game()
        if_draw_end_game()

        if game_concluded:
            would_you_like_to_play_again()
