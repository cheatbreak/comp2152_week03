import random
#Dice Options created using list() and range()
diceOptions = list(range(1,7))

# Weapons lilst

weapons = ["Fist", "Knife", "Club", "Gun", "Bat", "Bomb", "Grenade"]

print("Available weapons are: ", ",".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
            print("Invalid Input! Please enter a number between 1-6")

combatStrength = getCombatStrength("Please enter a number between 1-6 for player")
mCombatStrength = getCombatStrength("Please enter a number between 1-6 for player")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons(heroRoll - 1)
    monsterWeapon = weapons(monsterRoll - 1)

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    if heroTotal > monsterTotal:
        print("Player wins!")
    elif heroTotal < monsterTotal:
        print("Monster wins!")
    else:
        print("Its a tie!")