import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    guaranteed_chars = []
    
    if use_lower:
        char_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_upper:
        char_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        char_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))
    
    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars + [random.choice(char_pool) for _ in range(remaining_length)]
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def get_user_input():
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length >= 8:
                break
            print("Length must be at least 8.")
        except ValueError:
            print("Enter a valid number.")
    
    print("\nSelect character types (y/n):")
    use_upper = input("Uppercase (A-Z)? ").lower() == 'y'
    use_lower = input("Lowercase (a-z)? ").lower() == 'y'
    use_digits = input("Numbers (0-9)? ").lower() == 'y'
    use_symbols = input("Symbols (!@#$)? ").lower() == 'y'
    
    if sum([use_upper, use_lower, use_digits, use_symbols]) < 2:
        print("Select at least 2 types.")
        return get_user_input()
    
    return length, use_upper, use_lower, use_digits, use_symbols

def main():
    print("🔐 Password Generator")
    while True:
        length, use_upper, use_lower, use_digits, use_symbols = get_user_input()
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\n✅ Password: {password}")
        if input("\nGenerate another? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()