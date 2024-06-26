from encrypt_decrypt.encrypt_decrypt import encrypt, decrypt

# Test cases for encrypt function
def test_encrypt_basic():
    """
    Test case for encrypting a basic plaintext string.

    Checks that the encrypt function correctly encrypts the string 'hello' with
    a key of 3, resulting in 'khoor'.
    """
    plaintext = "hello"
    encryption_key = 3
    expected_encrypted_text = "khoor"
    
    encrypted_text = encrypt(plaintext, encryption_key)
    assert encrypted_text == expected_encrypted_text

def test_encrypt_empty_string():
    """
    Test case for encrypting an empty string.

    Checks that the encrypt function correctly returns an empty string when encrypting
    an empty input with a key of 5.
    """
    plaintext = ""
    encryption_key = 5
    expected_encrypted_text = ""
    
    encrypted_text = encrypt(plaintext, encryption_key)
    assert encrypted_text == expected_encrypted_text

def test_encrypt_long_text():
    """
    Test case for encrypting a long plaintext string.

    Checks that the encrypt function correctly encrypts the given long text with
    a key of 7, matching the expected encrypted output.
    """
    plaintext = "This is a long text to test encryption with a large number of characters."
    encryption_key = 7
    expected_encrypted_text = "[opz'pz'h'svun'{l {'{v'{lz{'lujy!w{pvu'~p{o'h'shynl'u|tily'vm'johyhj{lyz5"
    
    encrypted_text = encrypt(plaintext, encryption_key)
    assert encrypted_text == expected_encrypted_text
    
# Test cases for decrypt function
def test_decrypt_basic():
    """
    Test case for decrypting a basic cipher text.

    Checks that the decrypt function correctly decrypts the cipher text 'khoor'
    with a key of 3, resulting in 'hello'.
    """
    cipher_text = "khoor"
    decryption_key = 3
    expected_decrypted_text = "hello"
    
    decrypted_text = decrypt(cipher_text, decryption_key)
    assert decrypted_text == expected_decrypted_text

def test_decrypt_empty_string():
    """
    Test case for decrypting an empty cipher text.

    Checks that the decrypt function correctly returns an empty string when decrypting
    an empty input with a key of 5.
    """
    cipher_text = ""
    decryption_key = 5
    expected_decrypted_text = ""
    
    decrypted_text = decrypt(cipher_text, decryption_key)
    assert decrypted_text == expected_decrypted_text

def test_decrypt_long_text():
    """
    Test case for decrypting a long cipher text.

    Checks that the decrypt function correctly decrypts the given long encrypted text
    with a key of 7, matching the expected decrypted output.
    """
    encrypted_text = "[opz'pz'h'svun'{l {'{v'{lz{'lujy!w{pvu'~p{o'h'shynl'u|tily'vm'johyhj{lyz5"
    decryption_key = 7
    expected_decrypted_text = "This is a long text to test encryption with a large number of characters."
    
    decrypted_text = decrypt(encrypted_text, decryption_key)
    assert decrypted_text == expected_decrypted_text