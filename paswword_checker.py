import re

def assess_password_strength(password):
    # Initialize the strength score
    strength_score = 0
    feedback = []

    # Check the length of the password
    length = len(password)
    if length >= 8:
        strength_score += 2
        feedback.append("Password length is sufficient.")
    else:
        feedback.append("Password is too short. Consider using at least 8 characters.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
        feedback.append("Password contains uppercase letters.")
    else:
        feedback.append("Consider adding uppercase letters to your password.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
        feedback.append("Password contains lowercase letters.")
    else:
        feedback.append("Consider adding lowercase letters to your password.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += 1
        feedback.append("Password contains numbers.")
    else:
        feedback.append("Consider adding numbers to your password.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 2
        feedback.append("Password contains special characters.")
    else:
        feedback.append("Consider adding special characters to your password.")

    # Determine the overall strength of the password
    if strength_score <= 3:
        feedback.append("Overall strength: Weak")
    elif strength_score <= 5:
        feedback.append("Overall strength: Moderate")
    else:
        feedback.append("Overall strength: Strong")

    return "\n".join(feedback)

# Example usage:
password = input("Enter a password to assess: ")
print(assess_password_strength(password))

