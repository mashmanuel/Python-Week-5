class Superhero:
    """Base class for all superheroes"""
    def __init__(self, name, secret_identity, powers):
        self._name = name  # Encapsulated attribute
        self._secret_identity = secret_identity
        self._powers = powers
        self._health = 100

    def use_power(self):
        """Base method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement use_power()")

    def take_damage(self, damage):
        """Reduce health by damage amount"""
        self._health = max(0, self._health - damage)
        return f"{self._name} took {damage} damage! Health: {self._health}"

    def heal(self, amount):
        """Restore health"""
        self._health = min(100, self._health + amount)
        return f"{self._name} healed {amount} points. Health: {self._health}"

    def get_info(self):
        """Get superhero information"""
        return (f"Superhero: {self._name}\n"
                f"Secret Identity: {self._secret_identity}\n"
                f"Powers: {', '.join(self._powers)}\n"
                f"Health: {self._health}")


class FlyingHero(Superhero):
    """Superheroes with flight capability"""
    def __init__(self, name, secret_identity, powers, max_altitude):
        super().__init__(name, secret_identity, powers + ['Flight'])
        self._max_altitude = max_altitude  # in meters

    def use_power(self):
        """Fly and attack from above"""
        return (f"{self._name} soars to {self._max_altitude}m and "
                "strikes from the air! ✈️")

    def get_info(self):
        """Extended info with flight details"""
        base_info = super().get_info()
        return f"{base_info}\nMax Flight Altitude: {self._max_altitude}m"


class TechHero(Superhero):
    """Superheroes with advanced technology"""
    def __init__(self, name, secret_identity, powers, gadgets):
        super().__init__(name, secret_identity, powers + ['Technology'])
        self._gadgets = gadgets

    def use_power(self):
        """Use high-tech gadgets"""
        return (f"{self._name} deploys {self._gadgets[0]} "
                "to neutralize the threat! ⚡")

    def upgrade_gadget(self, new_gadget):
        """Add a new gadget to arsenal"""
        self._gadgets.append(new_gadget)
        return f"Added {new_gadget} to {self._name}'s arsenal"


# Demonstration
if __name__ == "__main__":
    print("=== Superhero Class Demonstration ===")
    
    # Create different superheroes
    superman = FlyingHero("Superman", "Clark Kent", 
                         ["Super strength", "Heat vision"], 20000)
    iron_man = TechHero("Iron Man", "Tony Stark",
                       ["Genius intellect"], ["Repulsor beams", "Jarvis AI"])
    
    # Show info
    print("\nSuperhero Profiles:")
    print(superman.get_info())
    print("\n" + iron_man.get_info())
    
    # Demonstrate powers
    print("\n=== Power Demonstration ===")
    print(superman.use_power())
    print(iron_man.use_power())
    
    # Show damage/healing
    print("\n=== Combat Simulation ===")
    print(superman.take_damage(30))
    print(iron_man.take_damage(45))
    print(iron_man.heal(20))