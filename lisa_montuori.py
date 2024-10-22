# decode and main function by Lisa Montuori


def encode(password):
    """Encodes a password by shifting each digit up by 3."""
    encoded_password = ''
    for char in password:
        if char.isdigit():  # Ensure we only process digits
            new_digit = (int(char) + 3) % 10  # Shift digit and wrap around using modulo
            encoded_password += str(new_digit)
    return encoded_password

def decode(password):
    """Decodes a password by shifting each digit down by 3."""
    decoded_password = ''
    for char in password:
        if char.isdigit():
            new_digit = (int(char) - 3) % 10
            decoded_password += str(new_digit)
    return decoded_password

def main():
    while True:
        print("Menu")
        print("-" * 15)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode (8 digits): ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
                print(f"Encoded Password: {encoded_password}")
            else:
                print("Invalid input. Please enter an 8-digit password containing only integers.")

        elif option == '2':
            encoded_password = input("Please enter your encoded password to decode: ")
            if len(encoded_password) == 8 and encoded_password.isdigit():
                decoded_password = decode(encoded_password)
                print("Your password has been decoded!")
                print(f"Decoded Password: {decoded_password}")
            else:
                print("Invalid input. Please enter an 8-digit encoded password containing only integers.")

        elif option == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
