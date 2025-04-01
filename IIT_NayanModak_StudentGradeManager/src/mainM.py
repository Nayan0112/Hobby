from DataBaseM import TeacherDB, StudentDB
from CreditManagerM import Editor

#main

def main():
    student_db = StudentDB()
    teacher_db = TeacherDB()
    edit = Editor()

    print("STUDENT GRADE MANAGER")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (student/teacher): ").lower()

            if role == "student":
                student_db.register_user(username, password, role)
            elif role == "teacher":
                teacher_db.register_user(username, password, role)
            else:
                print("Invalid role. Choose 'student' or 'teacher'.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            role = student_db.authenticate_user(username, password) or teacher_db.authenticate_user(username, password)
            if role:
                print(f"Welcome {username}! You are logged in as {role}.")
            else:
                continue

            while role:
                if role == "student":
                    print("\n1. View Registered Courses")
                    print("2. View Grades")
                    print("3. Available courses")
                    print("4. Add/Drop Courses")
                    print("5. Logout")

                    usr_choice = input("Enter choice: ")

                    if usr_choice == "1":
                        student_db.veiw_courses(username)

                    elif usr_choice == "2":
                        students = student_db.load_data(student_db.student_data)
                        if username in students:
                            for course, grade in students[username].items():
                                print(f"{course}: {grade}")
                            print(edit.calculate_CGPA(username))
                        else:
                            print("\nNo record found!\n")

                    elif usr_choice == "3" :
                        student_db.available_courses()

                    elif usr_choice == "4":
                        students = student_db.load_data(student_db.student_data)
                        course_name = input("Enter the course name: ")
                        print("List of available courses if the course is not available :")

                        for student, courses in students.items():
                            if student == username:
                                if course_name in courses:
                                    student_db.available_courses()
                                    edit.remove_course(username, course_name, role)
                                    break
                                elif course_name in student_db.available_courses():
                                    edit.add_course(username, course_name, role)
                                    break

                            
                    elif usr_choice == "5":
                        print("Logging out....")
                        break

                elif role == "teacher":
                    print("\n1. View Students")
                    print("2. Add Student")
                    print("3. Remove Student")
                    print("4. Add Course")
                    print("5. Update Grades")
                    print("6. Class Average")
                    print("7. Logout")

                    user_choice = input("Enter choice: ")

                    if user_choice == "1":
                        teacher_db.view_students(username)

                    elif user_choice == "2":
                        name = input("Enter student name: ")
                        course = input("Enter the course name: ")
                        teacher_db.add_student(name, course, username)

                    elif user_choice == "3":
                        name = input("Enter student name to remove: ")
                        course = input("Enter the course name: ")
                        teacher_db.remove_student(name, course, username)

                    elif user_choice == "4":
                        course = input("Enter course name: ")
                        edit.add_course(username, course, role)

                    elif user_choice == "5":
                        name = input("Enter student name: ")
                        course = input("Enter course name: ")
                        grades = input("Enter grades: ")
                        edit.update_grade(name, course, grades, username)

                    elif user_choice == "6":
                        course_name = input("Enter the course name: ")
                        print(edit.class_average(course_name))

                    elif user_choice == "7":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice or insufficient permissions.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Something went wrong! Try again.")

if __name__ == "__main__":
    main()
