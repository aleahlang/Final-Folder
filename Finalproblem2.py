class Animal:
    def __init__(self):
        self.age = 0
        self.weight = 0

    def age_and_weight(self):
        return (int(self.age) * 7), (int(self.weight) * 16)


cat1 = Animal()
cat1.age = input('Cats age in years:')
cat1.weight = input('Cats weight in pounds:')
print('Cat:\n Age in cat years and Weight in ounces: {} '.format(cat1.age_and_weight()))

dog1 = Animal()
dog1.age = input('Dogs age in years:')
dog1.weight = input('Dogs weight in pounds:')
print('Dog:\n Age in dog years and Weight in ounces: {} '.format(dog1.age_and_weight()))
