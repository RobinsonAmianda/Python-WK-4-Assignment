def file_read_write():
    try:
        #Ask user for filename
        filename = input("Enter the name of the file you want to read: ")

        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()
        file = open(filename, "r")
        

        # Step 3: Modify the content (here we convert it to uppercase)
        modified_content = content.upper()

        #Create a new file and write content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File has been read successfully and written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
file_read_write()
