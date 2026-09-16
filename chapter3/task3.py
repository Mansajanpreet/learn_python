guess = int(input('what is 6 + 7?'))
answer = 13

if guess == 13:
    print('Correct!')
elif guess < answer:
    print('Guess is small.')
else:
    print('Guess too big.')