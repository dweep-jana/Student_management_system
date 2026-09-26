from database import create_tables
from login import login
from student import student_menu


def main():

    create_tables()

    print("=" * 45)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    if login():

        student_menu()

    else:

        print("Login failed!")


if __name__ == "__main__":
    main()