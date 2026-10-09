title = input("Enter the title: ")
items = ""
total_cost = 0
units = 0

while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        price = float(input("Enter the price: "))
        count = float(input("Enter the item count: "))
        items += item + "\n"
        total_cost += price * count
        units += count

    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)
        print(f"Total cost: {total_cost:.2f} SEK")
        print(f"{"Units":<10}: {units}")
        break

    else:
        print("Error: Invalid choice, please try again.")
