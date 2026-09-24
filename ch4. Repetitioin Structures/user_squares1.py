# This program uses a loop to display a 
# table of number and their squares.

# print the ending limit.
print("This program display a list of numbers")
print("(starting at 1) and their squares.")
end = int(input("How high should I go? "))

#print the table headings.
print()
print("Number\tSquare")
print("---------------")

#print the number and their squares.
for number in range(1, end +1):
    square = number ** 2
    print(f"{number}\t{square}") 
