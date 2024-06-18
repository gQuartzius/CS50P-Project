# Contact Manager

#### Video Demo: https://youtu.be/3zD6lwnaIqM

#### Description:
The Contact Manager is a Python-based command-line application used to handle contacts and provide the user with an interface for adding, searching, deleting, updating, and listing contacts in a CSV file.

### Functionality
The Contact Manager provides a menu-driven user interface that enables users to do the following operations:

1. **Add Contact**: The user will be prompted to enter a first name, last name, phone number, email, and address for the new contact. Phone numbers are validated to contain all digits only and that there are exactly 10 characters in the phone number. Email addresses are also validated with some simple regular expression pattern. If successful, a message with text to this effect is returned from the system.

2. **Search Contact**: This feature allows the user to look up any pre-existing contact given a first and last name. In case of a match, it then displays detailed information about that contact with all the fields stored.

3. **Update Contact**: A user can update any previously existing contact by providing the first and last name of the contact. The user is required to fill in new values for fields such as the first name, last name, phone number, email address, and address. If fields are not filled in, their values remain the same.

4. **Delete Contact**: Contacts are deleted from the system based on the first and last names. If successful, a message with text to this effect is returned from the system.

5. **List Contacts**: All available contacts in the CSV file get listed. The contact details are therefore represented in tabular form for readability.

6. **Exit**: A user can quit the application when they are through managing contacts.

### Files Overview:
- `project.py`: This is the main file containing the application logic.
- `contacts.csv`: This CSV file acts as the back-end storage for all contacts, with columns representing table headers like First Name, Last Name, Phone Number, Email Address, and Address.

### Design Decisions:
- **CSV as Data Storage**: CSV was chosen because it's simple and easy to deal with using Python's `csv` module to read from/write to it without the need for any fully-featured database system.
- **Validation**: Phone number and email address validation is in place, hence no accumulation of bad data in the system is allowed.
- **Menu-driven Interface**: A clean and clear user interface with a menu-driven interface is developed using the `tabulate` library, which makes it much easier to view since this represents all the options clearly in a very readable format.
- **Error Handling**: For the whole application, proper error handling at every stage is included so that any turn of unexpected events that occur, it will behave nicely and always show a clear error message if possible.

### Usage:
How to run the Contact Manager:

1. Python should be installed on the system with the following libraries: `csv`, `re`, and `tabulate`.
2. Download or clone the project files: `project.py` and `contacts.csv`.
3. Run `project.py`.
4. Depending on the menu options displayed, perform the preferred actions on the contacts: add, search, update, delete, and list contacts.

### Conclusion:
The Contact Manager is an example of how Python can be used for simple data management tasks. It provides a lightweight, friendly way to store and manage contact information, aided by input validation and error checking upon user mistakes in order to preserve data integrity.
