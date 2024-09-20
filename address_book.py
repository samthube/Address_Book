from regex_validation import *
import logger_file

logger = logger_file.logger_init('address_book')

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, address, city, state, zip_code, phone, email):
        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.contacts.append(contact)
        logger.info(f"Contact {first_name} {last_name} added successfully.")

    def display_contacts(self):
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
