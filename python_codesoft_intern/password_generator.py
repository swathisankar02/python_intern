import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Combine all character sets
    all_chars = letters + digits + special_chars
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    # Prompt user for password length
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        print(e)
        return
    
    # Generate the password
    password = generate_password(password_length)
    
    # Display the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
