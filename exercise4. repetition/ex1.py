secret_number = 45
number_of_guesses = 0
won = False

print('Try to find the secret number (1 - 100)')
while not won:
    number_of_guesses += 1
    guess = int(input(f'Guess #{number_of_guesses}: '))
    if guess == secret_number:
        won = True
    elif guess < secret_number:
        print('Your guess is to small, try a bigger number')
    elif guess > secret_number:
        print('Your guess is to big, try a smaller number')

print(f'Well done! You found the correct number in {number_of_guesses} tries')