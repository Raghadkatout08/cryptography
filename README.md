# cryptography

This repository contains a simple implementation of encryption and decryption functions using a Caesar cipher technique. The project structure is organized as follows:

```
cryptography/
├── .venv
├── encrypt_decrypt
│ ├── init.py
│ ├── encrypt_decrypt.py # Contains encrypt and decrypt functions
├── test_encrypt_decrypt
│ ├── init.py
│ ├── test_encrypt_decrypt.py # Contains pytest test cases
├── .gitignore
├── README.md # Project README file
├── requirements.txt # Python dependencies
```

### Encryption and Decryption Functions

The `encrypt` and `decrypt` functions utilize a simple Caesar cipher technique to transform plaintext into ciphertext and vice versa. The `encrypt` function shifts each character in the plaintext forward by a specified key, while the `decrypt` function reverses this process by shifting each character backwards.

## Testing
The project includes test cases using pytest to validate the correctness of the encryption and decryption functions. To run the tests, make sure you have `pytest` installed: ```pip install pytest```


## Setup
1. Clone the repository:
- `git clone git@github.com:Raghadkatout08/cryptography.git`
- `cd cryptography`

2. Create and activate a virtual environment (optional but recommended):
- `python -m venv .venv`
- `source .venv/bin/activate`

3. Install dependencies:
- `pip install -r requirements.txt`

4. Run the tests:
- `pytest`