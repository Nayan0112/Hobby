import json

DATA_FILE = "data.json"
INFO_FILE = "info.json"

class Database:
    def __init__(self):
        self.data_file = DATA_FILE
        self.user_file = INFO_FILE

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self, data):
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_users(self):
        try:
            with open(self.user_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self, users):
        with open(self.user_file, "w") as file:
            json.dump(users, file, indent=4)

    def register_user(self, username, password, role):
        users = self.load_users()
        users_data = self.load_data()
        if username in users:
            print("Username already exists.")
            return

        users[username] = {"password": (password), "role": role}
        users_data[username] = {}
        self.save_data(users_data)
        self.save_users(users)
        print("User registered successfully.")

    def authenticate_user(self, username, password):
        users = self.load_users()
        if username in users and users[username]["password"] == (password):
            print("Login successful.")
            return users[username]["role"]
        else:
            print("Invalid credentials.")
            return None

    def add_student(self, name, course, teacher):

       users = self.load_data()
       if course not in users[teacher] :
            print("Course not found!")
            return
       if name in users :
            if course not in users[name]:
                users[name][course] = 0  
                self.save_data(users)
                print("Student added successfully!")
            else:
                print(f"{name} is already registered in the {course}")
       else :
            print("Student not found!")

    def remove_student(self, name, course, teacher):

        students = self.load_data()
        if name in students:
            if course in students[name].values() and students[teacher].values() :
                del students[name][course]
                self.save_data(students)
                print(f"Student {name} removed successfully.")
        else:
            print("Student not found.")
