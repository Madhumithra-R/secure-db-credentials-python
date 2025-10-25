from cryptography.fernet import Fernet

# Custom string class to prevent accidental print/log leaks
class FakeStr(str):
    def __str__(self):
        return "****" # Returns **** when explicitly printed
    
    def __repr__(self):
        return "****" # Returns **** in logging or interactive shells

def load_key():
    """Loads the Fernet key from the local 'secret.key' file."""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        # Handle case where key is missing (e.g., deleted or not generated)
        print("Error: 'secret.key' not found. Run encrypt_once.py first.")
        raise

def decrypt_password(encrypted_password):
    """Decrypts the password using the loaded key and returns a FakeStr instance."""
    key = load_key()
    f = Fernet(key)
    # Decrypt the bytes and decode to a string
    decrypted = f.decrypt(encrypted_password).decode()
    # Wrap the decrypted password in FakeStr for print-safety
    return FakeStr(decrypted)

def get_decrypted_password():
    """Main utility function to retrieve the decrypted and protected password."""
    # ** STEP 2: PASTE THE ENCRYPTED OUTPUT HERE (e.g., b'gAAAAABm...==') **
    encrypted_password = b'PASTE_YOUR_ENCRYPTED_OUTPUT_HERE'
    return decrypt_password(encrypted_password)