# This program uses the return value of a function.

def main():
    # Get the user's age.
    first_age = int(input("Enter your age: "))

    #Get the user best friend's age.
    second_age = int(input("Enter your best friend's age: "))

    #Get the sum of both ages.
    total = sum(first_age, second_age)

    # Display the result.
    print(f"Together you are {total} years old.")

# The sum function accepts two numeric arguments and
# return the sum of those arguments.
def sum(num1, num2):

    return num1 + num2
    

main()