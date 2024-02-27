import Volunteer
import Aviary


class AnimalShelter:

    def __init__(self, name, volunteers, aviaries):
        self.name = name
        self.volunteers = volunteers
        self.aviaries = aviaries


animal_shelter1 = AnimalShelter(name="Мокрый нос", volunteers=[Volunteer.v1, Volunteer.v2], aviaries=[Aviary.a1])
animal_shelter2 = AnimalShelter(name="Мокрый нос", volunteers=[Volunteer.v3], aviaries=[Aviary.a2])