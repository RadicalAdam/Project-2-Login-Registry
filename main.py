import csv_handler
import gui
import hashlib
import os

def validate_login(username, password):
    csv_path = os.path.join(os.path.dirname(__file__), 'user_data.csv')
    users = csv_handler.read_csv(csv_path)
    for user in users:
        if user['username'] == username and user['password'] == hashlib.sha256(password.encode()).hexdigest():
            return True
    return False

def register_new_user(username, password, email, name):
    csv_path = os.path.join(os.path.dirname(__file__), 'user_data.csv')
    users = csv_handler.read_csv(csv_path)
    for user in users:
        if user['username'] == username:
            return False

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    new_user_data = {
        'username': username,
        'password': hashed_password,
        'email': email,
        'name': name
    }
    csv_handler.write_csv(csv_path, new_user_data)
    return True

def main():
    gui.create_login_and_registration_form(validate_login, register_new_user)

if __name__ == "__main__":
    main()
