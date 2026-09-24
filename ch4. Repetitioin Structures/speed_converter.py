# This program converts the speed 60 kph
# through 130 kph (in 10 kph increments)
# to mph.

START_SPEED = 60
END_SPEED = 130
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

# Print the table headings.
print("KPH\tMPH")
print("------------")

# Print the speeds.
for kph in range (START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f"{kph}\t{mph:.1f}")