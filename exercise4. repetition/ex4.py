number_accepted = False
n = 0

print('Check if a number is a prime number or not.')
while not number_accepted:
    n = int(input('Input a number (2-100): '))
    if n >= 2 and n <= 100:
        number_accepted = True

is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(f'{n} is a prime number')
else:
    print(f'{n} is NOT a prime number')