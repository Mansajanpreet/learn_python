print('Welcome to our bank!\n')

first_name = input("Enter your name:")    #Display the first and last name.
last_name = input("Enter your last name:")
civic_number = input("Enter your civi number:")
balance = float(input("How much money you have (SEK):")) #Display the loan amount and interest for user.
interest_rate = float(input("Enter the interest rate:"))

balance_one_year = balance * (1 + (interest_rate / 100)) #Display balance after one year with interest.M

print('Your information:\n')

print(f'Name: {first_name} {last_name}')
print(f'Civic number: {civic_number} ')
print(f'Balance: {balance} SEK')            
print(f'Interest: {interest_rate} %\n')

print(f'after one year you will have: {balance_one_year} SEK')

deposit = float(input("Enter your deposit amount:"))

print(f'Your new balance is: {balance_one_year + deposit}')