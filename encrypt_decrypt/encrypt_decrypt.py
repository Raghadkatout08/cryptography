def encrypt(text, key):
    '''
    Encrypts a given plaintext using a Caesar cipher technique.

    Args:
        text (str): The plaintext string to be encrypted.
        key (int): The encryption key to shift characters in the plaintext.

    Returns:
        str: The encrypted ciphertext.
    '''
    encrypted_text = ''.join(chr((ord(c) + key - 32) % 95 + 32) for c in text)
    return encrypted_text

def decrypt(text, key):
    '''
    Decrypts a given ciphertext using a Caesar cipher technique.

    Args:
        text (str): The ciphertext string to be decrypted.
        key (int): The decryption key to shift characters in the ciphertext.

    Returns:
        str: The decrypted plaintext.
    '''
    decrypted_text = ''.join(chr((ord(c) - key - 32) % 95 + 32) for c in text)
    return decrypted_text


# Example Usage:

## Test cases for abc
plaintext = "abc"
encryption_key = 1

encrypted_text = encrypt(plaintext, encryption_key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, encryption_key)
print(f"Decrypted Text: {decrypted_text}") 

## Test cases for hello
plaintext = "hello"
encryption_key = 3

encrypted_text = encrypt(plaintext, encryption_key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, encryption_key)
print(f"Decrypted Text: {decrypted_text}") 


## Test cases for long text
plaintext = "This is a long text to test encryption with a large number of characters."
encryption_key = 7

encrypted_text = encrypt(plaintext, encryption_key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, encryption_key)
print(f"Decrypted Text: {decrypted_text}") 