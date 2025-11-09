# Exercise: Game Character System with Inheritance
# Description: Build a complete game character system using all OOP concepts learned
#
# Tasks:
# 1. Create a Character class (parent) with:
#    - name, health, attack_power
#    - attack(other_character) method
#    - is_alive() method
#    - __str__ method
# 2. Create Warrior class (child) that:
#    - Inherits from Character
#    - Adds shield_strength property
#    - Overrides attack() to do more damage
#    - Adds block() method that uses shield
# 3. Create Mage class (child) that:
#    - Inherits from Character
#    - Adds mana property
#    - Overrides attack() to use mana
#    - Adds cast_spell() method
# 4. Create characters and simulate a battle
#
# Expected Output:
# Warrior: Conan (Health: 120, Attack: 20, Shield: 50)
# Mage: Gandalf (Health: 80, Attack: 15, Mana: 100)
#
# Battle begins!
# Conan attacks Gandalf for 25 damage!
# Gandalf casts a spell at Conan for 30 damage!
# Conan blocks with shield! Shield strength: 20
#
# Battle Status:
# Warrior: Conan (Health: 90, Attack: 20, Shield: 20)
# Mage: Gandalf (Health: 55, Attack: 15, Mana: 80)

# Solution:

# Step 1: Create the parent Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_character):
        # Basic attack method
        other_character.health = other_character.health - self.attack_power
        print(f"{self.name} attacks {other_character.name} for {self.attack_power} damage!")

    def is_alive(self):
        # Check if character is still alive
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack: {self.attack_power})"


# Step 2: Create the Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name, health, attack_power, shield_strength):
        # Call parent constructor
        super().__init__(name, health, attack_power)
        # Add warrior-specific property
        self.shield_strength = shield_strength

    def attack(self, other_character):
        # Override attack to do more damage (warrior bonus)
        damage = self.attack_power + 5  # Warriors do extra damage
        other_character.health = other_character.health - damage
        print(f"{self.name} attacks {other_character.name} for {damage} damage!")

    def block(self, damage):
        # Block damage using shield
        if self.shield_strength >= damage:
            self.shield_strength = self.shield_strength - damage
            print(f"{self.name} blocks with shield! Shield strength: {self.shield_strength}")
        else:
            remaining_damage = damage - self.shield_strength
            self.shield_strength = 0
            self.health = self.health - remaining_damage
            print(f"{self.name}'s shield breaks! Takes {remaining_damage} damage!")

    def __str__(self):
        return f"Warrior: {self.name} (Health: {self.health}, Attack: {self.attack_power}, Shield: {self.shield_strength})"


# Step 3: Create the Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        # Call parent constructor
        super().__init__(name, health, attack_power)
        # Add mage-specific property
        self.mana = mana

    def attack(self, other_character):
        # Override attack to check for mana
        if self.mana >= 10:
            damage = self.attack_power
            other_character.health = other_character.health - damage
            self.mana = self.mana - 10
            print(f"{self.name} attacks {other_character.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't have enough mana!")

    def cast_spell(self, other_character):
        # Special spell attack that uses more mana but does more damage
        if self.mana >= 20:
            damage = self.attack_power * 2
            other_character.health = other_character.health - damage
            self.mana = self.mana - 20
            print(f"{self.name} casts a spell at {other_character.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't have enough mana for spell!")

    def __str__(self):
        return f"Mage: {self.name} (Health: {self.health}, Attack: {self.attack_power}, Mana: {self.mana})"


# Step 4: Create characters
warrior = Warrior("Conan", 120, 20, 50)
mage = Mage("Gandalf", 80, 15, 100)

# Step 5: Display initial status
print(warrior)
print(mage)
print("\nBattle begins!")

# Step 6: Simulate battle
warrior.attack(mage)  # Warrior attacks (does 25 damage with bonus)
mage.cast_spell(warrior)  # Mage casts spell (does 30 damage)
warrior.block(30)  # Warrior blocks 30 damage with shield

# Step 7: Display final status
print("\nBattle Status:")
print(warrior)
print(mage)
