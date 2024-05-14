#Task 1:


import os

def list_directory_contents(path):
    try:
        # List all files and subdirectories in given path
        contents = os.listdir(path)
        
        print("Contents of directory:", path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied to access directory.")

# Prompt user for the directory path
directory_path = input("Enter the directory path: ")

# List directory contents
list_directory_contents(directory_path)




#Task 2:


import os

def report_file_sizes(directory):
    try:
        # Iterate through files in directory
        print("File sizes in directory:", directory)
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            # Check if it's a file
            if os.path.isfile(filepath):
                # Get the size of the file
                size = os.path.getsize(filepath)
                print(f"{filename}: {size} bytes")
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied to access directory.")

# Prompt user for the directory path
directory_path = input("Enter the directory path: ")

# Report file sizes
report_file_sizes(directory_path)




#Task 3:


import os

def count_file_extensions(directory):
    try:
        # Create empty dictionary to store file extension counts
        extension_counts = {}

        # Iterate through files in directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            # Is this a file?
            if os.path.isfile(filepath):
                # Get file extension
                _, extension = os.path.splitext(filename)
                # Normalize the extension to lowercase
                extension = extension.lower()
                # Update the extension count
                extension_counts[extension] = extension_counts.get(extension, 0) + 1
        
        # Print the counts
        print("File extension counts in directory:", directory)
        for extension, count in extension_counts.items():
            print(f"{extension.upper()}: {count}")
    
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied to access directory.")

# Prompt user for the directory path
directory_path = input("Enter the directory path: ")

# Count file extensions
count_file_extensions(directory_path)
