print('--- Menu ---')
print('1. Calculate n raised to the power of n')
print('2. Calculate the sum of the arithmetic series 1, 2, 3, ..., n')

choice = input('Choose an option (1 or 2): ')

if choice == '1':
    n = int(input('Input n: '))
    result = n**n
    print(f'n raised to the power of n is {result}')
elif choice == '2':
    n = int(input('Input n: '))
    result = n * ((1 + n) / 2)
    print(f'The sum is {result}')