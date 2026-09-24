# This program demostrates an infinite loop.
# Create a variable to control the loop.
Keep_going = 'y'

# Warning! Infinite loop!
while Keep_going == 'y':
    # Get a salesperson's sales and commission rate.
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    #calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print(f"The commission is ${commission:,.2f}")
