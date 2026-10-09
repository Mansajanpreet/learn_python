title = input("Enter the title: ")
items = ""

while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        counter = int(input("Enter number of items: "))
        if counter < 1 or counter > 99:
            print("ERROR: You must buy at least 1 but not more than 99 of an item. Try again!")


        combined = (f"{item:<10}x{counter:>9}")
        items += combined + "\n"
        

    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)

        break

    else:
        print("Error: Invalid choice, please try again.")
