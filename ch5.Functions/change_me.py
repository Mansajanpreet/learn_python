# This program demostrates what happens when you
# change the value of a parameter

def main():
    value = 99
    print(f" The value is {value}.")
    change_me(value)
    print(f"Back in main the value is {value}.")

def change_me (very_descriptive_name_of_the_parameter):
    print("I am changing the value.")
    very_descriptive_name_of_the_parameter = 0
    print(f"Now the value is {very_descriptive_name_of_the_parameter}.")

main()
