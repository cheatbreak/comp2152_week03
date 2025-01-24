#Dice Options created using list() and range()
diceOptions = list(range(1,7))

# Weapons lilst

weapons = ["Fist", "Knife", "Club", "Gun", "Bat", "Bomb", "Grenade"]

print("Available weapons are: ", ",".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        return value