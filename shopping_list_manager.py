# Shopping List Manager

print("===== SHOPPING LIST MANAGER =====")

shopping_list = []

while True:
    print("\n1. Add Item")
    print("2. View Shopping List")
    print("3. Remove Item")
    print("4. Clear Shopping List")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")

        if item == "":
            print("Item name cannot be empty.")
        else:
            shopping_list.append(item)
            print("Item added successfully.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")

        else:
            print("\n----- SHOPPING LIST -----")

            for index, item in enumerate(shopping_list, start=1):
                print(index, ".", item)

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")

        else:
            item = input("Enter item to remove: ")

            if item in shopping_list:
                shopping_list.remove(item)
                print("Item removed successfully.")
            else:
                print("Item not found.")

    elif choice == "4":
        shopping_list.clear()
        print("Shopping list cleared.")

    elif choice == "5":
        print("Exiting Shopping List Manager...")
        break

    else:
        print("Invalid choice. Please try again.")