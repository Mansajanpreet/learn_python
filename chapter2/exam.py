title = input("Enter a title for your shopping list: ")


while True:
    print("\nMenu")
    print("1. Add an item")
    print("2. View shopping list")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter an item: ")
        shopping_list += item + "\n"
        print("Item added.")

    elif choice == "2":
        print(f"\n{title}")
        print("-" * len(title))

        if shopping_list == "":
            print("Your shopping list is empty.")
        else:
            print(shopping_list)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")