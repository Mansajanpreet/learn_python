# This program demostrates two functions that 
# have local variables with the same name.

def main():
    # Call the texas function. 
    texas()
    # Call the california function.
    california()

# Defination of the texas function. It creates 
# a local variable named birds
def texas():
    birds = 5000
    print(f"Texas has {birds} birds.")

# Defination of the california function. It also
#creates a local variable named birds.
def california():
    birds = 8000
    print(f"California has {birds} birds.")

main()