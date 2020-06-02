from eng57.monsters_inc.monster import Monster


class StudentMonster(Monster):
    def __init__(self, name, tax_number, fur, student_no, skill_list=[]):
        super().__init__(name, tax_number, fur)
        self.__student_no = student_no
        self.skill_list = skill_list

    def set_student_no(self, student_no):
        self.__student_no = student_no

    def get_student_no(self):
        return self.__student_no

    def add_skill(self, skill):
        self.skill_list.append(skill)
        return 'Skill added!'

    def get_skills(self):
        return self.skill_list
