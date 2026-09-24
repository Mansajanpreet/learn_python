title = input("Enter the title: ")
items = ""
item_counter = 0


while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    print("S. Show number of added items")

    choice = input("Enter your choice: ")

    if choice == "1":
        if item_counter >= 10:
            print("ERROR: The list is full, your item was not added")
        else:
         item = input("Enter an item: ")
         items += item + "\n"
         item_counter += 1


    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)
        break

    elif choice == "S":
    
        print(f"Currently the list contains {item_counter} item(s)")
        print("[" + "*" * item_counter + " " * (10 - item_counter) + "]")

        
    else:
     print("Error: Invalid choice, please try again.")
        
