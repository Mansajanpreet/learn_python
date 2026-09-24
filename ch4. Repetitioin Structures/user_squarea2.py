# This program uses a loop to display a 
# table of number and their squares.

# Get the starting value.
print("This program display a list of numbers and their squares")
start = int(input("Enter the starting number: "))

# Get the ending limit
end = int(input("How high should I go? "))

#print the table headings.
print()
print("Number\tSquare")
print("---------------")

#print the number and their squares.
for number in range(start, end +1):
    square = number ** 2
    print(f"{number}\t{square}") 
