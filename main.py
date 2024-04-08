from abc import ABC, abstractmethod


# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete Product: Dog
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Concrete Product: Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Simple Factory
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Client
def main():
    factory = AnimalFactory()

    dog = factory.create_animal("dog")
    print(f"Dog says: {dog.speak()}")

    cat = factory.create_animal("cat")
    print(f"Cat says: {cat.speak()}")


if __name__ == "__main__":
    main()
