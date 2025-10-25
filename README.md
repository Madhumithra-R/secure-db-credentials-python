# 🔒 Secure DB Connection Framework (Python & MySQL)

A robust utility demonstrating a **secure, production-ready** methodology for handling sensitive database credentials in Python applications using encryption and environment variables.

---

## ✨ Features

* **Encryption at Rest:** Uses the **Fernet** symmetric encryption scheme from the `cryptography` library to store the database password in an encrypted format.
* **Print/Log Protection:** Implements a custom **`FakeStr` class** to mask the plaintext password as `****` if it is accidentally printed or logged at runtime.
* **Zero-Trust Key Management:** The decryption key (`secret.key`) is generated locally and is **excluded from Git** via `.gitignore`, ensuring your system remains secure.
* **External Configuration:** Reads non-secret connection parameters (`host`, `user`, `database`) from **Environment Variables** (`os.getenv`), preventing hardcoding.

---

## 🛠️ Technologies

* 💻 **Python 3**
* 🐘 **MySQL** (Database)
* 🔐 `cryptography` (for Fernet Encryption)
* 🔗 `mysql-connector-python` (Database Driver)

---

## 🚀 How to Run the Project (The Setup)

**⚠️ IMPORTANT:** The encryption key (`secret.key`) and the raw password script (`encrypt_once.py`) are deliberately missing from this public repository for security. A new user must perform a one-time setup to generate these files locally.

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/Madhumithra-R/secure-db-credentials-python.git
cd secure-db-credentials-python

pip install cryptography mysql-connector-python
```

---

### 2. Generate Key and Encrypted Password

You must recreate the `encrypt_once.py` script locally to generate your unique encryption key and the resulting encrypted password.

1. **Create the file** `encrypt_once.py` in your project folder.  
2. **Replace** `"YOUR_REAL_MYSQL_PASSWORD"` with your actual database password.  
3. **Run the script** once.

<details>
<summary>Click to view <code>encrypt_once.py</code> code</summary>

```python
from cryptography.fernet import Fernet

def generate_key():
    """Generates a Fernet key and saves it to 'secret.key'."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("Key saved to 'secret.key'")

def encrypt_password(password):
    """Loads the key and encrypts the provided password."""
    key = open("secret.key", "rb").read()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    print("\nEncrypted password to copy:")
    print(encrypted)
    return encrypted

if __name__ == "__main__":
    # 🛑 UNCOMMENT THIS LINE ONLY FOR THE FIRST RUN! 🛑
    # generate_key() 

    # REPLACE THIS WITH YOUR REAL MYSQL PASSWORD
    encrypt_password("YOUR_REAL_MYSQL_PASSWORD") 
```

</details>

**Execute the setup:**

```bash
python encrypt_once.py
```

This will output your **Encrypted password (e.g., `b'gAAAAABo_...=='`)** and create the **`secret.key`** file.

---

### 3. Insert the Encrypted Secret

Copy the encrypted output from your console and paste this output into the placeholder line in **`password_utils.py`**:

```python
# password_utils.py

def get_decrypted_password():
    # 🛑 PASTE YOUR UNIQUE ENCRYPTED OUTPUT HERE 🛑
    encrypted_password = b'PASTE_YOUR_ENCRYPTED_OUTPUT_HERE' 
    return decrypt_password(encrypted_password)
```

---

### 4. Set Connection Environment Variables

Set the environment variables in your terminal before running the script:

**Example (Linux/macOS):**

```bash
export DB_HOST=localhost
export DB_USER=root
export DB_NAME=test
```

**Example (Windows PowerShell):**

```powershell
setx DB_HOST "localhost"
setx DB_USER "root"
setx DB_NAME "test"
```

---

### 5. Run the Main Application

Execute the final script:

```bash
python mysql_connect_safe.py
```

**Expected Output (if successful):**

```
Connected to MySQL securely.
Inserted 1 record. Total rows affected: 1
...
Connection closed.
```

---

## 🧠 Why This Matters

This framework demonstrates **industry-grade best practices** for secret handling and database security in Python projects.  
It helps developers move away from insecure patterns like hardcoded passwords and plaintext credentials.

---

## 📂 Repository Structure

```
secure-db-credentials-python/
│
├── encrypt_once.py          # (Create locally – not in repo)
├── password_utils.py        # Decrypts stored encrypted password
├── mysql_connect_safe.py    # Main script for secure MySQL connection
├── secret.key               # (Generated locally – excluded via .gitignore)
├── .gitignore               # Ensures sensitive files aren’t committed
└── README.md                # Documentation
```

---

## 🛡️ Security Notes

* Never push your **`secret.key`** or **plaintext password** to GitHub.  
* Regenerate your encryption key and re-encrypt your password if compromised.  
* Always store environment variables using a secure manager like **.env files**, **Docker secrets**, or **AWS Secrets Manager**.

---

## 🧑‍💻 Author

**Madhumithra R**  
📧 [GitHub Profile](https://github.com/Madhumithra-R)

> “Security isn’t a feature — it’s a foundation.”
