# This program determines wheather a bank customer
# qualifies for a loan.

MIN_SALARY = 30000       # This minimum annual salary.
MIN_YEARS = 2             # This minimum years on the job.

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years current job.
year_on_job = float(input('Enter the number of year of ' +
                         'years employed: '))

# Determine the customer is qualifier.
if salary >= MIN_SALARY:
    if year_on_job >= MIN_YEARS:
        print('your qualify for the loan.')
    else:
        print(f'You must have been employed '
                  f'for at least {MIN_YEARS} '
                  F'years to qualify.')
else:
    print(f'You must earn at least $'
          f'{MIN_SALARY:,.2f}'
          f'per year to qualify.')
