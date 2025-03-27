from DataBase import Database
from CreditManager import Editor

def main() :

    db = Database()
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
            if role in ["student", "teacher"]:
                db.register_user(username, password, role)
            else:
                print("Invalid role. Choose 'student' or 'teacher'.")
            
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = db.authenticate_user(username, password)
            if role :
                print(f"Welcome {username}! You are logged in as {role}.")
            else :
                continue

            while role :

                if role == "student" :
                    
                    print("\n1. View registered courses")
                    print("2. Veiw grades")
                    print("3. Add/Drop courses")
                    print("4. Logout")

                    usr_choice = input("Enter choice :")

                    if usr_choice == "1" :
                        students = db.load_data()
                        if username in students :
                            for course in students[username] :
                                print(f"{course}")
                        else :
                            print("\nNo record found!\n")

                    elif usr_choice == "2" :
                        students = db.load_data()
                        if username in students :
                            for course, grade in students[username].items() :
                                print(f"{course} : {grade}")
                            print(edit.calculate_CGPA(username))
                        else :
                            print("\nNo record found!\n")
                    
                    elif usr_choice == "3" :

                        students = db.load_data()
                        course_name = input("Enter the course name :")
                        if username not in students :
                            db.add_student(username, {})
                        if (edit.add_course(username, course_name, role)) == 0 :
                                edit.remove_course(username, course_name, role)
                            

                    elif usr_choice == "4" :
                        print("Logging out....")
                        break

                elif role == "teacher" :
                    print("\n1. View Students")
                    print("2. Add Student")
                    print("3. Remove Student ")
                    print("4. Add Course ")
                    print("5. Update Grades ")
                    print("6. Class Average")
                    print("7. Logout")
                    user_choice = input("\nEnter choice: \n")

                    if user_choice == "1":
                        student_db.veiw_courses(username)
                    elif user_choice == "2" :
                        name = input("Enter student name: ")
                        course = input("Enter the course name:")
                        db.add_student(name, course, username)
                    elif user_choice == "3" :
                        name = input("Enter student name to remove: ")
                        course = input("Enter the course name:")
                        db.remove_student(name, course, username)
                    elif user_choice == "4" :
                        course = input("Enter course name: ")
                        edit.add_course(username, course, role)
                    elif user_choice == "5" :
                        name = input("Enter student name: ")
                        course = input("Enter course name: ")
                        grades = input("Enter grades ")
                        edit.update_grade(name, course, grades, username)
                    elif user_choice == "6" :
                        course_name = input("Enter the course name :")
                        print(edit.class_average(course_name))

                    elif user_choice == "7":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice or insufficient permissions.")
        elif choice == "3" :
            print("Exiting...")
            break
        else :
            print("Something went wrong! Try again.")  

if __name__ == "__main__" :
    main()              