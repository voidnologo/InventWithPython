
# Sonar

import random
import sys
from color import Colorize as c


RING_SET = []
MIN_X = 0
MAX_X = 59
MIN_Y = 0
MAX_Y = 14


# def clear_rings(board):
#     for x in range(MIN_X, MAX_X + 1):
#         for y in range(MIN_Y, MAX_Y + 1):
#             board[x][y] = '.'
#     return board


def gen_ring(point, distance):
    ring = []
    x1 = MIN_X if point[0] - distance < MIN_X else point[0] - distance
    x2 = MAX_X if point[0] + distance + 1 > MAX_X else point[0] + distance + 1
    for x in range(x1, x2):
        lower_y = point[1] - distance if point[1] - distance > MIN_Y else MIN_Y
        upper_y = point[1] + distance if point[1] + distance < MAX_Y else MAX_Y
        ring.append((x, lower_y))
        ring.append((x, upper_y))
    y1 = MIN_Y if point[1] - distance < MIN_Y else point[1] - distance
    y2 = MAX_Y if point[1] + distance + 1 > MAX_Y else point[1] + distance + 1
    for y in range(y1, y2):
        lower_x = point[0] - distance if point[0] - distance > MIN_X else MIN_X
        upper_x = point[0] + distance if point[0] + distance < MAX_X else MAX_X
        ring.append((lower_x, y))
        ring.append((upper_x, y))
    return ring


def draw_board(board):
    # Draw the board data structure.

    hline = '    '  # initial space for the numbers down the left side of the board
    for i in range(1, 6):
        hline += '{}{}'.format((' ' * 9), c.colorize('YELLOW', i))

    # print the numbers across the top
    print(hline)
    num_lin = '{}123456789'.format(c.colorize('YELLOW', 0))
    print('{}{}'.format('   ', (num_lin * 6)))
    print()

    # print each of the 15 rows
    for i in range(15):
        # single-digit numbers need to be padded with an extra space
        if i < 10:
            extra_space = ' '
        else:
            extra_space = ''
        print('{}{} {} {}'.format(extra_space, i, get_row(board, i), i))

    # print the numbers across the bottom
    print()
    print('{}{}'.format('   ', (num_lin * 6)))
    print(hline)


def pluralize(item):
    if item > 1:
        return 's'
    return ''


def get_row(board, row):
    # Return a string from the board data structure at a certain row.
    board_row = ''
    for i in range(60):
        board_row += board[i][row]
    return board_row


def get_new_board():
    # Create a new 60x15 board data structure.
    board = []
    for x in range(60):  # the main list is a list of 60 lists
        board.append([])
        for y in range(15):  # each list in the main list has 15 single-character strings
            # use different characters for the ocean to make it more readable.
            # if random.randint(0, 1) == 0:
            #     board[x].append('~')
            # else:
            #     board[x].append('`')
            board[x].append('.')
    return board


def get_random_chests(num_chests):
    # Create a list of chest data structures (two-item lists of x, y int coordinates)
    chests = []
    for i in range(num_chests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    return chests


def is_valid_move(x, y):
    # Return True if the coordinates are on the board, otherwise False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14


def make_move(board, chests, x, y):
    # Change the board data structure with a sonar device character. Remove treasure chests
    # from the chests list as they are found. Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    if not is_valid_move(x, y):
        return False

    smallest_distance = 100  # any chest will be closer than 100.
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)

        if distance < smallest_distance:  # we want the closest treasure chest.
            smallest_distance = distance

    if smallest_distance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallest_distance < 10:
            ring = gen_ring((x, y), smallest_distance)
            RING_SET.extend(ring)
            for a, b in set(RING_SET):
                if board[a][b] == '.':
                    board[a][b] = '{}'.format(c.colorize('BLUE', '.'))
            board[x][y] = '{}'.format(c.colorize('GREEN', smallest_distance))
            return 'Treasure detected at a distance of {} from the sonar device.'.format(smallest_distance)
        else:
            board[x][y] = '{}'.format(c.colorize('RED', '0'))
            return 'Sonar did not detect anything. All treasure chests out of range.'


def enter_player_move():
    # Let the player type in her move. Return a two-item list of int xy coordinates.
    print('Where do you want to drop the next sonar device? (0-59, 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split(',')
        if len(move) == 2 and move[0].strip().isdigit() and move[1].strip().isdigit() and is_valid_move(int(move[0].strip()), int(move[1].strip())):
            return [int(move[0].strip()), int(move[1].strip())]
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')


def play_again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def show_instructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to find the three sunken treasure chests that are lurking in the part of the
ocean you are in and collect them.

To play, enter the coordinates of the point in the ocean you wish to drop a
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and the 2's
represent distances of 2 away from the device. The 4's represent
distances of 4 away from the device.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Press enter to continue...''')
    input()

    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the sonar device (the d):

    22222
    c   2
    2 d 2
    2   2
    22222

The point where the device was dropped will be marked with a 2.

The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O

If a device is directly dropped on a treasure chest, you have discovered
the location of the chest, and it will be collected. The sonar device will
remain there.

When you collect a chest, all sonar devices will update to locate the next
closest sunken treasure chest.
Press enter to continue...''')
    input()
    print()


print('S O N A R !')
print()
print('Would you like to view the instructions? (yes/no)')
if input().lower().startswith('y'):
    show_instructions()

while True:
    # game setup
    sonar_devices = 16
    the_board = get_new_board()
    the_chests = get_random_chests(3)
    draw_board(the_board)
    previous_moves = []

    while sonar_devices > 0:
        # Start of a turn:

        # sonar device/chest status
        sonars = pluralize(sonar_devices)
        chests = pluralize(len(the_chests))
        print('You have {} sonar device{} left. {} treasure chest{} remaining.'.format(
            sonar_devices, sonars, len(the_chests), chests))

        x, y = enter_player_move()
        previous_moves.append([x, y])  # we must track all moves so that sonar devices can be updated.

        move_result = make_move(the_board, the_chests, x, y)
        if not move_result:
            continue
        else:
            if move_result == 'You have found a sunken treasure chest!':
                # update all the sonar devices currently on the map.
                RING_SET = []
                the_board = get_new_board()
                for x, y in previous_moves:
                    make_move(the_board, the_chests, x, y)
            draw_board(the_board)

        if len(the_chests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
            break

        sonar_devices -= 1

    if sonar_devices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print('    The remaining chests were here:')
        for x, y in the_chests:
            print('    {}, {}'.format(x, y))

    if not play_again():
        sys.exit()
