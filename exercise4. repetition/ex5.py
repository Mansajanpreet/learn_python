name = 'Not set yet'
phone_number = 'N/A'
balance = 1000
keep_running = True

while keep_running:
    print('\n--- The best bank ---')
    print('1. Create an account')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. Display account')
    print('9. Exit')

    choice = int(input('\nEnter choice: '))
    print()

    if choice == 1:
        name = input('Name: ')
        phone_number = input('Phone number: ')
        balance = 0
    elif choice == 2:
        deposit = int(input('How much do you want to deposit? '))
        balance += deposit
    elif choice == 3:
        withdraw = int(input('How much do you want to withdraw? '))
        balance -= withdraw
    elif choice == 4:
        print(f'Name         : {name:>15}')
        print(f'Phone number : {phone_number:>15}')
        print(f'Balance      : {balance:>15.2f}')
    elif choice == 9:
        keep_running = False