def validate_name(name):
    """
    Check whether name is valid.
    Name should not be empty and should contain only letters and spaces.
    """

    name = name.strip()

    if not name:
        return False

    if not all(char.isalpha() or char.isspace() for char in name):
        return False

    return True

def validate_age(age):
    """
    Check whether age is valid.
    """

    if not age.isdigit():
        return False

    age = int(age)

    if age < 1 or age > 100:
        return False

    return True

def validate_email(email):
    """
    Basic email validation.
    """

    email = email.strip()

    if "@" not in email:
        return False

    if "." not in email:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    return True

def validate_phone(phone):
    """
    Check Indian 10-digit phone number.
    """

    phone = phone.strip()

    if not phone.isdigit():
        return False

    if len(phone) != 10:
        return False

    if phone[0] not in "6789":
        return False

    return True

def validate_course(course):
    """
    Check whether course is empty.
    """

    course = course.strip()

    if not course:
        return False

    return True