import mysql.connector
from password_utils import get_decrypted_password
import os # 👈 1. IMPORT OS: Allows reading environment variables

def connect_to_mysql():
    db_password = get_decrypted_password() 
    conn = None # Initialized for robust finally block
    cursor = None # Initialized for robust finally block
    
    try:
        conn = mysql.connector.connect(
            # 2. USE OS.GETENV: Reads variable from the environment or uses default fallback
            host=os.getenv("DB_HOST", "localhost"),   # Default to 'localhost' if DB_HOST is not set
            user=os.getenv("DB_USER", "root"),       # Default to 'root' if DB_USER is not set
            password=db_password, 
            database=os.getenv("DB_NAME", "test")    # Default to 'test' if DB_NAME is not set
        )
        print("Connected to MySQL securely.") 
        
        # -----------------------------------------------------------------
        # 🟢 START: Database logic (Wrapped in inner try/finally) 🟢
        # -----------------------------------------------------------------
        
        cursor = conn.cursor() 
        
        try:
            # 1A. Create a sample table if it doesn't exist
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                email VARCHAR(255)
            )
            """
            cursor.execute(create_table_sql)

            # 2. INSERT Data (Modifying data requires conn.commit())
            insert_sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
            data_to_insert = ("Zara_Secure", "secure@example.com")
            cursor.execute(insert_sql, data_to_insert)
            conn.commit()
            print(f"Inserted 1 record. Total rows affected: {cursor.rowcount}")

            # 3. SELECT Data (Reading data does not require conn.commit())
            select_sql = "SELECT id, username FROM users WHERE username LIKE 'Zara%'"
            cursor.execute(select_sql)
            
            # Fetch and display the results
            results = cursor.fetchall()
            print("\nFetched Records:")
            for row in results:
                print(f"ID: {row[0]}, Username: {row[1]}")
                
        except mysql.connector.Error as sql_err:
            print(f"SQL Operation Error: {sql_err}")
            
        finally:
            if cursor:
                cursor.close()
        
        # -----------------------------------------------------------------
        # 🔴 END: Database logic 🔴
        # -----------------------------------------------------------------

    except mysql.connector.Error as conn_err:
        # Catches connection-level errors
        print(f"Connection Error: {conn_err}")
        
    finally:
        # Close the connection
        if conn and conn.is_connected():
            conn.close()
            print("\nConnection closed.")

if __name__ == "__main__":
    connect_to_mysql()