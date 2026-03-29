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

# Write your code here:
