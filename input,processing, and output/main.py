title = input("Enter a title: ")
items = ""

while True:
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input()
        if items == "":
            items = item
        else:
            items += "\n" + item
    elif choice == "2":
        print(items)
    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)
        break
    else:
        print("Error: Invalid choice, please try again.")
