# This program assists a technician in the process.
# of checking a substance's temperature.

# Named constant to represent the maximum
# temperature.
MAX_TEMP = 102.5

# Get the substance's temperature.
temperature = float(input("Enter the substance's Celsius temperature: "))

# As long as necessary, instruct the user to 
# adjust the thermost.
while temperature > MAX_TEMP:
    print("The temperature is too high.")
    print("Turn the thermostat down and wait")
    print("5 mintues. Then take the temperature")
    print("again and enter it.")
    temperature = float(input("Enter the new Celsius temperature: "))

    # Remind the user to check the temperature again 
    # in 15 minutues. 
print("The temperature is acceptable.")
print("Check it again in 15 minutes.")
