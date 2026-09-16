number = int(input('Input a three digit number: '))

last_digit = number % 10
number = number // 10

middle_digit = number % 10
number = number // 10

first_digit = number

sum_of_digits = first_digit + middle_digit + last_digit

print('The sum of the three digit is ' + str(sum_of_digits))