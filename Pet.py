class Pet:

    def __init__(self, kind, name, animal_species, gender):
        self.kind = kind
        self.name = name
        self.animal_species = animal_species
        self.gender = gender


p1 = Pet(kind="Кот", name="Сэм", animal_species="Британский", gender="М")
p2 = Pet(kind="Собака", name="Джек", animal_species="Лайка", gender="М")
p3 = Pet(kind="Собака", name="Лейла", animal_species="Немецкая овчарка", gender="Ж")
p4 = Pet(kind="Кот", name="Яся", animal_species="Сфинкс", gender="Ж")