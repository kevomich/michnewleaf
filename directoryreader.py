import os

# Specify the directory path (use "." for current directory)
directory_path = r"C:\Users\Kelvin\Downloads\Programs"

try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception:
    print("out of context")



