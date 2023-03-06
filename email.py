class Email:
    """Creating a class definition for an email which takes in the arguments below
    and stores them as instance-level variables. It also takes in two more instance-level variables with default values."""

    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    def mark_as_read(self):
        """Method that changes the status of has_been_read."""
        self.has_been_read = True

    def mark_as_spam(self):
        """Method that changes the status of is_spam."""
        self.is_spam = True


class Inbox:
    """Class that stores all emails and takes in no arguments."""

    def __init__(self):
        self.emails = []

    def add_email(self, from_address, subject_line, email_contents):
        """Method which takes in the contents and email address from the received
        email to make a new Email object and stores it in the inbox"""
        new_email = Email(from_address, subject_line, email_contents)
        self.emails.append(new_email)

    def list_messages_from_sender(self, sender_address):
        """Method which returns a string showing all subject lines in emails from a specific sender, along with corresponding number"""
        subject_lines = []
        found_sender = False
        for i, email in enumerate(self.emails):
            if email.from_address == sender_address:
                subject_lines.append(f"{i}: {email.subject_line}")
                found_sender = True

        if not found_sender:
            print("No email found from this sender")
        return "\n".join(subject_lines)

    def get_email(self, sender_address, index):
        """Method that returns the email at a specific index from a specific user."""
        for email in self.emails:
            if email.from_address == sender_address and not email.has_been_read:
                if index == 0:
                    email.mark_as_read()
                    return email.email_contents
                else:
                    index -= 1
        raise IndexError("Email not found.")

    def mark_as_spam(self, sender_address, index):
        """Method that marks the email at a specific index within a sender address as spam."""
        for email in self.emails:
            if email.from_address == sender_address and not email.is_spam:
                if index == 0:
                    email.mark_as_spam()
                    return
                else:
                    index -= 1
        raise IndexError("Email not found.")

    def get_unread_emails(self):
        """Method that returns a string containing a list of all unread emails."""
        unread_subject_lines = []
        for email in self.emails:
            if not email.has_been_read:
                unread_subject_lines.append(email.subject_line)
        return "\n".join(unread_subject_lines)

    def get_spam_emails(self):
        """Method that returns a string containing a list of all spam emails."""
        spam_subject_lines = []
        for email in self.emails:
            if email.is_spam:
                spam_subject_lines.append(email.subject_line)
        return "\n".join(spam_subject_lines)

    def delete(self, sender_address, index):
        """Method that deletes an email from the inbox."""
        for email in self.emails:
            if email.from_address == sender_address:
                if index == 0:
                    self.emails.remove(email)
                    return
                else:
                    index -= 1
        raise IndexError("Email not found.")


usage_message = """
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
"""

inbox = Inbox()
# adding some emails to the inbox
inbox.add_email("example1@example.com", "Subject 1", "Email contents 1")
inbox.add_email("example1@example.com", "Subject 1", "Email contents 1.1")
inbox.add_email("example2@example.com", "Subject 2", "Email contents 2")
inbox.add_email("example3@example.com", "Subject 3", "Email contents 3")

user_choice = ""

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")
        # Creating a new Email object
        email = Email(sender_address, subject_line, contents)

        # Adding a new email to the inbox
        inbox.add_email(sender_address, subject_line, contents)
        # Print a success message
        print("Email has been added to inbox.")

    elif user_choice == "l":
        # List all emails from a sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Print all emails from this sender
        print(inbox.list_messages_from_sender(sender_address))

    elif user_choice == "r":
        # Read an email
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Print all emails from the sender with indexes
        print(inbox.list_messages_from_sender(sender_address))

        # Ask the user for the index of the email they wish to read
        index = int(
            input("Please enter the index of the email that you would like to read\n:")
        )

        # Display the email selected
        print(inbox.get_email(sender_address, index))

    elif user_choice == "m":
        # Mark an email as spam
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Show emails from the sender with indexes
        print(inbox.list_messages_from_sender(sender_address))
        # Ask the user for the index of the email to be marked as spam
        index = int(
            input("Please enter the index of the email to be marked as spam\n:")
        )
        # Mark the email as spam
        inbox.mark_as_spam(sender_address, index)
        # Print a success message
        print("Email marked as spam.")

    elif user_choice == "gu":
        # List all unread emails
        print(inbox.get_unread_emails())

    elif user_choice == "gs":
        # List all spam emails
        print(inbox.get_spam_emails())

    elif user_choice == "d":
        # Delete an email
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Show emails from the sender with indexes
        print(inbox.list_messages_from_sender(sender_address))
        # Ask the user for the index of the email they wish to delete
        index = int(input("Please enter the index of the email to be deleted\n:"))
        # Delete the selected email
        inbox.delete(sender_address, index)
        # Print a success message
        print("Email has been deleted.")

    elif user_choice == "e":
        # Exit the program
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input")
