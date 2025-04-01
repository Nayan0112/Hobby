STUDENT GRADE MANAGER :

###################################################################################################################################

    To start with project :

    After downloading and extracting, make sure CreditManagerM.py DataBaseM.py and MainM.py is present. Please go through requirements.txt for installation of any library (if required)
    Then in CLI type :

    For Unix systems :
        python3 mainM.py
    
    For windows systems :
        python mainM.py

        1. Register as student / teacher .
        2. Enter password .
        3. Teachers need to create courses .
        4. Teachers may add students in their courses .
        5. Then assign a grade between 0 - 10 . 
        6. Students can also add couses to thier basket .
        7. The grades can be only edited by the teacher .
    
    ############################################################################################################################

    Design choices :

        Since GUI was not possible, I went will a CLI-based program. The program runs indefinetly untill quit or Ctrl + C. Main inspiration was from an attendance maintainance code written by our prof. in Java with incoporated the ideas of inheritance. In my code I tried to make student and teacher different classes to incoporate features sperately. JSON was choosen since that seemed appropiate 
        for this job.
    ############################################################################################################################

    FEATURES :

        The program is meant to manage the grades of the student. The program incoporates the idea of inheritance .
        Details of usersnames and password are stored in user_data.json. The informations about students and teachers are stored in files student_data.json and teacher_data.json respectively.

        user_data :
        It is stored in the format : 
            {
                "user_1" : {
                    password : ***
                    role : <student/teacher>
                }
                .
                .
                .
            }
            
        Similarly student_data / teacher_data :
            {
                "student_1" : {
                    course_1 : <grade_assigned>
                    .
                    .
                    .
                }
                .
                .
            }

        The fundamental idea of this program is to update the grades of list of students belonging to different courses and teachers. Teacher can easily update the student's grade name-wise and check class average. As for the students they can view the registered courses and their grade. Adding and dropping courses also made easy by typing the course name, the code will automatically go through the student details and add/drop courses automatically. If they want to add courses they also check for available courses followed with its instructors.
        The teacher can alos check the class averages so that they can change the overvall grade accordingly.


        Things I wanted add more :
            -> GRADE BUMPS to make class average desirable.
            -> GRADE PARSER so that we can enter A,B.. and it detects and coverts it into points
            -> REMARKS from instructors
            -> semester-wise
            -> SQL based database
            -> Hashing of passwords
            -> GUI :(
                
        etc...

        ref : 
            NOTES from google classoom for file management in JSON
            NOTES from our prof for inheritance and basic code structures

