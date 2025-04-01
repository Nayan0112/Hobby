import json

STUDENT_DATA_FILE = "student_data.json"
TEACHER_DATA_FILE = "teacher_data.json"
USER_DATA_FILE = "user_data.json"

class DataBase:
    def __init__(self, user_file=USER_DATA_FILE):
        self.user_file = user_file

    def load_users(self):
        try:
            with open(self.user_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError):
            return {}

    def save_users(self, users):
        with open(self.user_file, "w") as file:
            json.dump(users, file, indent=4)

    def authenticate_user(self, username, password):
        users = self.load_users()
        if username in users and users[username]["password"] == password:
            print("Login successful.")
            return users[username]["role"]
        else:
            print("Invalid credentials.")
            return None

    def load_data(self, data_file):
        try:
            with open(data_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError):
            return {}

    def save_data(self, data_file, data):
        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

    def available_courses(self):
        course_name = []
        teachers = self.load_data(TEACHER_DATA_FILE)
        for teacher, courses in teachers.items():
            print(f"{teacher}")
            for course in courses.keys() :
                course_name.append(course)
                print(f"    |{course}")
        return course_name

class TeacherDB(DataBase):
    def __init__(self):
        super().__init__()
        self.teacher_data = TEACHER_DATA_FILE
        self.student_data = STUDENT_DATA_FILE

    def view_students(self, teacher_name):
        students = self.load_data(self.student_data)
        teachers = self.load_data(self.teacher_data)

        teacher_courses = teachers[teacher_name] 
        if not teacher_courses:
            print("You have no courses.")
            return

        print(f"\nStudents enrolled in your courses:")

        course_found = False
        for course in teacher_courses:
            enrolled_students = [student for student, courses in students.items() if course in courses]
            
            if enrolled_students:
                print(f"\nCourse: {course}")
                for student in enrolled_students:
                    print(f"    |{student}")
                course_found = True

        if not course_found:
            print("No students are in your courses.")


    def add_student(self, name, course, teacher):
        students = self.load_data(self.student_data)
        teachers = self.load_data(self.teacher_data)

        if teacher not in teachers or course not in teachers[teacher]:
            print("Course not found!")
            return

        if name in students:
            if course not in students[name]:
                students[name][course] = -1  
                self.save_data(self.student_data, students)
                print("Student added successfully!")
            else:
                print(f"{name} is already registered in {course}")
        else:
            print("Student not found!")

    def remove_student(self, name, course, teacher):
        students = self.load_data(self.student_data)

        if name in students:
            if course in students[name] and course in self.load_data(self.teacher_data).get(teacher):
                del students[name][course]
                self.save_data(self.student_data, students)
                print(f"Student {name} removed successfully.")
            else:
                print("Course not found for this student.")
        else:
            print("Student not found.")

    def register_user(self, username, password, role="teacher"):
        users = self.load_users()
        teachers = self.load_data(self.teacher_data)

        if username in users:
            print("Username already exists.")
            return

        users[username] = {"password": password, "role": role}
        teachers[username] = {}

        self.save_data(self.teacher_data, teachers)
        self.save_users(users)
        print("Teacher registered successfully.")

class StudentDB(DataBase):
    def __init__(self):
        super().__init__()
        self.student_data = STUDENT_DATA_FILE

    def register_user(self, username, password, role="student"):
        users = self.load_users()
        students = self.load_data(self.student_data)

        if username in users:
            print("Username already exists.")
            return

        users[username] = {"password": password, "role": role}
        students[username] = {}

        self.save_data(self.student_data, students)
        self.save_users(users)
        print("Student registered successfully.")

    def veiw_courses(self, name) :
        users = self.load_data(self.student_data)
        print("\nRegistered Courses :")
    
        for course in users[name].keys() :
            print(f"{course}")