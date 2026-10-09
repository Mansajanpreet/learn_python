def fib(count):
    first = 0                                       # Store the first number in the sequence
    second = 1                                      # Store the second number in the sequence

    if count == 1:                                  # Printing one numbers from the sequence does not require a loop
        print(f'Number[0]: {first}')
    elif count >= 2:                                # If more than one number, print the first two manually, then use a loop for the others
        print(f'Number[0]: {first}')
        print(f'Number[1]: {second}')
        for i in range(2, count):
            n = first + second
            print(f'Number[{i}]: {n}')

            first = second
            second = n


def main():
    fib(8)


main()