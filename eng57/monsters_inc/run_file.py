from eng57.monsters_inc.monster import Monster
from eng57.monsters_inc.student_monster import StudentMonster
from eng57.monsters_inc.course import Course


# CREATE 2 STUDENT OBJECTS
# ADD SKILL TO EACH STUDENT
mike = StudentMonster('Mike Wazowski', '1100A', 'green', 12, ['cunning', 'grit'])
sully = StudentMonster('Sully', '100B', 'blue', 13, ['terrifying', 'confident'])

# CREATE COURSE OBJECT
course1 = Course('Scary Teens 101', '01/06/2020', [])

# APPEND STUDENT OBJECT TO LIST OF STUDENTS ATTRIBUTE
course1.add_student(mike)
course1.add_student(sully)

for student in course1.student_list:
    print(student.get_name())
    print(student.get_skills())
    print(course1.get_module_name())












# ITERATE OVER GET LIST OF STUDENTS (FOR LOOP)

