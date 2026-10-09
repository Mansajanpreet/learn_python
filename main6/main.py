title = input("Enter the title: ")
items = ""
edited = ("don,t f**k")

while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    print("C. Change title.")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        items += item + "\n"

    elif choice == "c" or choice == "C":
        new_title = input("Enter the new title: ")
        if new_title == title:
            print("INFO: The new title is the same as the old one.")
        if new_title == "":
            print("ERROR: Title can not be empty.")
        else:
            title = new_title
            edited = ("yes f**k")

    elif choice == "2":
        print(f"Currently added items:\n{items}")

    

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        if edited == ("yes f**k"):
            print(f"{'(edited)':^20}")
        print("-" * 20)
        print(items)
        break

    else:
        print("Error: Invalid choice, please try again.")
