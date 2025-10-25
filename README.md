🔒 Secure DB Connection Framework (Python & MySQL)
A robust utility demonstrating a secure, production-ready methodology for handling sensitive database credentials in Python applications using encryption and environment variables.

✨ Features

Encryption at Rest: Uses the Fernet symmetric encryption scheme from the cryptography library to store the database password in an encrypted format.





Print/Log Protection: Implements a custom FakeStr class to mask the plaintext password as **** if it is accidentally printed or logged at runtime.






Zero-Trust Key Management: The decryption key (secret.key) is stored locally and is excluded from Git via .gitignore, ensuring your system remains secure.



External Configuration: Reads non-secret connection parameters (host, user, database) from Environment Variables (os.getenv), preventing hardcoding.

🛠️ Technologies
💻 Python 3 

🐘 MySQL (Database) 


🔐 cryptography (for Fernet Encryption) 


🔗 mysql-connector-python (Database Driver) 

🚀 How to Use (Local Setup)
Because the project stores the necessary secrets locally, a new user must perform a one-time setup to generate their unique encryption key and encrypted password.

1. Clone and Install Dependencies
Bash

git clone https://github.com/Madhumithra-R/secure-db-credentials-python.git
cd secure-db-credentials-python

pip install cryptography mysql-connector-python
2. Generate Key and Encrypted Password
You must run the encrypt_once.py script locally to generate your unique decryption key and encrypted password.

Replace the placeholder in encrypt_once.py with your actual MySQL password.

Uncomment the generate_key() line.

Run the script:

Bash

# This creates the necessary 'secret.key' file and outputs the encrypted password
python encrypt_once.py
Copy the entire outputted encrypted string (e.g., b'gAAAAABo_JlK...').

3. Insert the Encrypted Secret
Open password_utils.py and paste the string you just copied into the encrypted_password variable:

Python

# password_utils.py

def get_decrypted_password():
    # PASTE YOUR UNIQUE ENCRYPTED OUTPUT HERE
    encrypted_password = b'PASTE_YOUR_ENCRYPTED_OUTPUT_HERE' 
    return decrypt_password(encrypted_password)
4. Set Connection Environment Variables
The mysql_connect_safe.py file uses environment variables to configure the connection. Set these variables in your terminal before running the script (or use a local .env file):

Example (Linux/macOS):

Bash

export DB_HOST=localhost
export DB_USER=root
export DB_NAME=test
5. Run the Application
Execute the main connection script. It will use the environment variables and securely decrypt the password at runtime.

Bash

python mysql_connect_safe.py
Expected Output:

Connected to MySQL securely.
Inserted 1 record. Total rows affected: 1
...
Connection closed.
