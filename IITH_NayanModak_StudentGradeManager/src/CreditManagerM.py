from DataBaseM import TeacherDB, StudentDB

class Editor:
    def __init__(self):
        self.teacher_db = TeacherDB()
        self.student_db = StudentDB()

    def add_course(self, name, course, role):
        db = self.student_db if role == "student" else self.teacher_db
        users = db.load_data(db.student_data if role == "student" else db.teacher_data)

        if role == "student":
            all_courses = {course for teacher_courses in users.values() for course in teacher_courses}
            if course not in all_courses:
                print("Course not available!")        

        if name in users:
            if course not in users[name]:
                users[name][course] = -1
                db.save_data(db.student_data if role == "student" else db.teacher_data, users)
                print("Course added successfully!")
            else:
                print("Course already exists.")
        else:
            print("User not found.")

    def remove_course(self, name, course, role):
        db = self.student_db if role == "student" else self.teacher_db
        users = db.load_data(db.student_data if role == "student" else db.teacher_data)

        if name in users:
            if course in users[name]:
                del users[name][course]  
                db.save_data(db.student_data if role == "student" else db.teacher_data, users)
                print(f"Course '{course}' removed successfully for {name}.")
            else:
                print("Course not found.")
        else:
            print("User not found.")

    def update_grade(self, name, course, grade, teacher):
        users = self.student_db.load_data(self.student_db.student_data)
        
        if course not in self.teacher_db.load_data(self.teacher_db.teacher_data).get(teacher, {}):
            print("Course not found!")
            return

        if name in users and course in users[name]:
            if grade >= 0 and grade <=10 :
                users[name][course] = int(grade) 
                self.student_db.save_data(self.student_db.student_data, users)
                print("Grade updated successfully!")
            else :
                print("Action unsuccesful!")
        else:
            print("Student or course not found!")

    def class_average(self, course):
        users = self.student_db.load_data(self.student_db.student_data)
        total, count = 0, 0

        for user, courses in users.items():
            if course in courses:
                if courses[course] != -1 :
                    total += int(courses[course]) if courses[course] != -1 else print(f"Warning : {user} not GRADED")
                    count += 1
                else :
                    print(f"WARNING : {user} NOT GRADED!")
        
        if count == 0:
            return f"No grades are available for the course : {course}"
        
        average = total / count
        return f"Average grade for {course}: {average:.2f}"

    def calculate_CGPA(self, name):
        users = self.student_db.load_data(self.student_db.student_data)

        if name not in users or not users[name]:
            print("No courses available.")
            return
        
        total = sum(int(grade) if grade > -1 else 0 for grade in users[name].values())
        count = len(users[name])

        CGPA = total / count
        return f"CGPA: {CGPA:.2f}"
