class Flower:
    def __init__(self, name, water_rquirements, is_happy=False):
        self.name = name
        self.water_rquirements = water_rquirements
        self.is_happy = is_happy

    def water(self, quantity):
        self.quantity = quantity
        if self.quantity >= self.water_rquirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())