import random
import string

def generate_password(length):
    # Define the character sets to use for the password
    characters = string.ascii_letters + string.digits
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


    # Prompt the user to specify the length of the password
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Generate and display the password
password = generate_password(length)
print("Generated password:", password)

