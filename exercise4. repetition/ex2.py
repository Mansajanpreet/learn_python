print('This script will calculate the sum for 1 to n (1 + 2 + … + n)')
n = int(input('Specify n: '))

# A solution using a count-controlled loop
print('\nSolving it using a count-controlled loop.')
sum_count_controlled = 0

for i in range(1, (n + 1)):
    sum_count_controlled += i

print(f'  Min: 1')
print(f'  Max: {n}')
print(f'  Sum: {sum_count_controlled}')
print(f'  Avg: {sum_count_controlled / n}')

# Gives the same result as above, but using a condition-controlled loop instead
print('\nSolving it using a condition-controlled loop.')
sum_condition_controlled = 0
current_number = 1

while current_number <= n:
    sum_condition_controlled += current_number
    current_number += 1

print(f'  Min: 1')
print(f'  Max: {n}')
print(f'  Sum: {sum_condition_controlled}')
print(f'  Avg: {sum_condition_controlled / n}')