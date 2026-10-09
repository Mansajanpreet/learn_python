def is_hit(x, y):
    if (3 <= x <= 5) and y == 2:                # Check if we hit the first ship, the yellow one
        return True
    elif x == 6 and (7 <= y <= 9):              # Check if we hit the second ship, the green one
        return True
    else:                                       # In all other cases we missed
        return False


def format_output(shot_x, shot_y, hit):
    if hit:
        return f'Congratulations! You hit a ship at (x={shot_x}, y={shot_y}).'
    else:
        return f'Sorry! No ship at (x={shot_x}, y={shot_y}).'


def main():
    x1 = 4
    y1 = 2

    x2 = 6
    y2 = 9

    x3 = 3
    y3 = 6

    print()
    print(format_output(shot_x=x1, shot_y=y1, hit=is_hit(x=x1, y=y1)))
    print(format_output(shot_x=x2, shot_y=y2, hit=is_hit(x=x2, y=y2)))
    print(format_output(shot_x=x3, shot_y=y3, hit=is_hit(x=x3, y=y3)))
    print()


main()