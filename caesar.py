def caesar_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def main():
    message = input("Enter message to encrypt: ")
    key = int(input("Enter key (a number from 1 to 25): "))
    
    encrypted_message = caesar_encrypt(message, key)
    print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
    main()

def caesar_decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    encrypted_message = input("Enter message to decrypt: ")
    key = int(input("Enter key (a number from 1 to 25): "))
    
    decrypted_message = caesar_decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
