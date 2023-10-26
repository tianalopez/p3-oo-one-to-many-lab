

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if Pet.PET_TYPES.count(pet_type):
            self._pet_type = pet_type
        else:
            raise Exception
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return Pet.all

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda x: x.name)
