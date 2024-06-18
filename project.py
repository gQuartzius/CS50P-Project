import csv
import re
from tabulate import tabulate


class Contact:
    def __init__(self, first, last, phone, email=None, address=None):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"First Name: {self.first}, Last Name: {self.last}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number.")
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value and not re.match(r"^[^@]+@[^@]+\.[^@]+$", value):
            raise ValueError("Invalid email address.")
        self._email = value

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        if not value:
            raise ValueError("First name cannot be empty.")
        self._first = value

    def __dict__(self):
        return {
            "first": self.first,
            "last": self.last,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }


def load_contacts(file_path="contacts.csv"):
    contacts = []
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            contacts = [Contact(**row) for row in reader]
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(contacts, file_path="contacts.csv"):
    with open(file_path, "w", newline="") as file:
        fieldnames = ["first", "last", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(
                {
                    "first": contact.first,
                    "last": contact.last,
                    "phone": contact.phone,
                    "email": contact.email,
                    "address": contact.address,
                }
            )


def add_contact(first, last, phone, email=None, address=None, file_path="contacts.csv"):
    new_contact = Contact(first, last, phone, email, address)
    contacts = load_contacts(file_path)
    if not any(
        c.first == new_contact.first and c.last == new_contact.last for c in contacts
    ):
        contacts.append(new_contact)
        save_contacts(contacts, file_path)
        return "\n" + "Contact added successfully!"
    else:
        return "\n" + "Contact already exists."


def list_contacts(file_path="contacts.csv"):
    contacts = load_contacts(file_path)
    if contacts:
        contact_list = [
            {
                "First Name": contact.first,
                "Last Name": contact.last,
                "Phone": contact.phone,
                "Email": contact.email,
                "Address": contact.address,
            }
            for contact in contacts
        ]
        return tabulate(contact_list, headers="keys", tablefmt="grid")
    else:
        return "\n" + "No contacts available."


def delete_contact(first, last, file_path="contacts.csv"):
    contacts = load_contacts(file_path)
    contact_found = False
    for index, contact in enumerate(contacts):
        if contact.first == first and contact.last == last:
            del contacts[index]
            save_contacts(contacts, file_path)
            contact_found = True
            return "\n" + "Contact deleted successfully."
    if not contact_found:
        return "\n" + "Contact not found."


def update_contact(
    first,
    last,
    new_first=None,
    new_last=None,
    new_phone=None,
    new_email=None,
    new_address=None,
    file_path="contacts.csv",
):
    contacts = load_contacts(file_path)
    contact_found = False
    for contact in contacts:
        if contact.first == first and contact.last == last:
            contact_found = True
            contact.first = new_first or contact.first
            contact.last = new_last or contact.last
            contact.phone = new_phone or contact.phone
            contact.email = new_email or contact.email
            contact.address = new_address or contact.address
            save_contacts(contacts, file_path)
            return "\n" + "Contact updated successfully."
    if not contact_found:
        return "\n" + "Contact not found."


def search_contact(first, last, file_path="contacts.csv"):
    contacts = load_contacts(file_path)
    contact_list = []
    contact_found = False
    for contact in contacts:
        if contact.first == first and contact.last == last:
            contact_list.append(
                {
                    "First Name": contact.first,
                    "Last Name": contact.last,
                    "Phone": contact.phone,
                    "Email": contact.email,
                    "Address": contact.address,
                }
            )
            contact_found = True

    if contact_found:
        return tabulate(contact_list, headers="keys", tablefmt="grid")
    else:
        return "\n" + "Contact not found."


def main():
    menu = [
        ["1", "Add Contact"],
        ["2", "Search Contact"],
        ["3", "Delete Contact"],
        ["4", "Update Contact"],
        ["5", "List Contacts"],
        ["6", "Exit"],
    ]

    while True:
        print("\n", tabulate(menu, headers=["Option", "Action"], tablefmt="grid"))
        choice = input("Enter your choice: ")
        print()
        try:
            if choice == "1":
                first = input("First Name: ")
                last = input("Last Name: ")
                phone = input("Phone: ")
                email = input("Email (optional): ")
                address = input("Address (optional): ")
                print(add_contact(first, last, phone, email, address))
            elif choice == "2":
                first = input("First Name of the contact to search: ")
                last = input("Last Name of the contact to search: ")
                print(search_contact(first, last))
            elif choice == "3":
                first = input("First Name of the contact to delete: ")
                last = input("Last Name of the contact to delete: ")
                print(delete_contact(first, last))
            elif choice == "4":
                first = input("First Name of the contact to update: ")
                last = input("Last Name of the contact to update: ")
                new_first = input(
                    "New First Name (leave blank to keep current value): "
                )
                new_last = input("New Last Name (leave blank to keep current value): ")
                new_phone = input("New Phone (leave blank to keep current value): ")
                new_email = input("New Email (leave blank to keep current value): ")
                new_address = input("New Address (leave blank to keep current value): ")
                print(
                    update_contact(
                        first,
                        last,
                        new_first,
                        new_last,
                        new_phone,
                        new_email,
                        new_address,
                    )
                )
            elif choice == "5":
                print(list_contacts())
            elif choice == "6":
                break
            else:
                print("Invalid input.")
        except ValueError as e:
            print(f"Error: {e}")

    print("Goodbye!")


if __name__ == "__main__":
    main()
