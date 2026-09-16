# Task 1. Clean name
"""
def clean_name(name):
    if not isinstance(name, str):
        raise TypeError("Type is not a string")
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("The name cant be empty")

    return name.strip().title()

print(clean_name(" anna smith "))
print(clean_name("DAVID COHEN"))
print(clean_name(""))
print(clean_name(22))

#======================================================

# Task 2. Normalize an Email
def normalize_email(email):
    if not isinstance(email, str):
        raise TypeError("Type is not a string")
    cleaned = email.strip()
    if not cleaned:
        raise ValueError("The name cant be empty")
    return email.strip().lower()

print(normalize_email(""))
print(normalize_email(22))
print(normalize_email("NicoleShefer@Example.COM"))

#======================================================

# Task 3. Check a File Name

def function_is_python_name(filename):
    if not isinstance(filename, str):
        raise TypeError("Type is not a string")
    cleaned = filename.strip()
    if not cleaned:
        raise ValueError("The name cant be empty")
    return filename.lower().endswith(".py")

print(function_is_python_name("HOMEWORK.PY"))
print(function_is_python_name("NicoleShefer.com"))
print(function_is_python_name(222))

#======================================================

# Task 4. Replace Words

def fix_message(message):
    if not isinstance(message, str):
        raise TypeError("Type is not a string")
    cleaned = message.strip()
    if not cleaned:
        raise ValueError("The name cant be empty")
    return message.strip().replace(" bad ", " good ")

print(fix_message("bad weather, bad mood"))
print(fix_message(" "))
print(fix_message(22222))

#======================================================

# Task 5. Count a Letter

def count_letter(letter, text):
    if not isinstance(letter, str):
        raise TypeError("Type is not a string")
    cleaned = letter.strip()
    if not cleaned:
        raise ValueError("The name cant be empty")
    return text.count(cleaned)
print(count_letter(" r ", "programming"))
print(count_letter(" i ", "Mississippi"))
print(count_letter("   ", "  "))
print(count_letter(3, 4))

#======================================================

# Task 6. Create a Short Login
def create_login(first_name, last_name):
    if not isinstance(first_name, str):
        raise TypeError("Type is not a string")
    if not isinstance(last_name, str):
        raise TypeError("Type is not a string")

    cleaned = first_name.strip().lower() + "." + last_name.strip().lower()

    if not cleaned:
        raise ValueError("The name cant be empty")

    if not cleaned:
        raise ValueError("The name cant be empty")
    return cleaned

print(create_login(" Anna ", "SMITH"))

"""












