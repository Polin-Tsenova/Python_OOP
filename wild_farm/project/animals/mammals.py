# from excersises.wild_farm.project.animals.animal import Mammal
# from excersises.wild_farm.project.food import Meat, Vegetable, Fruit
from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return 'Squeak'

    def feed(self, food):
        if isinstance(food, Fruit) or isinstance(food, Vegetable):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return 'Woof!'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return 'Meow'

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
            return
        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


# t = Tiger("Pip", 100, 10)
# print(t)
# meat = Meat(10)
# print(t.make_sound())
# print(t.feed(meat))
# print(t)