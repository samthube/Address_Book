'''
@Author: Samadhan Thube
@Date: 2024-09-23
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-09-23
@Title : Address Book Program 
'''

from regex_validation import *
import logger_file
import os
import csv

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
        return f"\nName: {self.first_name} {self.last_name},\nAddress: {self.address},\nCity: {self.city},\nState: {self.state},\nzip Code: {self.zip_code},\nPhone: {self.phone},\nEmail: {self.email}\n{'*'*50}"


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
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                logger.error(f"Duplicate entry: Contact {first_name} {last_name} already exists.")
                return
            
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
            
    def sort_by_name(self):
        """
        Description:
            Sorts the contacts in the address book by their first name in alphabetical order.

        Parameter:
            None

        Return:
            None
        """
        if not self.contacts:
            logger.warning("No contacts available to sort.")
        else:
            self.contacts.sort(key=lambda contact: contact.first_name.lower())
            logger.info("Contacts sorted by first name.")
            self.display_contacts()

    def sort_by_city(self):
        """
        Description:
            Sorts the contacts in the address book by the city name in alphabetical order.

        Parameter:
            None

        Return:
            None
        """
        if not self.contacts:
            logger.warning("No contacts available to sort.")
        else:
            self.contacts.sort(key=lambda contact: contact.city.lower())
            logger.info("Contacts sorted by city.")
            self.display_contacts()

    def sort_by_state(self):
        """
        Description:
            Sorts the contacts in the address book by the state name in alphabetical order.

        Parameter:
            None

        Return:
            None
        """
        if not self.contacts:
            logger.warning("No contacts available to sort.")
        else:
            self.contacts.sort(key=lambda contact: contact.state.lower())
            logger.info("Contacts sorted by state.")
            self.display_contacts()

    def sort_by_zip(self):
        """
        Description:
            Sorts the contacts in the address book by their zip code in ascending numerical order.

        Parameter:
            None

        Return:
            None
        """
        if not self.contacts:
            logger.warning("No contacts available to sort.")
        else:
            self.contacts.sort(key=lambda contact: contact.zip_code)
            logger.info("Contacts sorted by zip code.")
            self.display_contacts()
            
    def save_contact_to_file(self, first_name, last_name, filename):
        """
        Description:
            Saves a specific contact to a text file.

        Parameter:
            first_name (str): First name of the contact to save.
            last_name (str): Last name of the contact to save.
            filename (str): The name of the file to save the contact.

        Return:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                with open(filename, 'w') as file:
                    file.write(str(contact))
                logger.info(f"Contact {first_name} {last_name} saved to {filename}.")
                return
        logger.error(f"No contact found with name {first_name} {last_name}.")

    
    def load_contacts_from_file(self, filename):
        """
        Description:
            Loads contacts from a text file into the address book.

        Parameter:
            filename (str): The name of the file to load contacts from.

        Return:
            None
        """
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    if len(data) == 8:  
                        first_name, last_name, address, city, state, zip_code, phone, email = data
                        self.add_contact(first_name, last_name, address, city, state, zip_code, phone, email)
                logger.info(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            logger.error(f"The file {filename} was not found.")
        except Exception as e:
            logger.error(f"An error occurred while loading contacts: {e}")

    def write_contact_to_csv(self, first_name, last_name, filename):
        """
        Description:
            Writes a specific contact from the address book to a CSV file.

        Parameter:
            first_name (str): First name of the contact to write to CSV.
            last_name (str): Last name of the contact to write to CSV.
            filename (str): Name of the CSV file to save the contact.

        Return:
            None
        """
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["First Name", "Last Name", "Address", "City", "State", "Zip", "Phone", "Email"])
                    writer.writerow([contact.first_name, contact.last_name, contact.address, contact.city,
                                    contact.state, contact.zip_code, contact.phone, contact.email])
                logger.info(f"Contact {first_name} {last_name} saved to {filename}.")
                return
        logger.error(f"No contact found with name {first_name} {last_name}.")


    def load_contacts_from_csv(self, filename):
        """
        Description:
            Loads contacts from a CSV file into the address book.

        Parameter:
            filename (str): Name of the CSV file to load contacts from.

        Return:
            None
        """
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    first_name = row["First Name"]
                    last_name = row["Last Name"]
                    address = row["Address"]
                    city = row["City"]
                    state = row["State"]
                    zip_code = row["Zip"]
                    phone = row["Phone"]
                    email = row["Email"]
                    self.add_contact(first_name, last_name, address, city, state, zip_code, phone, email)
                logger.info(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            logger.error(f"The file {filename} was not found.")
        except Exception as e:
            logger.error(f"An error occurred while loading contacts from CSV: {e}")

class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, book_name):
        """
        Description:
            Adds a new address book to the system.

        Parameter:
            book_name (str): The unique name of the address book.

        Return:
            None
        """
        if book_name in self.address_books:
            logger.warning(f"Address book '{book_name}' already exists.")
        else:
            self.address_books[book_name] = AddressBook()
            logger.info(f"Address book '{book_name}' created successfully.")

    def select_address_book(self, book_name):
        """
        Description:
            Selects an existing address book by name.

        Parameter:
            book_name (str): The name of the address book to select.

        Return:
            AddressBook: The selected address book.
        """
        return self.address_books.get(book_name, None)

    def search_person(self, location, search_type, display_details=True):
        """
        Description:
            Searches for people in a specific city or state across multiple address books.
        
        Parameter:
            location (str): The city or state to search for.
            search_type (str): 'city' or 'state', indicating which field to search.
            display_details (bool): If True, displays contact details; if False, only counts the contacts.

        Return:
            count (int): The total number of contacts found.
        """
        found = False
        count = 0
        for book_name, address_book in self.address_books.items():
            logger.info(f"Searching in address book: {book_name}")
            for contact in address_book.contacts:
                if (search_type == 'city' and contact.city.lower() == location.lower()) or \
                (search_type == 'state' and contact.state.lower() == location.lower()):
                    if display_details:
                        print(f"\nContact found in Address Book '{book_name}':")
                        print(contact)
                    found = True
                    count += 1

        if not found and display_details:
            logger.warning(f"No contacts found in {search_type.capitalize()}: {location}")
        return count

def validation():
    """
    Description:
        Collects and validates user input for address, city, state, zip code, phone, and email.
        Repeats asking for input if invalid data is entered.

    Parameter:
        None

    Return:
        tuple: A tuple containing validated values (address, city, state, zip_code, phone, email).
    """
    address = input("Enter address: ")

    while True:
        city = input("Enter city: ")
        if validate_name(city):
            break
        else:
            logger.error("Invalid city name. Please try again.")

    while True:
        state = input("Enter state: ")
        if validate_name(state):
            break
        else:
            logger.error("Invalid state name. Please try again.")

    while True:
        zip_code = input("Enter zip code: ")
        if validate_zip(zip_code):
            break
        else:
            logger.error("Invalid zip code. Please try again.")

    while True:
        phone = input("Enter phone number (xx xxxxxxxxxx): ")
        if validate_phone(phone):
            break
        else:
            logger.error("Invalid phone number. Please try again.")

    while True:
        email = input("Enter email: ")
        if validate_email(email):
            break
        else:
            logger.error("Invalid email. Please try again.")

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
    address_book_system = AddressBookSystem()

    while True:
        print("\n1. Create new address book")
        print("2. Select and manage an address book")
        print("3. Search for a person by city or state")
        print("4. Get count of contacts by city or state")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            logger.warning("Invalid input. Please enter a number from the menu.")
            continue

        if choice == 1:
            book_name = input("Enter address book name: ")
            address_book_system.add_address_book(book_name)

        elif choice == 2:
            book_name = input("Enter the name of the address book you want to manage: ")
            selected_book = address_book_system.select_address_book(book_name)

            if selected_book:
                while True:
                    print(f"\nManaging Address Book: {book_name}")
                    print("1. Add contact")
                    print("2. Show contacts")
                    print("3. Edit contact")
                    print("4. Delete contact")
                    print("5. Save contact to file")
                    print("6. Load contact from file")
                    print("7. Sort by")
                    print("8. Back to main menu")

                    try:
                        action_choice = int(input("Enter your choice: "))
                    except ValueError:
                        logger.warning("Invalid input. Please enter a number from the menu.")
                        continue

                    if action_choice == 1:
                        first_name = input_name("first")
                        last_name = input_name("last")
                        details = validation()
                        if details:
                            address, city, state, zip_code, phone, email = details
                            selected_book.add_contact(first_name, last_name, address, city, state, zip_code, phone, email)

                    elif action_choice == 2:
                        selected_book.display_contacts()

                    elif action_choice == 3:
                        first_name = input_name("first")
                        last_name = input_name("last")
                        selected_book.edit_contact(first_name, last_name)

                    elif action_choice == 4:
                        first_name = input_name("first")
                        last_name = input_name("last")
                        selected_book.delete_contact(first_name, last_name)
                        
                    elif action_choice == 5: 
                        while True:
                            print("\n1. Save to text file")
                            print("2. Save to csv file")
                            print("3. Go Back")
                            
                            try:
                                save_choice = int(input("Enter your choice: "))
                            except ValueError:
                                logger.warning("Invalid input. Please enter a number from the menu.")
                                continue
                            
                            if save_choice == 1:
                                first_name = input_name("first")
                                last_name = input_name("last")
                                filename = input("Enter the filename to save the contact: ")
                                selected_book.save_contact_to_file(first_name, last_name, filename)
                            
                            elif save_choice == 2:
                                first_name = input_name("first")
                                last_name = input_name("last")
                                filename = input("Enter the CSV filename to save the contact: ")
                                selected_book.write_contact_to_csv(first_name, last_name, filename)
                            
                            elif save_choice == 3:
                                break
                            else:
                                logger.warning("Invalid option. Please select a valid choice.")

                    elif action_choice == 6:
                        while True:
                            print("\n1. Load from text file")
                            print("2. Load from csv file")
                            print("3. Go Back")
                            
                            try:
                                load_choice = int(input("Enter your choice: "))
                            except ValueError:
                                logger.warning("Invalid input. Please enter a number from the menu.")
                                continue
                            
                            if load_choice == 1:
                                filename = input("Enter the filename to load contacts from: ")
                                selected_book.load_contacts_from_file(filename)
                                
                            elif save_choice == 2:
                                filename = input("Enter the CSV filename to load contacts from: ")
                                selected_book.load_contacts_from_csv(filename)
                            
                            elif save_choice == 3:
                                break
                            else:
                                logger.warning("Invalid option. Please select a valid choice.")
                                  
                    elif action_choice == 7:
                        while True:
                            print(f"\nManaging Address Book: {book_name}")
                            print("1. Name")
                            print("2. City")
                            print("3. State")
                            print("4. Zip")
                            print("5. Back to main menu")

                            try:
                                sort_choice = int(input("Enter your choice: "))
                            except ValueError:
                                logger.warning("Invalid input. Please enter a number from the menu.")
                                continue
                            
                            if sort_choice == 1:
                                selected_book.sort_by_name()
                                print("Contacts sorted by city.")

                            elif sort_choice == 2:
                                selected_book.sort_by_city()
                                print("Contacts sorted by city.")

                            elif sort_choice == 3:
                                selected_book.sort_by_state()
                                print("Contacts sorted by state.")

                            elif sort_choice == 4:
                                selected_book.sort_by_zip()
                                print("Contacts sorted by zip code.")

                            elif sort_choice == 5:
                                break
                            else:
                                logger.warning("Invalid option. Please select a valid choice.")
                                
                    elif action_choice == 8:
                        break
                    else:
                        logger.warning("Invalid option. Please select a valid choice.")
            else:
                logger.error(f"Address book '{book_name}' not found.")
                
        elif choice == 3:
            search_type = input("Search by 'city' or 'state': ").lower()
            if search_type not in ['city', 'state']:
                logger.warning("Invalid search type. Please enter 'city' or 'state'.")
                continue

            location = input(f"Enter the {search_type} name to search for: ")
            address_book_system.search_person(location, search_type)
            
        elif choice == 4:
            search_type = input("Get count by 'city' or 'state': ").lower()
            if search_type not in ['city', 'state']:
                logger.warning("Invalid search type. Please enter 'city' or 'state'.")
                continue

            location = input(f"Enter the {search_type} name to get count: ")
            count = address_book_system.search_person(location, search_type, display_details=False)
            print(f"\nTotal number of contacts in {search_type.capitalize()} '{location}': {count}")

        elif choice == 5:
            logger.info("Exiting the program.")
            break
        else:
            logger.warning("Invalid choice. Please select from the menu options.")


if __name__ == "__main__":
    main()
