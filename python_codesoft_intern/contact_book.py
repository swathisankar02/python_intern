#CONTACT BOOK

def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    email = input("Enter the contact email: ")
    address = input("Enter the contact address: ")
    contact_book[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact '{name}' added.")

def view_contacts(contact_book):
    if contact_book:
        print("\nContacts:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found.")

def search_contact(contact_book):
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contact_book.items():
        if search_term in name or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact(contact_book):
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        phone = input("Enter the new phone number (or press Enter to keep the current one): ")
        email = input("Enter the new email (or press Enter to keep the current one): ")
        address = input("Enter the new address (or press Enter to keep the current one): ")
        
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        if address:
            contact_book[name]['address'] = address
        
        print(f"Contact '{name}' updated.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contact_book):
    name = input("Enter the contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contact_book = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            update_contact(contact_book)
        elif choice == '5':
            delete_contact(contact_book)
        elif choice == '6':
            print("Exiting the contact book.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
