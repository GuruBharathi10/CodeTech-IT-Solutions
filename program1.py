import random
import string

def generate_password(length, complexity):
    if complexity not in ["easy", "medium", "hard"]:
        raise ValueError("Invalid complexity level. Please choose from 'easy', 'medium', or 'hard'.")

    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:  # hard
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter the desired password length: "))
        complexity = input("Enter the desired complexity level (easy/medium/hard): ").lower()
        return length, complexity
    except ValueError:
        print("Invalid input. Please enter a valid integer for length.")
        return get_user_input()

def main():
    print("Welcome to the Secure Password Generator!")

    length, complexity = get_user_input()
    password = generate_password(length, complexity)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
