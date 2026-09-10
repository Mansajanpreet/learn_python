#Get the desired future value.
future_value = float(input("Enter the desired future value: "))

#Get the annual interest.
rate = float(input("Enter the annual interest rate: "))

#Get the number of years that the money will appreciate.

years = int(input("Enter the number of years the money will grow: "))

#calculate the amount need to deposit.
present_value = future_value / (1.0 + rate / 100)**years

#Display the amount need to deposit.
print("You will need t deposit this amount: ", present_value)