# This program allows the user to choose various
# geometry calculations from a menu.

import math

# Constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


# ---------- Circle functions ----------
def circle_area(radius):
    return math.pi * radius ** 2


def circle_circumference(radius):
    return 2 * math.pi * radius


# ---------- Rectangle functions ----------
def rectangle_area(width, length):
    return width * length


def rectangle_perimeter(width, length):
    return 2 * (width + length)


# ---------- Input helpers ----------
def get_number(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Error: please enter a valid number.")


def get_choice():
    """Keep asking until the user enters a whole number."""
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Error: please enter a number from 1 to 5.")


# ---------- Menu ----------
def display_menu():
    print("\nMENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")


# ---------- Main ----------
def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = get_choice()

        if choice == AREA_CIRCLE_CHOICE:
            radius = get_number("Enter the circle's radius: ")
            print("The area is", round(circle_area(radius), 2))

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = get_number("Enter the circle's radius: ")
            print("The circumference is", round(circle_circumference(radius), 2))

        elif choice == AREA_RECTANGLE_CHOICE:
            width = get_number("Enter the rectangle's width: ")
            length = get_number("Enter the rectangle's length: ")
            print("The area is", round(rectangle_area(width, length), 2))

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = get_number("Enter the rectangle's width: ")
            length = get_number("Enter the rectangle's length: ")
            print("The perimeter is", round(rectangle_perimeter(width, length), 2))

        elif choice == QUIT_CHOICE:
            print("Exiting the program...")

        else:
            print("Error: invalid selection. Choose 1 to 5.")


main()