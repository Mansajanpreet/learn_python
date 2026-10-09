def find_smallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


def find_biggest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def find_sum(a, b, c):
    return a + b + c


def find_average(a, b, c):
    return find_sum(a, b, c) / 3


def main():
    print('\nPlease specify the following three numbers:')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    print(f'\nThe smallest number is {find_smallest(a, b, c)}')
    print(f'The biggest number is {find_biggest(a, b, c)}')
    print(f'The sum is {find_sum(a, b, c)}')
    print(f'The average is {find_average(a, b, c):.2f}\n')


main()