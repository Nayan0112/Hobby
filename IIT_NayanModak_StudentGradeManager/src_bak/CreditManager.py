from DataBase import Database 

class Editor:

    def __init__(self):
        self.db = Database()
    
    def add_course(self, name, course,role):
        users = self.db.load_data()
        if role == "student" :
            if not any(course in courses for courses in users.values()):
                print("Course not available!")
                return 0          
        if name in users :
            if course not in users[name]:
                users[name][course] = 0  
                self.db.save_data(users)
                print("Course added successfully!")
                return 1

            else:
                print("Course already exists.")
                return 0
        else:
            print("...")
            return 0
    
    def remove_course(self, name, course,role):
        users = self.db.load_data()

        if name in users:
            if course in users[name]:
                del users[name][course]  
                self.db.save_data(users)
                print(f"Course '{course}' removed successfully for {name}.")
                return 1
            else:
                print("Course not found.")
                return 0
        else:
            print("Student not found.")
            return 0


    def update_grade(self, name, course, grade, teacher):
        users = self.db.load_data()
        if course not in users[teacher].keys():
            print("Course not found!")
            return
        
        if name in users:
            if course in users[name]:
                users[name][course] = int(grade)  
                self.db.save_data(users)
                print("Grade updated successfully!")
            else:
                print("Course does not exist!")
        else:
            print("Student not found.")

    def class_average(self, course):
        users = self.db.load_data() 
        total, count = 0, -1

        for user, courses in users.items(): 
            if course in courses:
                total += (int)(courses[course])
                count += 1
        
        if count == 0:
            print("No grades available!") 
            return
        
        average = total / count
        return f"Average grade for {course}: {average:.2f}"

    def calculate_CGPA(self, name):
        total, count = 0, 0
        users = self.db.load_data()
        if name in users:
            for course in users[name]:  
                total += (int)(users[name][course]) 
                count += 1
        if count == 0:
            print("No courses are available.")
            return
        
        CGPA = total / count
        return f"CGPA: {CGPA:.2f}"
