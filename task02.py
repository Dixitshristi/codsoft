import string
import random

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random choice from the characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user to enter the desired length of the password
        length = int(input("Enter the desired length for the password: "))
        
        # Check if the length is a positive integer
        if length <= 0:
            print("Please enter a positive integer for the password length.")
        else:
            # Generate the password
            password = generate_password(length)
            
            # Display the generated password
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

# Call the main function to execute the program
if _name_ == "_main_":
    main()
