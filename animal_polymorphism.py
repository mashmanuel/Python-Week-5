class Animal:
    """Base class for all animals"""
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Movement method to be overridden"""
        raise NotImplementedError("Subclasses must implement move()")


class Bird(Animal):
    """Birds fly through the air"""
    def move(self):
        return f"{self.name} is flying through the sky 🌟"
    
    def sing(self):
        return "Tweet tweet!"


class Fish(Animal):
    """Fish swim in water"""
    def move(self):
        return f"{self.name} is swimming in the ocean 🌊"
    
    def blow_bubbles(self):
        return "Blub blub blub!"


class Cheetah(Animal):
    """Cheetahs run on land"""
    def move(self):
        return f"{self.name} is sprinting across the savanna 🐆"
    
    def purr(self):
        return "Purrrrr!"


# Demonstration
def animal_movement_demo(animals):
    """Show polymorphic movement"""
    print("\n=== Animal Movement Demonstration ===")
    for animal in animals:
        print(animal.move())
        # Call type-specific methods
        if isinstance(animal, Bird):
            print(animal.sing())
        elif isinstance(animal, Fish):
            print(animal.blow_bubbles())
        elif isinstance(animal, Cheetah):
            print(animal.purr())
        print()


if __name__ == "__main__":
    # Create animal instances
    animals = [
        Bird("Robin"),
        Fish("Clownfish"),
        Cheetah("Chester")
    ]
    
    print("=== Animal Polymorphism Example ===")
    print(f"Created {len(animals)} different animals\n")
    
    # Show info about each animal
    for i, animal in enumerate(animals, 1):
        print(f"{i}. {animal.__class__.__name__}: {animal.name}")
    
    # Demonstrate movement
    animal_movement_demo(animals)