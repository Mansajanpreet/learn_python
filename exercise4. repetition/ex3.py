print('\n -- -- First pattern -- -- \n')
for y in range(1, 7):
    for x in range(0, y):
        print('*', end='')
    print()

print('\n -- -- Second pattern -- -- \n')
for y in range(0, 4):
    for x in range(0, 5):
        print('*', end='')
    print()

print('\n -- -- Third pattern -- -- \n')
for y in range(10, 0, -2):
    for x in range(0, y):
        print('*', end='')
    print()

print('\n -- -- Fourth pattern -- -- \n')
current_char = '*'
for y in range(0, 4):
    for x in range(0, 9):
        print(current_char, end='')
        if current_char == '*':
            current_char = ' '
        else:
            current_char = '*'
    print()

print('\n -- -- Fifth pattern -- -- \n')
inner_count = 1
for y in range(0, 4):
    for x in range(0, inner_count):
        print('*', end='')
    print()
    inner_count *= 2

# Fifth pattern - Alternative
# for i in range(4):
#     for _ in range(2**i):
#         print('*', end='')
#     print()