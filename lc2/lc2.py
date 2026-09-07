class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        return"..."
    def __str__(self):
        return f"{self.name} says {self.make_sound()}"


class dog(Animal):
    def make_sound(self):
        return "Woof!"
class cat(Animal):
    def make_sound(self):
        return "Meow!"
    
dog1 = dog("Doggy")
cat1 = cat("Kitty")

animals = [dog1, cat1]

for animal in animals:
    print(animal)