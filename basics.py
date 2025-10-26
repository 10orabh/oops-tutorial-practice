class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")

    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")

    def speak(self):
        return "Meow!"
# Example usage:
dog = Dog("Buddy")      
cat = Cat("Whiskers")
print(f"{dog.name} says {dog.speak()}")
print(f"{cat.name} says {cat.speak()}")