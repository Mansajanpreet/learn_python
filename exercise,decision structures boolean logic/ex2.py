lower_limit = int(input('Specify the lower range: '))
upper_limit = int(input('Specify the upper range: '))

print(f'\n The range is from {lower_limit} to {upper_limit}\n')

range = int(input('Enter the range: '))

if lower_limit <= range <= upper_limit:
    print('The number lies within the range.')
else:
    print('The number lies outside the range.')