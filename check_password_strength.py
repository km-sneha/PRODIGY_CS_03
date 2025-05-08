import re

# Function to check password complexity
def check_password_strength(password):
    feedback = []
    score = 0  # Start with 0 score

    # Check password length (at least 8 characters)
    if len(password) >= 8:
        score += 2
        feedback.append("Length: Good (8+ characters).")
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Check for at least one uppercase letter
    if any(char.isupper() for char in password):
        score += 2
        feedback.append("Uppercase: Present.")
    else:
        feedback.append("Password must contain at least one uppercase letter.")

    # Check for at least one lowercase letter
    if any(char.islower() for char in password):
        score += 2
        feedback.append("Lowercase: Present.")
    else:
        feedback.append("Password must contain at least one lowercase letter.")

    # Check for at least one digit
    if any(char.isdigit() for char in password):
        score += 2
        feedback.append("Number: Present.")
    else:
        feedback.append("Password must contain at least one number.")

    # Check for at least one special character
    special_chars = '!@#$%^&*()_+[]{}|;:,.<>?/~`'
    if any(char in special_chars for char in password):
        score += 2
        feedback.append("Special Character: Present.")
    else:
        feedback.append("Password must contain at least one special character.")

    # Blacklist check (common passwords)
    common_passwords = ['123456', 'password', 'qwerty', '123456789', 'abc123', 'letmein']
    if password.lower() in common_passwords:
        feedback.append("This password is too common. Choose a more secure one.")
    else:
        score += 1  # Add a point for not using a common password

    # Evaluate password strength based on the score
    if score == 10:
        strength = "Strong"
        color = "\033[92m"  # Green for strong
    elif 7 <= score < 10:
        strength = "Moderate"
        color = "\033[93m"  # Yellow for moderate
    else:
        strength = "Weak"
        color = "\033[91m"  # Red for weak

    # Output the feedback
    print("\nPassword Strength Evaluation:")
    for line in feedback:
        print(f"- {line}")
    
    # Display strength in color
    print(f"{color}Overall Strength: {strength}\033[0m")
    
    # Suggestions for improving the password
    if strength == "Weak":
        print("\nSuggestions to improve your password:")
        if len(password) < 8:
            print("- Increase the length to at least 8 characters.")
        if not any(char.isupper() for char in password):
            print("- Add at least one uppercase letter.")
        if not any(char.isdigit() for char in password):
            print("- Add at least one number.")
        if not any(char in special_chars for char in password):
            print("- Add at least one special character.")
        if password.lower() in common_passwords:
            print("- Choose a more unique password. Avoid common passwords.")

# Function to get user input and check password
def get_password_input():
    print("Welcome to the Enhanced Password Complexity Checker!\n")
    password = input("Enter your password: ")

    # Validate password
    print("\nChecking your password...")
    check_password_strength(password)

# Run the program
get_password_input()

# Run the program
get_password_input()
input("\nPress Enter to exit...")

