# The following is used as a global constant to represent 
# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input("Enter the gross pay: "))
    bonus = float(input("Enter the amount of bonuses: "))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement.
# contribution for that amount of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f"Contribution for gross pay: ${contrib:,.2f}.")

# The show bonus contrib accepts the bonus amount
# bonus amount as an argument and displays the
# retirement contribution for that amount pay.


def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f"Contribution for bonus: ${contrib:,.2f}.")

# Call the main function. 
main()