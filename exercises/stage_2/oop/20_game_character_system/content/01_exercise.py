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
#
# Hint: This exercise combines inheritance, method overriding, object interaction, and composition

# Write your code here:
