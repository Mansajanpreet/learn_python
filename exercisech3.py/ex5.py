name = 'not set yet'
phone_number = 'NA'
balance = 1000
print('---THE EARTH BANK---')

print('1. Create an account.')
print('2. Deposit money.')
print('3. Withdraw money.')
print('4. Display account.')
print('5. Exit')

choice = int(input('Enter choice: '))

if choice == 1:
    name = input('Enter your name: ')
    phone_number = int(input('Enter your phone number: '))
    balance = 0
    print(f'Name         : {name:>15}')
    print(f'Phone Number : {phone_number:>15}')
    print(f'Balance      : {balance:>15.2f}')

elif choice == 2:
    deposit = int(input('How much do you want to deposit: '))
    balance += deposit
    print(f'Balance      : {balance:>15.2f}')

elif choice == 3:
    withdraw = int(input('How much do you want to withdraw: '))
    balance -= withdraw
    print(f'Balance      : {balance:>15.2f}')

elif choice == 4:
    print(f'Name         : {name:>15}')
    print(f'Phone number : {phone_number:>15}')
    print(f'Balance      : {balance:>15.2f}')

elif choice == 5:
    print('Thank you for using The Earth Bank.')
