title = input("Enter the title: ")
items = ""
total_cost = 0
units = 0
lowest_cost = ""
highest_cost = ""

while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        price = float(input("Enter the price: "))
        count = int(input("Enter the count: "))

        item_cost = price * count
        total_cost += item_cost
        units += count
        items += item + "\n"
        if lowest_cost == "" or price < lowest_cost:
            lowest_cost = price
        if highest_cost == "" or price > highest_cost:
            highest_cost = price
            

           

    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items, end="")
        print(f"Total cost: {total_cost:.2f} SEK")
        print(f"{'Units':<10}: {units}")
        average_cost = total_cost / units
        print(f"Price info: {lowest_cost:.2f} (Low) / {highest_cost:.2f} (High) / {average_cost:.2f} (Average) SEK")

        break

    else:
        print("Error: Invalid choice, please try again.")