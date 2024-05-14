#Task 1:


import re

def extract_emails(filename):
    try:
        # Open file and read ontents
        with open(filename, 'r') as file:
            text = file.read()

        # Use regex to find all email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)

        # Print the unique email addresses
        unique_emails = set(emails)
        print("Unique email addresses found in the file:")
        for email in unique_emails:
            print(email)
    
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied to access file.")

# Provide filename as input
filename = input("Enter the filename (with path if not in the same directory): ")

# Extract emails
extract_emails(filename)
