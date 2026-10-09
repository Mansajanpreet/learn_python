# This program demostrates passing two strings.
# arguments to a function.

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last_name: ")
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

#call the main function
main()