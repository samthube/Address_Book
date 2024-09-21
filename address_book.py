'''
@Author: Samadhan Thube
@Date: 2024-09-20 
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-09-20 
@Title : Address Book Program
'''

from regex_validation import *
import logger_file

logger = logger_file.logger_init('address_book')

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        """
        Description:
            Class to represent a contact with attributes like name, address, and other details.

        Parameter:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
            address (str): The address of the contact.
            city (str): The city of the contact.
            state (str): The state of the contact.
            zip_code (str): The zip code of the contact.
            phone (str): The phone number of the contact.
            email (str): The email address of the contact.

        Return:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Description:
            Returns a string representation of the contact.

        Parameter:
            None

        Return:
            str: The formatted string representation of the contact.
        """
        return f"\nName: {self.first_name} {self.last_name},\nAddress: {self.address},\nCity: {self.city},\nState: {self.state},\nzip Code: {self.zip_code},\nPhone: {self.phone},\nEmail: {self.email}\n{"*"*50}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        """
        Description:
            Adds a new contact to the address book after validating the input fields.

        Parameter:
            first_name (str): First name of the contact.
            last_name (str): Last name of the contact.
            address (str): Address of the contact.
            city (str): City of the contact.
            state (str): State of the contact.
            zip_code (str): Zip code of the contact.
            phone (str): Phone number of the contact.
            email (str): Email address of the contact.

        Return:
            None
        """
        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.contacts.append(contact)
        logger.info(f"Contact {first_name} {last_name} added successfully.")

    def display_contacts(self):
        """
        Description:
            Displays all the contacts in the address book. Logs a warning if there are no contacts.

        Parameter:
            None

        Return:
            None
        """
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            logger.warning("No contacts available to display.")

    def edit_contact(self, first_name, last_name):
        """
        Description:
            Edits an existing contact based on the provided first and last name.

        Parameter:
            first_name (str): First name of the contact to edit.
            last_name (str): Last name of the contact to edit.

        Return:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                logger.info(f"Editing contact: {contact}")
                updated_details = validation()
                if updated_details:
                    address, city, state, zip_code, phone, email = updated_details
                    contact.address = address
                    contact.city = city
                    contact.state = state
                    contact.zip_code = zip_code
                    contact.phone = phone
                    contact.email = email
                    logger.info(f"Contact {first_name} {last_name} updated successfully.")
                break
        else:
            logger.error(f"No contact found with name {first_name} {last_name}.")

    def delete_contact(self, first_name, last_name):
        """
        Description:
            Deletes a contact based on the provided first and last name.

        Parameter:
            first_name (str): First name of the contact to delete.
            last_name (str): Last name of the contact to delete.

        Return:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                logger.info(f"Contact {first_name} {last_name} deleted successfully.")
                break
        else:
            logger.error(f"No contact found with name {first_name} {last_name}.")


def validation():
    """
    Description:
        Collects and validates user input for address, city, state, zip code, phone, and email.

    Parameter:
        None

    Return:
        tuple: A tuple containing validated values (address, city, state, zip_code, phone, email).
    """
    address = input("Enter address: ")

    city = input("Enter city: ")
    if not validate_name(city):
        logger.error("Invalid city name. Please try again.")
        return

    state = input("Enter state: ")
    if not validate_name(state):
        logger.error("Invalid state name. Please try again.")
        return

    zip_code = input("Enter zip code: ")
    if not validate_zip(zip_code):
        logger.error("Invalid zip code. Please try again.")
        return

    phone = input("Enter phone number (xx xxxxxxxxxx): ")
    if not validate_phone(phone):
        logger.error("Invalid phone number. Please try again.")
        return

    email = input("Enter email: ")
    if not validate_email(email):
        logger.error("Invalid email. Please try again.")
        return

    return address, city, state, zip_code, phone, email


def input_name(field_name):
    """
    Description:
        Validates the input for first name or last name.

    Parameter:
        field_name (str): Field name (first or last) to prompt the user for input.

    Return:
        str: Validated name.
    """
    while True:
        name = input(f"Enter {field_name} name: ")
        if validate_name(name):
            return name
        else:
            logger.error(f"Invalid {field_name} name. Please try again.")


def main():
    
    address_book = AddressBook()

    while True:
        print("\n1. Add contact details")
        print("2. Show contact details")
        print("3. Edit contact details")
        print("4. Delete contact details")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            logger.warning("Invalid input. Please enter a number from the menu.")
            continue

        if choice == 1:
            first_name = input_name("first")
            last_name = input_name("last")

            details = validation()
            if details:
                address, city, state, zip_code, phone, email = details
                address_book.add_contact(first_name, last_name, address, city, state, zip_code, phone, email)

        elif choice == 2:
            address_book.display_contacts()

        elif choice == 3:
            first_name = input_name("first")
            last_name = input_name("last")
            address_book.edit_contact(first_name, last_name)

        elif choice == 4:
            first_name = input_name("first")
            last_name = input_name("last")
            address_book.delete_contact(first_name, last_name)

        elif choice == 5:
            logger.info("Exiting the address book application.")
            break

        else:
            logger.warning("Invalid choice. Please select from 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
