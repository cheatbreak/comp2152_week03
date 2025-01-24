#Dice Options created using list() and range()
diceOptions = list(range(1,7))

# Weapons lilst

weapons = ["Fist", "Knife", "Club", "Gun", "Bat", "Bomb", "Grenade"]

print("Available weapons are: ", ",".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 60:
            return value
        else:
            print("Invalid Input! Please enter a number between 1-6")

combatStrength = getCombatStrength("Please enter a nuber between 1-6 for player")
mCombatStrength = getCombatStrength("Please enter a nuber between 1-6 for player")