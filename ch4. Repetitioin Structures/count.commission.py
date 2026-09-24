# This program calculates sales commissions.
# Count variable
count = 1


# Get the number of salespeople.
salespeople = int(input("Enter the number of salespeople: "))

# Calculate each salesperson's commission.

while count <= salespeople:
    # Get salesperson's sales and commission rate.
    sales = float(input(f"Enter the sales person {count}: "))
    comm_rate = float(input("Enter the commission rate: "))

    # Calculate the commission rate.
    commission = sales * (comm_rate / 100)

    # Display the commission.
    print(f"The commission is ${commission:,.2f}")

    #update the counter variable.
    count += 1