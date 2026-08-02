import os

# Specify the directory path (use "." for current directory)
directory_path = r"C:/Users/Kelvin/Downloads/Documents/DOCS/The%20Ultimate%20Python%20Handbook.pdf"

try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")
