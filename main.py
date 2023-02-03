import numpy as np
import random

game = np.zeros((3, 3))


def print_game(structure):
    for i in range(len(structure)):
        for j in range(len(structure)):
            # print(f' {structure[i][j]}', end=" ")
            if structure[i][j] == 1:
                print(f' X', end=" ")
            elif structure[i][j] == 2:
                print(f' O', end=" ")
            else:
                print(f'  ', end=" ")
            if j != len(structure) - 1:
                print('|', end="")
        print('\n------------')


def check_player_win(structure):
    for i in range(len(structure)):
        win_sum = 0
        for j in range(len(structure)):
            if structure[i][j] == 1:
                win_sum += 1
        if win_sum == 3:
            return True

    # check columns
    for i in range(len(structure)):
        win_sum = 0
        for j in range(len(structure)):
            if structure[j][i] == 1:
                win_sum += 1
        if win_sum == 3:
            return True

    if (structure[0][0] == 1) and (structure[1][1] == 1) and (structure[2][2] == 1):
        return True
    elif (structure[0][2] == 1) and (structure[1][1] == 1) and (structure[2][0] == 1):
        return True
    else:
        return False


def check_computer_win(structure):
    # check rows
    for i in range(len(structure)):
        win_sum = 0
        for j in range(len(structure)):
            if structure[i][j] == 2:
                win_sum += 1
        if win_sum == 3:
            return True
    # check columns
    for i in range(len(structure)):
        win_sum = 0
        for j in range(len(structure)):
            if structure[j][i] == 2:
                win_sum += 1
        if win_sum == 3:
            return True

    if (structure[0][0] == 2) and (structure[1][1] == 2) and (structure[2][2] == 2):
        return True
    elif (structure[0][2] == 2) and (structure[1][1] == 2) and (structure[2][0] == 2):
        return True
    else:
        return False


def check_if_full(structure):
    for i in range(len(structure)):
        for j in range(len(structure)):
            if structure[i][j] == 0:
                return False
    return True


def check_player_input(structure):
    while True:
        while True:
            try:
                row_sel = int(input('Please enter the row you want: '))
                if row_sel > 3:
                    raise ValueError
            except ValueError:
                print('Please choose a valid number (between 1 and 3)')
            else:
                break

        while True:
            try:
                col_sel = int(input('Please enter the column you want: '))
                if col_sel > 3:
                    raise ValueError
            except ValueError:
                print('Please choose a valid number (between 1 and 3)')
            else:
                break
        if structure[row_sel - 1][col_sel - 1] != 0:
            print('The location is taken, please choose another location!')
        else:
            break
    structure[row_sel - 1][col_sel - 1] = 1
    return structure

# def check_player_input(structure, row_sel, col_sel):
#     if row_sel is None:
#         try:
#             row_sel = int(input('Please enter the row you want: '))
#         except ValueError:
#             print('Please choose a valid number (between 1 and 3)')
#             check_player_input(structure, row_sel=None, col_sel=col_sel)
#     if row_sel > 3:
#         print('Please choose a valid number (between 1 and 3)')
#         check_player_input(structure, row_sel=None, col_sel=col_sel)
#
#     if col_sel is None:
#         try:
#             col_sel = int(input('Please enter the column you want: '))
#         except ValueError:
#             print('Please choose a valid number (between 1 and 3)')
#             check_player_input(structure, row_sel=row_sel, col_sel=None)
#     if col_sel > 3:
#         print('Please choose a valid number (between 1 and 3)')
#         check_player_input(structure, row_sel=row_sel, col_sel=None)
#     if structure[row_sel - 1][col_sel - 1] != 0:
#         print('The location is taken, please choose another location!')
#         check_player_input(structure, row_sel=None, col_sel=None)
#     structure[row_sel - 1][col_sel - 1] = 1
#     return structure


# def check_computer_input(structure):
#     row_sel = random.randint(0, 2)
#     col_sel = random.randint(0, 2)
#     if structure[row_sel][col_sel] != 0:
#         check_computer_input(structure)
#     structure[row_sel][col_sel] = 2
#     return structure

def check_computer_input(structure):
    while True:
        row_sel = random.randint(0, 2)
        col_sel = random.randint(0, 2)
        if structure[row_sel][col_sel] == 0:
            structure[row_sel][col_sel] = 2
            return structure


player_turn = random.randint(0, 1)
print('You will play the game by typing which row and column you want to draw on!')
if player_turn:
    print('You will go first!')
else:
    print('The computer will go first!')
print('--------------------------------------------------------------------------')
while True:
    row = None
    col = None
    if player_turn:
        if check_if_full(game):
            print('----------------------------------')
            print('Nobody won, a tie!')
            print('----------------------------------')
            break
        print_game(structure=game)
        game = check_player_input(structure=game)
        if check_player_win(game):
            print('----------------------------------')
            print_game(game)
            print('You win!')
            print('----------------------------------')
            break
        player_turn = 0

    if not player_turn:
        if check_if_full(game):
            print('----------------------------------')
            print_game(game)
            print('Nobody won, a tie!')
            print('----------------------------------')
            break
        else:
            print('Computer turn!')
        game = check_computer_input(structure=game)
        if check_computer_win(game):
            print('----------------------------------')
            print_game(game)
            print('Game over, you lost!')
            print('----------------------------------')
            break
        player_turn = 1
