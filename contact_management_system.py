# Contact Management System

print("===== CONTACT MANAGEMENT SYSTEM =====")

contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")

    else:
        print("\n----- CONTACT LIST -----")

        for name, contact in contacts.items():
            print("Name:", name)
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("------------------------")


def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        contact = contacts[name]

        print("\n----- CONTACT DETAILS -----")
        print("Name:", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])

    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        contacts[name]["phone"] = input("Enter new phone number: ")
        contacts[name]["email"] = input("Enter new email: ")

        print("Contact updated successfully.")

    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]

        print("Contact deleted successfully.")

    else:
        print("Contact not found.")


while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Exiting Contact Management System...")
        break

    else:
        print("Invalid choice. Please try again.")