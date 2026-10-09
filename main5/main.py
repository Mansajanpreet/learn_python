title = input("Enter the title: ")
items = ""
total_price = 0


while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    print("C. Calculate price.")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item: ")
        price = float(input("Enter the price: "))
        items += item + "\n"


    elif choice == "2":
        print()
        print(f"Currently added items:\n{items}")

    elif choice == "C" or choice == "c":
        smallest = ""
        largest = ""
        
        for i in range(3):
            price = int(input("Enter the price of item: "))
            total_price += price

            if smallest == "" or price < smallest:
                smallest = price
            if largest == "" or price > largest:
                largest = price

            average = total_price / 3
    
    
    

        

    

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)
        print(items)
        print(f"Total price:{total_price:>5} SEK")
        print(f"Min: {smallest}, Max: {largest}, Average: {average:.2f}")
        break

    else:
        print("Error: Invalid choice, please try again.")
