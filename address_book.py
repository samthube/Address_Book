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
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"

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

def main():
    address_book = AddressBook()
    
    while True:
        print("\n1. Add contact details")
        print("2. Show contact details")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            
            first_name = input("Enter first name: ")
            if not validate_name(first_name):
                logger.error("Invalid first name. Please try again.")
                continue

            last_name = input("Enter last name: ")
            if not validate_name(last_name):
                logger.error("Invalid last name. Please try again.")
                continue

            address = input("Enter address: ")

            city = input("Enter city: ")
            if not validate_name(city):
                logger.error("Invalid city name. Please try again.")
                continue

            state = input("Enter state: ")
            if not validate_name(state):
                logger.error("Invalid state name. Please try again.")
                continue

            zip_code = input("Enter zip code: ")
            if not validate_zip(zip_code):
                logger.error("Invalid zip code. Please try again.")
                continue

            phone = input("Enter phone number (xx xxxxxxxxxx): ")
            if not validate_phone(phone):
                logger.error("Invalid phone number. Please try again.")
                continue

            email = input("Enter email: ")
            if not validate_email(email):
                logger.error("Invalid email. Please try again.")
                continue

            address_book.add_contact(first_name, last_name, address, city, state, zip_code, phone, email)

        elif choice == 2:
            
            address_book.display_contacts()

        elif choice == 3:
            logger.info("Exiting the address book application.")
            break
        
        else:
            logger.warning("Invalid choice. Please select from 1, 2, or 3.")

if __name__ == "__main__":
    main()
