from database import get_connection

from validation import (
    validate_name,
    validate_age,
    validate_email,
    validate_phone,
    validate_course
)


def add_student():

    print("\n========== ADD STUDENT ==========")

    while True:
        name = input("Enter Name: ")

        if validate_name(name):
            break

        print("Invalid name! Enter letters only.")

    while True:
        age = input("Enter Age: ")

        if validate_age(age):
            age = int(age)
            break

        print("Invalid age! Enter age between 1 and 100.")

    while True:
        course = input("Enter Course: ")

        if validate_course(course):
            break

        print("Course cannot be empty.")

    while True:
        email = input("Enter Email: ")

        if validate_email(email):
            break

        print("Invalid email!")

    while True:
        phone = input("Enter Phone: ")

        if validate_phone(phone):
            break

        print("Invalid phone number!")


    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, age, course, email, phone)
        VALUES (?, ?, ?, ?, ?)
    """, (name, age, course, email, phone))

    conn.commit()
    conn.close()

    print("\nStudent added successfully!")

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    if not students:
        print("\nNo students found.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:

        print("\nID      :", student[0])
        print("Name    :", student[1])
        print("Age     :", student[2])
        print("Course  :", student[3])
        print("Email   :", student[4])
        print("Phone   :", student[5])

        print("---------------------------------")

def search_student():

    student_id = input("\nEnter Student ID: ")

    if not student_id.isdigit():
        print("Invalid ID!")
        return

    student_id = int(student_id)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    if student:

        print("\n========== STUDENT FOUND ==========")

        print("ID      :", student[0])
        print("Name    :", student[1])
        print("Age     :", student[2])
        print("Course  :", student[3])
        print("Email   :", student[4])
        print("Phone   :", student[5])

    else:

        print("\nStudent not found!")

def update_student():

    student_id = input("\nEnter Student ID: ")

    if not student_id.isdigit():
        print("Invalid ID!")
        return

    student_id = int(student_id)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:

        print("\nStudent not found!")

        conn.close()
        return


    print("\nEnter new information:")

    # Name
    while True:

        name = input("Name: ")

        if validate_name(name):
            break

        print("Invalid name!")


    # Age
    while True:

        age = input("Age: ")

        if validate_age(age):

            age = int(age)
            break

        print("Invalid age!")


    # Course
    while True:

        course = input("Course: ")

        if validate_course(course):
            break

        print("Course cannot be empty!")


    # Email
    while True:

        email = input("Email: ")

        if validate_email(email):
            break

        print("Invalid email!")


    # Phone
    while True:

        phone = input("Phone: ")

        if validate_phone(phone):
            break

        print("Invalid phone number!")


    cursor.execute("""
        UPDATE students
        SET name = ?,
            age = ?,
            course = ?,
            email = ?,
            phone = ?
        WHERE id = ?
    """, (
        name,
        age,
        course,
        email,
        phone,
        student_id
    ))

    conn.commit()
    conn.close()

    print("\nStudent updated successfully!")

def delete_student():

    student_id = input("\nEnter Student ID: ")

    if not student_id.isdigit():

        print("Invalid ID!")
        return

    student_id = int(student_id)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:

        print("\nStudent deleted successfully!")

    else:

        print("\nStudent not found!")

    conn.close()

def student_menu():

    while True:

        print("""
========================================
       STUDENT MANAGEMENT SYSTEM
========================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Logout

========================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            print("\nLogged out successfully!")
            break

        else:

            print("\nInvalid choice!")