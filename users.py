from getpass import getpass

USERS = {
    "admin":   {"password": "admin123",   "role": "Administrator"},
    "student": {"password": "student123", "role": "Standard User"},
}

current_user = None


def login():
    global current_user
    print("=" * 40)
    print("              MiniOS Login")
    print("=" * 40)

    attempts = 3
    while attempts > 0:
        username = input("\nUsername: ").strip()
        password = getpass("Password: ")

        if username in USERS and USERS[username]["password"] == password:
            current_user = username
            print("\nLogin successful.\n")
            print(f"Welcome, {username}!\n")
            return True

        attempts -= 1
        print(f"Error: Invalid username or password. Attempts left: {attempts}")

    print("\nToo many failed attempts. System locked.")
    return False