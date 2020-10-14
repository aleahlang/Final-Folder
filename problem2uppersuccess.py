class Animal:
    def __init__(self):
        self.petname = 0
        self.ownername = 0

    def petname_and_ownername(self):
        return self.petname.upper(), self.ownername.upper()


cat1 = Animal()
cat1.petname = input('Cats name:')
cat1.ownername = input('Cats owners name:')
print('Cat:\n Name of cat and Owners name: {} '.format(cat1.petname_and_ownername()))

dog1 = Animal()
dog1.petname = input('Dogs name:')
dog1.ownername = input('Dogs owners name:')
print('Dog:\n Name of dog and Owners name: {} '.format(dog1.petname_and_ownername()))
