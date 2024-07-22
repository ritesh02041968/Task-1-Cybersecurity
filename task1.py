def caesar_cipher(text, shift, direction='encrypt'):
    encrypted_text = []
    shift = shift % 26  # Ensure shift is within the range of 0-25

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')

            if direction == 'encrypt':
                new_char = chr((ord(char) - start + shift) % 26 + start)
            elif direction == 'decrypt':
                new_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                raise ValueError("Direction must be 'encrypt' or 'decrypt'.")

            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_text)

def main():
    while True:
        try:
            choice = input("Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt': ").strip().lower()
            if choice not in ['encrypt', 'decrypt']:
                raise ValueError("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            
            text = input("Enter your message: ").strip()
            shift = int(input("Enter the shift value (a positive integer): "))
            
            if shift <= 0:
                raise ValueError("Shift value must be a positive integer.")

            if choice == 'decrypt':
                shift = -shift  # Invert shift for decryption

            encrypted_message = caesar_cipher(text, shift, direction=choice)
            print(f"The {choice}ed message is: {encrypted_message}")
            
            break  # Exit the loop if everything is processed correctly

        except ValueError as ve:
            print(f"Error: {ve}")
            continue

if __name__ == "__main__":
    main()
