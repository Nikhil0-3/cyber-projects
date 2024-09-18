import re
import string

# Common passwords list (expand this list as needed)
COMMON_PASSWORDS = {'123456', 'password', '123456789', '12345678', '12345', 'password1', '1234567'}

def check_length(password):
    return len(password) >= 8

def check_complexity(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special

def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def check_predictability(password):
    # Example: Check for sequences or repeated characters
    return not (re.search(r'(\d)\1{2,}', password) or  # Repeated digits
                re.search(r'(abc|123|qwerty|password)', password, re.IGNORECASE))  # Simple sequences

def analyze_password(password):
    results = {
        'length_ok': check_length(password),
        'complexity_ok': check_complexity(password),
        'common_password': check_common_password(password),
        'predictability_ok': check_predictability(password)
    }

    return results

def recommend_password(password):
    recommendations = []
    results = analyze_password(password)

    if not results['length_ok']:
        recommendations.append("Password should be at least 8 characters long.")
    
    if not results['complexity_ok']:
        recommendations.append("Password should include uppercase, lowercase, digits, and special characters.")
    
    if results['common_password']:
        recommendations.append("Password is too common. Choose a more unique password.")
    
    if not results['predictability_ok']:
        recommendations.append("Password is too predictable. Avoid using simple sequences or repeated characters.")
    
    if not recommendations:
        recommendations.append("Password is strong and secure.")

    return recommendations

if __name__ == "__main__":
    password = input("Enter the password to analyze: ")
    recommendations = recommend_password(password)
    for recommendation in recommendations:
        print(recommendation)
