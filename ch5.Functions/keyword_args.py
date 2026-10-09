# This program demostrates keyword arguments.

def main():
    # Show the amount of simple interest, using 0.01 as 
    # interest rate per period, 10 as the number of periods,
    # and $10,000 as the principal
    show_interest(rate=0.01, periods=10, principal=10000.0)

    # The show_interest function displays the amount of
    # Simple interest for a given principal, interest rate.
    # Per period, and number of periods.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f"The simple interest will be ${interest:,.2f}")
    def inner_function():
        ...


# Call the main function.
main() 