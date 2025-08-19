def encrypt_caesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            base = ord('A') if char.isupper() else ord('a')  # ASCII base
            # Shift character within alphabet range
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters stay the same
    return encrypted_text

def decrypt_caesar(text, shift):
    # Decryption is just encryption with negative shift
    return encrypt_caesar(text, -shift)

def main():
    print("==== Caesar Cipher Encryption and Decryption ====")
    message = input("Enter your message: ")
    
    # Validate shift input
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift.")

    # Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()

    if choice == 'e':
        encrypted = encrypt_caesar(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'd':
        decrypted = decrypt_caesar(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
