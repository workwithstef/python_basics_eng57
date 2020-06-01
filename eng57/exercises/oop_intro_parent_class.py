
class Animal:
    def __init__(self, species='', limbs=4, natural_habitat=''):
        self.species = species
        self.habitat = natural_habitat
        self.limbs = limbs

    def diet(self, carni_herbi):
        return f'This {self.species} is a {carni_herbi}'

    def sleep(self):
        return 'zzzZZZZZZZzZZZzzz'