first_name = input("Enter your name:")    #Display the first and last name.
last_name = input("Enter your last name:")

balance = float(input("How much money you have (SEK):")) #Display the loan amount and interest for user.
interest_rate = float(input("Enter the interest rate:"))

balance_one_year = balance * (1 + (interest_rate / 100)) #Display balance after one year with interest.M

print(f'Name: {first_name} {last_name}')
print(f'Balance: {balance} SEK')            
print(f'Interest: {interest_rate} %')
print(f'Balance after one year: {balance_one_year} SEK')

