

class Course:
    def __init__(self, module_name, start_date, list_of_students=[]):
        self.__module_name = module_name
        self.start_date = start_date
        self.student_list = list_of_students

    def set_module_name(self, module):
        self.__module_name = module

    def get_module_name(self):
        return self.__module_name

    def add_student(self, student):
        self.student_list.append(student)
        return 'Student added!'
