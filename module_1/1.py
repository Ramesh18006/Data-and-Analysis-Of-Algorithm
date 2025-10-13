""" Open a text document read the string and print the string in the document.
Handle exceptions accordingly """
try:
    filename = input("Enter the file name (with .txt extension): ")

    file = open(filename, "r")
    content = file.read()

    print("\n--- File Content ---")
    print(content)

    file.close()
except FileNotFoundError:
    print("Error: The file does not exist. Please check the name and try again.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)
