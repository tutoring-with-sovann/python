# Exercise: Game Character System (Extended)
# Description: Build a complete RPG battle system with parties, items, XP, and leveling
#
# Tasks:
# 1. Create an Item class with: name, type (weapon/potion/armor), stat_bonus
#    - Add use(character) method that applies the item's effect
# 2. Create a Character class (parent) with:
#    - name, health, max_health, attack, defense, level, xp, inventory
#    - attack(target) - virtual method (must override)
#    - take_damage(amount, damage_type) - reduces health by amount - defense
#    - heal(amount) - restores health up to max_health
#    - gain_xp(amount) - levels up if xp >= level * 100
#    - add_item(item) - adds to inventory
#    - use_item(item_name) - uses item from inventory
#    - is_alive() - returns True if health > 0
#    - __str__ - displays character stats
# 3. Create Warrior class (child) with:
#    - rage property (starts at 0, max 100)
#    - shield property
#    - Overrides attack() - physical damage + rage bonus
#    - Add block() - reduces next damage by shield amount
#    - Add rage_attack() - powerful attack using all rage
#    - Add take_damage() - gains rage when hit
# 4. Create Mage class (child) with:
#    - mana property
#    - Overrides attack() - magic damage using mana
#    - Add cast_spell(target, spell_name) - different spells cost different mana
#    - Add regenerate_mana() - restores mana
#    - Add take_damage() - can reduce mana to absorb damage (mana shield)
# 5. Create a Party class with:
#    - members list, is_player_party boolean
#    - add_member(character) method
#    - is_defeated() - returns True if all members dead
#    - get_alive_members() - returns list of living members
#    - select_target(enemy_party) - AI targeting logic
# 6. Create a Battle class with:
#    - player_party, enemy_party
#    - turn_number
#    - execute_turn(party) - each living member acts
#    - resolve_round() - player turn then enemy turn
#    - is_battle_over() - checks if either party defeated
#    - display_status() - shows battle state
# 7. Demonstrate: Create parties with mixed classes, simulate multi-turn battle
#
# Expected Output:
# === BATTLE BEGIN ===
# Party 1: [Warrior: Conan (Lv2 HP:120/120 ATK:25)], [Mage: Merlin (Lv1 HP:80/80 MP:100)]
# Party 2: [Warrior: Grimgor (Lv1 HP:100/100 ATK:20)], [Mage: Zarana (Lv1 HP:70/70 MP:80)]
#
# === TURN 1 ===
# Conan attacks Grimgor for 30 damage! (Critical!)
# Merlin casts Fireball at Zarana for 35 damage!
# Grimgor attacks Conan for 18 damage! Conan gains 10 rage.
# Zarana casts Ice Lance at Merlin for 25 damage!
#
# Status: P1[Conan:102 HP, Merlin:55 HP] | P2[Grimgor:70 HP, Zarana:45 HP]
#
# === TURN 2 ===
# Conan uses RAGE ATTACK on Grimgor for 50 damage!
# Merlin casts Lightning at Zarana for 28 damage! Zarana defeated!
# Grimgor attacks Conan for 22 damage!
#
# Battle Over! Party 1 Victorious!
# Conan gained 50 XP (Level Up!) Conan is now Level 3!
# Merlin gained 50 XP (Level Up!) Merlin is now Level 2!
#
# Hint: Use polymorphism - all characters can attack() differently. Parties contain Characters.

# Solution:

import random

# Step 1: Create Item class
class Item:
    def __init__(self, name, item_type, stat_bonus):
        self.name = name
        self.item_type = item_type  # "weapon", "potion", "armor"
        self.stat_bonus = stat_bonus

    def use(self, character):
        if self.item_type == "potion":
            character.heal(self.stat_bonus)
            print(f"{character.name} uses {self.name} and heals for {self.stat_bonus} HP!")
            return True
        elif self.item_type == "weapon":
            character.attack += self.stat_bonus
            print(f"{character.name} equips {self.name}! Attack +{self.stat_bonus}")
            return True
        return False


# Step 2: Create Character parent class
class Character:
    def __init__(self, name, health, attack, defense=5):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.blocking = False

    def attack_target(self, target):
        raise NotImplementedError("Subclasses must implement attack_target()")

    def take_damage(self, amount, damage_type="physical"):
        actual_damage = max(0, amount - self.defense)
        self.health -= actual_damage
        return actual_damage

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def gain_xp(self, amount):
        self.xp += amount
        xp_needed = self.level * 100
        if self.xp >= xp_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        print(f"{self.name} gained enough XP! {self.name} is now Level {self.level}!")

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item_name):
        for i, item in enumerate(self.inventory):
            if item.name == item_name:
                if item.use(self):
                    self.inventory.pop(i)
                return
        print(f"{self.name} doesn't have {item_name}")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} (Lv{self.level} HP:{self.health}/{self.max_health} ATK:{self.attack})"


# Step 3: Create Warrior class
class Warrior(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack, defense=8)
        self.rage = 0
        self.max_rage = 100
        self.shield = 50

    def attack_target(self, target):
        damage = self.attack + (self.rage // 10)
        actual = target.take_damage(damage, "physical")
        self.rage = min(self.max_rage, self.rage + 10)
        crit = " (Critical!)" if random.random() < 0.2 else ""
        print(f"{self.name} attacks {target.name} for {actual} damage!{crit}")

    def block(self):
        self.blocking = True
        print(f"{self.name} raises shield!")

    def rage_attack(self, target):
        damage = self.attack + self.rage
        actual = target.take_damage(damage, "physical")
        print(f"{self.name} uses RAGE ATTACK on {target.name} for {actual} damage!")
        self.rage = 0

    def take_damage(self, amount, damage_type="physical"):
        if self.blocking:
            reduced = max(0, amount - self.shield)
            self.shield -= min(amount, self.shield)
            self.blocking = False
            self.health -= reduced
            print(f"{self.name} blocks! Shield remaining: {self.shield}")
            return reduced
        actual = super().take_damage(amount, damage_type)
        self.rage = min(self.max_rage, self.rage + 10)
        print(f"{self.name} takes {actual} damage! Rage: {self.rage}")
        return actual


# Step 4: Create Mage class
class Mage(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack, defense=3)
        self.mana = 100
        self.max_mana = 100
        self.mana_shield_active = False

    def attack_target(self, target):
        if self.mana >= 10:
            self.mana -= 10
            damage = self.attack + 5
            actual = target.take_damage(damage, "magic")
            print(f"{self.name} casts Magic Missile at {target.name} for {actual} damage!")
        else:
            print(f"{self.name} doesn't have enough mana!")

    def cast_spell(self, target, spell_name):
        spells = {
            "Fireball": {"cost": 20, "damage": self.attack + 15},
            "Ice Lance": {"cost": 15, "damage": self.attack + 10},
            "Lightning": {"cost": 25, "damage": self.attack + 20}
        }
        if spell_name in spells and self.mana >= spells[spell_name]["cost"]:
            self.mana -= spells[spell_name]["cost"]
            damage = spells[spell_name]["damage"]
            actual = target.take_damage(damage, "magic")
            print(f"{self.name} casts {spell_name} at {target.name} for {actual} damage!")
            if not target.is_alive():
                print(f"{target.name} defeated!")
            return True
        print(f"{self.name} can't cast {spell_name}!")
        return False

    def regenerate_mana(self):
        restored = min(20, self.max_mana - self.mana)
        self.mana += restored
        print(f"{self.name} regenerates {restored} mana!")

    def take_damage(self, amount, damage_type="physical"):
        if self.mana_shield_active and self.mana > 0:
            absorb = min(self.mana, amount)
            self.mana -= absorb
            remaining = max(0, amount - absorb)
            self.health -= remaining
            print(f"{self.name}'s mana shield absorbs {absorb} damage! Takes {remaining} damage.")
        else:
            return super().take_damage(amount, damage_type)


# Step 5: Create Party class
class Party:
    def __init__(self, name, is_player_party=False):
        self.name = name
        self.members = []
        self.is_player_party = is_player_party

    def add_member(self, character):
        self.members.append(character)

    def is_defeated(self):
        return not any(m.is_alive() for m in self.members)

    def get_alive_members(self):
        return [m for m in self.members if m.is_alive()]

    def select_target(self, enemy_party):
        # Select from enemy party, not own party
        alive = enemy_party.get_alive_members()
        if alive:
            return random.choice(alive)
        return None

    def __str__(self):
        alive = self.get_alive_members()
        return f"[{', '.join(str(m) for m in alive)}]"


# Step 6: Create Battle class
class Battle:
    def __init__(self, player_party, enemy_party):
        self.player_party = player_party
        self.enemy_party = enemy_party
        self.turn_number = 0

    def execute_turn(self, party, opponents):
        alive = party.get_alive_members()
        for character in alive:
            if not opponents.is_defeated():
                target = party.select_target(opponents)  # party selects from opponents
                if target:
                    if isinstance(character, Mage) and character.mana >= 15:
                        spells = ["Fireball", "Ice Lance", "Lightning"]
                        character.cast_spell(target, random.choice(spells))
                    elif isinstance(character, Warrior) and character.rage >= 50:
                        character.rage_attack(target)
                    else:
                        character.attack_target(target)

    def resolve_round(self):
        self.turn_number += 1
        print(f"\n=== TURN {self.turn_number} ===")

        self.execute_turn(self.player_party, self.enemy_party)
        if self.enemy_party.is_defeated():
            return

        self.execute_turn(self.enemy_party, self.player_party)
        self.display_status()

    def is_battle_over(self):
        return self.player_party.is_defeated() or self.enemy_party.is_defeated()

    def display_status(self):
        p1_alive = self.player_party.get_alive_members()
        p2_alive = self.enemy_party.get_alive_members()
        p1_status = ", ".join(f"{m.name}:{m.health} HP" for m in p1_alive)
        p2_status = ", ".join(f"{m.name}:{m.health} HP" for m in p2_alive)
        print(f"\nStatus: P1[{p1_status}] | P2[{p2_status}]")

    def award_xp(self, xp_amount):
        for member in self.player_party.get_alive_members():
            member.gain_xp(xp_amount)


# Step 7: Demonstration
print("=== BATTLE BEGIN ===")

# Create parties
player_party = Party("Heroes", is_player_party=True)
enemy_party = Party("Monsters", is_player_party=False)

# Create characters
conan = Warrior("Conan", 120, 25)
merlin = Mage("Merlin", 80, 15)
grimgor = Warrior("Grimgor", 100, 20)
zarana = Mage("Zarana", 70, 15)

# Level up Conan for demo
conan.gain_xp(100)

# Add to parties
player_party.add_member(conan)
player_party.add_member(merlin)
enemy_party.add_member(grimgor)
enemy_party.add_member(zarana)

# Show initial state
print(f"Party 1: {player_party}")
print(f"Party 2: {enemy_party}")

# Create battle and fight
battle = Battle(player_party, enemy_party)

while not battle.is_battle_over() and battle.turn_number < 5:
    battle.resolve_round()

# Result
print("\nBattle Over!")
if enemy_party.is_defeated():
    print("Party 1 Victorious!")
    battle.award_xp(50)
elif player_party.is_defeated():
    print("Party 2 Victorious!")
else:
    print("Battle ended in a draw!")
