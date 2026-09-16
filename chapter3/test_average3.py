# This program gets three test scores and displays
# their average. It congratulates the user if the 
# average is a high score.

# The HIGH SCORE named constant holds the value that is
# consider a high score
HIGH_SCORE = 90

# Get the three exams score.
exam1 = int(input('Enter your score exam1: '))
exam2= int(input('Enter your score exam2: '))
exam3 = int(input('Enter your score exam3: '))

#Calculate the average score
average = (exam1 + exam2 + exam3) / 3

# print the average score.
print(f'The average score is {average:.2f}.')

# If the average is a high score
# Congratulate the user
# else good score
if average >= HIGH_SCORE:
 print('Congratulation!')
 print('You are above on average.')
else:
 print('Good score')