import random
import string

# Ask the user for the password length
while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length > 0:
            break
        else:
            print("Length must be a positive number.")
    except ValueError:
        print("Please enter a valid number.")

# Ask if the user wants special characters
use_specials = input("Include special characters? (yes/no): ").strip().lower()
include_specials = use_specials == 'yes'

# Create the character set
characters = string.ascii_letters + string.digits  #To be able to take both letters (lowercase and uppercase) and numbers
if include_specials:
    characters += string.punctuation  # Adds special characters using a punctuation variable

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length)) #random.choice(characters) : We call the imported random command to pick a choice from the characters format we created
                                                        #for _ in range(length): Make a for loop for the random sellection for each space within the range/length given
# Display the password
print("\nYour random password is:")
print(password)
