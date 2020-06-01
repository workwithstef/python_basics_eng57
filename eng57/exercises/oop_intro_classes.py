
class Animal:
    def __init__(self, species='', limbs=4, natural_habitat=''):
        self.species = species
        self.habitat = natural_habitat
        self.limbs = limbs

    def diet(self, carni_herbi):
        return f'This {self.species} is a {carni_herbi}'

    def sleep(self):
        return 'zzzZZZZZZZzZZZzzz'


class Cat(Animal):
    # age is 'non-optional', breed & name are 'optionals'; non-optionals must always come first
    def __init__(self, age, breed='Tiger', name='Melon'):
        super().__init__('Mammal', 4, 'Indian Rainforest')
        self.__name = name
        self.__age = age
        self.__breed = breed
        self.colour = 'white with black stripes... or is it black with white stripes..?'
        self.__best_friend = 'Stefan'
        print(self.__info_summary())

    def purr(self):
        return '*vibrate* purrrrrr *vibrate*'

    def bark(self):
        return "What's that?"

    def sleep(self):
        return "You aint gotta tell me twice-- zzzzZZZzz"

    def food(self):
        return f'{self.__name} loves salmon and fresh lamb'

    def getter_name(self):
        return self.__name

    def __setter_age(self):
        self.__age += 1

    def birthday(self):
        self.__setter_age()
        return f"Happy Birthday {self.__name}!! You are now {self.__age} years old :)"

    def __info_summary(self):
        return f"This {self.species} is a beautiful {self.__breed}, born in the {self.habitat}. It is currently {self.__age} years old. It's name is {self.__name}, and it's {self.__best_friend}'s ThunderBuddy for life."


