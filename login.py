import getpass
from database import get_connection


def register():

    print("\n========== REGISTER ==========")

    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty!")
        return

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")

    if not password:
        print("Password cannot be empty!")
        return

    if password != confirm_password:
        print("Passwords do not match!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    # Check username already exists
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        print("Username already exists!")
        conn.close()
        return

    # Insert new user
    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
    """, (username, password))

    conn.commit()
    conn.close()

    print("\nRegistration successful!")
    print("You can now login.")


def login():

    while True:

        print("""
========================================
                LOGIN
========================================

1. Login
2. Register
3. Exit

========================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":

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

            else:
                print("\nInvalid username or password!")

        elif choice == "2":

            register()

        elif choice == "3":

            print("\nThank you for using Student Management System!")
            return False

        else:

            print("\nInvalid choice!")