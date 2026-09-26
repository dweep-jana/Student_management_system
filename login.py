import getpass
from database import get_connection


def login():
    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = getpass.getpass("Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:
        print("\nLogin successful!")
        return True

    print("\nInvalid username or password!")
    return False