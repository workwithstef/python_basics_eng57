
class Dog:
    def bark(self):
        return 'woof woof!'

    def sleep(self):
        return 'zzZZZZzzzZzzzzzzZZZz'


class Cat:
    def __init__(self, age, breed='Tiger', name='Melon'):
        self.name = name
        self.age = age
        self.breed = breed
        self.colour = 'white with black stripes... or is it black with white stripes..?'
        self.best_friend = 'Stefan'

    def purr(self):
        return '*vibrate* purrrrrr *vibrate*'

    def bark(self):
        return "What's that?"

    def sleep(self):
        return "You aint gotta tell me twice-- zzzzZZZzz"

    def food(self):
        return 'salmon'

    def introduce_yourself(self, name, breed):
        pass

