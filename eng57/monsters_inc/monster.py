
class Monster:
    def __init__(self, name, tax_number, fur):
        self.__name = name
        self.__tax_number = tax_number
        self.__fur = fur

    def set_name(self, name):
        self.__name = name.title()

    def get_name(self):
        return self.__name

    def set_tax_number(self, tax_no):
        self.__tax_number = tax_no

    def get_tax_number(self):
        return self.__tax_number



