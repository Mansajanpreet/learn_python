# Named constants to represent the base hours and
# the over time.
BASE_HOURS = 40 # base hours per week.
OT_multiplier = 1.5 # overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of you worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# calculate and display the gross pay.
if hours > BASE_HOURS:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked.
    overtime_hours = hours - BASE_HOURS

    # calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * OT_multiplier

    # Calculate the gross pay.
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    #calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print(f'The gross pay is $ {gross_pay:,.2f} ')


