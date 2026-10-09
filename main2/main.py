title = input("Enter the title: ")
items = ""
counter = 0

while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    print("S. Show number of added items")
    

    choice = input("Enter your choice: ")

    if choice == "1":
        if items >= 10:
            print("ERROR: The list is full, your item was not added")
        else:
            item = input("Enter an item: ")
            items += item + "\n"
            counter += 1

    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    elif choice == "S" or choice == "s":
        print(f"Currently the list contains {counter} item(s)")

    

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)
        
        break

    else:
        print("Error: Invalid choice, please try again.")
