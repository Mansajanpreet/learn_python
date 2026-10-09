def display_menu():
    print('\n--- The best bank ---')
    print('1. Create an account')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. Display account')
    print('9. Exit')


def create_account():
    name = input('Name: ')
    phone_number = input('Phone number: ')
    balance = 0

    return name, phone_number, balance


def deposit():
    deposit = int(input('How much do you want to deposit? '))
    return deposit


def withdraw(current_balance):
    withdraw = int(input('How much do you want to withdraw? '))
    new_balance = current_balance - withdraw
    return new_balance


def display(name, phone_number, balance):
    print(f'Name         : {name:>15}')
    print(f'Phone number : {phone_number:>15}')
    print(f'Balance      : {balance:>15.2f}')


def main():
    name = 'Not set yet'
    phone_number = 'N/A'
    balance = 1000
    keep_running = True

    while keep_running:
        display_menu()

        choice = int(input('\nEnter choice: '))
        print()

        if choice == 1:
            name, phone_number, balance = create_account()
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            display(name, phone_number, balance)
        elif choice == 9:
            keep_running = False


main()

