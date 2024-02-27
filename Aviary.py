import Pet


class Aviary:

    def __init__(self, size, availability_of_walking, pets):
        self.size = size
        self.availability_of_walking = availability_of_walking
        self.pets = pets


a1 = Aviary(size="Большой", availability_of_walking="С выгулом", pets=[Pet.p2, Pet.p3])
a2 = Aviary(size="Маленький", availability_of_walking="Без выгула",  pets=[Pet.p1, Pet.p4])