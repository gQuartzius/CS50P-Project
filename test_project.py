import pytest
import os
from project import (
    Contact,
    add_contact,
    delete_contact,
    search_contact,
    update_contact,
    load_contacts,
    save_contacts,
)

TEST_CSV_FILE = "test_contacts.csv"


@pytest.fixture
def setup_contacts():
    contacts = [
        Contact(
            "John", "Harvard", "1234567890", "john.harvard@example.com", "123 Street"
        ),
        Contact(
            "Harry", "Potter", "0987654321", "harry.potter@example.com", "123 Hogwarts"
        ),
    ]
    save_contacts(contacts, TEST_CSV_FILE)
    yield
    if os.path.exists(TEST_CSV_FILE):
        os.remove(TEST_CSV_FILE)


def test_add_contact(setup_contacts):
    assert (
        add_contact(
            "Hermione",
            "Granger",
            "1112223333",
            "hermione.granger@example.com",
            "123 Hogwarts",
            TEST_CSV_FILE,
        )
        == "\nContact added successfully!"
    )
    contacts = load_contacts(TEST_CSV_FILE)
    assert any(c.first == "Hermione" and c.last == "Granger" for c in contacts)


def test_add_duplicate_contact(setup_contacts):
    contacts = load_contacts(TEST_CSV_FILE)
    assert (
        add_contact(
            "John",
            "Harvard",
            "1234567890",
            "john.harvard@example.com",
            "123 Street",
            TEST_CSV_FILE,
        )
        == "\nContact already exists."
    )
    assert len([c for c in contacts if c.first == "John" and c.last == "Harvard"]) == 1


def test_delete_contact(setup_contacts):
    assert (
        delete_contact("Harry", "Potter", TEST_CSV_FILE)
        == "\nContact deleted successfully."
    )
    contacts = load_contacts(TEST_CSV_FILE)
    assert not any(c.first == "Harry" and c.last == "Potter" for c in contacts)


def test_delete_nonexistent_contact(setup_contacts):
    assert delete_contact("Hermione", "Granger", TEST_CSV_FILE) == "\nContact not found."


def test_search_contact(setup_contacts):
    result = search_contact("John", "Harvard", TEST_CSV_FILE)
    assert "John" in result
    assert "Harvard" in result
    assert "1234567890" in result


def test_search_nonexistent_contact(setup_contacts):
    assert search_contact("Test", "Name", TEST_CSV_FILE) == "\nContact not found."


def test_update_contact(setup_contacts):
    assert (
        update_contact(
            "John", "Harvard", new_phone="5555555555", file_path=TEST_CSV_FILE
        )
        == "\nContact updated successfully."
    )
    contacts = load_contacts(TEST_CSV_FILE)
    assert any(
        c.phone == "5555555555"
        for c in contacts
        if c.first == "John" and c.last == "Harvard"
    )


def test_validate_contact():
    test = Contact("Test", "Name", "1112223333", "test.name@example.com")
    with pytest.raises(ValueError):
        test.phone = "111222"
    with pytest.raises(ValueError):
        test.email = "invalid-email"
    with pytest.raises(ValueError):
        test.first = ""
