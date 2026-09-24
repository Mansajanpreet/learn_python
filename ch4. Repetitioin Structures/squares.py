# This program uses a loop to display a 
# table showing the number 1 through 10
# and their squares.

# print the table heading
print("Number\tSquare")
print("---------------")

#print the number 1 through 10
#and their squares.
for number in range(1,11):
    square = number ** 2
    print(f"{number}\t{square}") 
