class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    def display_status(self):
        print("Name: " + self.name)
        print("Health: " + str(self.health))
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))

def create_character():
    name = input("What is your character's name? ")
    health = int(input("What is your character's starting health? "))
    attack = int(input("What is your character's starting attack? "))
    defense = int(input("What is your character's starting defense? "))
    return Character(name, health, attack, defense)

player = create_character()
player.display_status()

world = {"a": "forest", "b": "mountain", "c": "lake"}

print("You find yourself in a vast world with three different regions to explore.")
print("a: Forest\nb: Mountain\nc: Lake")

region = input("Which region would you like to explore? ")

if region in world:
    print("You have entered the " + world[region] + ".")
else:
    print("Invalid input. Please try again.")

