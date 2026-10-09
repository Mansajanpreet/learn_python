title = input("Enter the title: ")
items = ""
reset_count = 0


while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    print("R. Reset shopping list.")
    print("T. Reset from Template.")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        items += item + "\n"

    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    elif choice == "R" or choice == "r":
        reset = input("Are you sure (y/n)?")
        if reset == "y" or reset == "Y":
            items = ""
            reset_count += 1

    elif choice == "T" or choice == "t":
        option1 = ("Dumle\nJapp\nBilar")
        option2 = ("Apple\nPear\nBanana")
        print("1) Sweets template")
        print("2) Fruit template")

        pick = input("Pick one option: ")
        if pick == "1":
            items = option1
        if pick == "2":
            items = option2
        else:
            print("Invalid option, pick 1 or 2")
        reset_count += 1
            
            
            
        

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)
        
        if reset_count == 0:
            print("<< Shopping list was never reset >>")
        else:
            print(f"<< Shopping list was reset {reset_count} time(s) >>")
        break

    else:
        print("Error: Invalid choice, please try again.")
