# Contact Manager

#### Video Demo: https://youtu.be/3zD6lwnaIqM

#### Description:
The Contact Manager is a Python-based command-line application used to handle contacts, specifically for adding, searching, deleting, updating, and listing contacts in a CSV file.

### Functionality
The Contact Manager provides a menu-driven user interface that enables users to do the following operations:

1. **Add Contact**: The user will be prompted to enter a first name, last name, phone number, email, and address for the new contact. If successful, a message is returned from the system.

2. **Search Contact**: By providing a first and last name, this feature enables the user to look up any previous contact. If there is a match, all of the contact's data stored fields are displayed.

3. **Update Contact**: The user can update any previously existing contact by providing the first and last name of the contact. The user is required to fill in new values for the data fields. If they are not filled in, their values remain the same.

4. **Delete Contact**: Contacts are deleted from the system based on the first and last name entered by the user. If successful, the system returns a message.

5. **List Contacts**: All available contacts information in the CSV file get listed, represented in tabular form for readability.

6. **Exit**: The user can exit the application when finished managing contacts.

### Contact Class
The `Contact` class represents individual contacts, encapsulating properties like first name, last name, phone number, email address, and physical address. It includes validation methods to ensure data integrity through getter and setter methods.

For example, the `phone` property setter ensures the phone number contains only digits and has exactly 10 characters, while the `email` property setter checks if the email address matches a simple regular expression pattern.

By using the `Contact` class, the application can create, modify, and manage contact objects in a structured and organized manner, ensuring data integrity and consistency.

### Files Overview:
- `project.py`: This is the main file containing the application logic, including the implementation of the `Contact` class.
- `contacts.csv`: This CSV file acts as the back-end storage for all contacts, with columns representing table headers like First Name, Last Name, Phone Number, Email Address, and Address.

### Design Decisions:
- **CSV as Data Storage**: CSV was chosen because it's simple and easy to deal with using Python's `csv` module to read from/write to it without the need for any fully-featured database system.
- **Validation**: Implemented within the `Contact` class,  it ensures that no invalid data is accumulated in the system.
- **Menu-driven Interface**: A clear menu driven interface is developed using the `tabulate` library, which makes it much easier to view since this represents all the options clearly in a very readable format.
- **Error Handling**: For the whole application, proper error handling is included so that any turn of unexpected events that occur, it will behave nicely and always show a clear error message if possible.
- **Object-Oriented Design**: The use of the `Contact` class promotes an object-oriented design approach, encapsulating contact-related data and behavior within a single class.

### Usage:
How to run the Contact Manager:

1. Python should be installed on the system with the following libraries: `csv`, `re`, and `tabulate`.
2. Download or clone the project files: `project.py` and `contacts.csv`.
3. Run `project.py`.
4. Depending on the menu options displayed, perform the preferred actions on the contacts: add, search, update, delete, and list contacts.

### Conclusion:
The Contact Manager is an example of how Python can be used for simple data management tasks. It provides a lightweight, friendly way to store and manage contact information, aided by input validation and error checking upon user mistakes in order to preserve data integrity. The implementation of the `Contact` class demonstrates the use of object-oriented programming principles, helping with code organization, reusability, and maintainability.
