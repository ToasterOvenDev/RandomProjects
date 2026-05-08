import random
import json
import math

def saveObject():
        pass

# unserializing 

# Caracter Classes
class character:
        def __init__(self, name, age, char_class, level, stats, health, speed, armor, max_health, weapon, skills, inventory, race, stat_points, accessories):
                self.name = name # The character's name, which can be modified by the player
                self.age = age # The character's age
                self.char_class = char_class # The character's class
                self.level = level # The character's level, which can be modified by gaining experience and leveling up
                self.stats = stats # A dictionary of the character's stats, Strength, Dexterity, Constitution, Intelligence, Ability
                self.health = health # The character's current health, which can be modified by damage and healing
                self.inventory = inventory # A list of the character's inventory items, which can be modified by adding and removing items
                self.skills = skills # A list of the character's skills, which can be modified by adding and removing skills
                self.weapon = weapon # The character's equipped weapon, which can be modified by equipping and unequipping weapons
                self.max_health = max_health # The character's maximum health
                self.speed = speed # The character's speed, determines initiative in combat
                self.armor = armor # The character's armor class, which can be modified by leveling up and equipping items
                self.race = race # The character's race, which can affect their stats and abilities
                self.stat_points = stat_points # The amount of current stat points
                self.accessories = accessories # A list of the character's equipped accessories, which can be modified by equipping and unequipping accessories
                self.active_effects = [] # A list of the character's active effects, such as stat boosts from boost items, or debuffs from enemy attacks
        
        def __str__(self):
                printedData = {
                        "name":self.name,
                        "age":self.age,
                        "class":self.char_class.name,
                        "race":self.race.name,
                        "level":self.level,
                        "max_health":self.max_health,
                        "health":self.health,
                        "stat_points":self.stat_points,
                        "stats":self.stats,
                        "speed":self.speed,
                        "armor":self.armor,
                        "skills":self.serializeSkills(),
                        "weapon":self.serializeWeapon(),
                        "accessories":self.serializeAccessories(),
                        "inventory":self.serializeInventory(),
                        "active_effects":self.serializeActive_effects()
                }
                return json.dumps(printedData,indent=4)
        # Save/Load functions
        def serializeWeapon(self):
                if self.weapon:
                        return self.weapon.serialize()
                return None
        def serializeInventory(self):
                serializedInventory = []
                for item in self.inventory:
                        serializedInventory.append(item.serialize())
                return serializedInventory
        def serializeSkills(self):
                serializedSkills = []
                for skill in self.skills:
                        serializedSkills.append(skill.serialize())
                return serializedSkills
        def serializeAccessories(self):
                serializedAccessories = []
                for acc in self.accessories:
                        serializedAccessories.append(acc.serialize())
                return serializedAccessories
        def serializeActive_effects(self):
                serializedEffects = []
                for effect in self.active_effects:
                        serializedEffects.append(effect.serialize())
                return serializedEffects
        def serialize(self):
                return {
                        "name":self.name,
                        "age":self.age,
                        "char_class":self.char_class.serialize(),
                        "level":self.level,
        	        "stats":self.stats,
                        "health":self.health,
                        "inventory":self.serializeInventory(),
                        "skills":self.serializeSkills(),
                        "weapon":self.weapon.serialize(),
                        "max_health":self.max_health,
                        "speed":self.speed,
                        "armor":self.armor,
                        "race":self.race.serialize(),
                        "stat_points":self.stat_points,
	        	"accessories":self.serializeAccessories(),
                        "active_effects":self.serializeActive_effects()
                }

        # Level functions
        def statChanged(self):
                self.max_health = int(self.stats["Constitution"] * self.race.healthModifier + self.race.baseHealth)
                self.health = self.max_health
                self.armor = int((200/math.pi)*math.atan(0.5*(self.stats["Constitution"] * self.race.armorModifier) / max(1, self.level)))
                self.speed = int((200/math.pi)*math.atan(0.5*(self.stats["Dexterity"] * self.race.speedModifier) / max(1, self.level)))
        def levelUp(self):
                self.level += 1
                self.stat_points += 5
                self.char_class.levelUp(self)
        def useStat_points(self, stat, points):
                if self.stat_points >= points and stat in self.stats:
                        self.stats[stat] += points
                        self.stat_points -= points
                        self.statChanged()
        # Functions to modify the character's health
        def dodged(self):# temporary method to print when an attack is dodged, can be replaced with a more complex method that provides feedback to the player in the UI
                print("The attack was dodged!")
        def damage(self, damage, attacker, damage_type):
                print("Attacked by "+ attacker.name+" for ",f"{damage:,}"," before any resistances and armor is applied")
                for ability in self.race.abilities:
                        if isinstance(ability, ResistancePassive):
                                damage = ability.applyResistance(damage, damage_type) # Apply any resistances
                level_diff = attacker.level - self.level
                if level_diff <= 10: # if level difference is less than or equal to 10, the damage is not modified by the level difference
                        level_diff = 0
                elif level_diff <= 20: # if level difference is between 11 and 20, the level difference is halved
                        level_diff*=0.5
                ac = self.armor
                if self.level < attacker.level: # if the attacker is higher subtract the level difference from the armor of the character, making them more vulnerable to damage
                        ac -= level_diff # modify the armor of the character based on the level difference
                elif self.level > attacker.level: # if the attacker is lower add the level difference to the armor of the character, making them less vulnerable to damage
                        ac += level_diff # modify the armor of the character based on the level difference
                if ac>100:
                        ac=100
                elif ac<0:
                        ac=0
                damage *= (100 - ac) / 100 # The armor reduces the damage taken by a percentage, with a maximum reduction of 100%
                speedDiff = self.speed - attacker.speed 
                dodge_chance = speedDiff * 0.01 # The character's speed provides a chance to dodge attacks
                for ability in self.race.abilities:
                        if isinstance(ability, DodgePassive):
                                dodge_chance += ability.applyDodgeBonus(self, attacker) # Apply any dodge bonuses
                if random.random() < dodge_chance: # Check if the attack is dodged
                        damage = 0
                        self.dodged()
                self.health -= damage
                print("Damaged for ",f"{damage:,}")
                print("Max: ",f"{self.max_health:,}")
                print("Health: ",f"{self.health:,}")
                if self.health < 0:
                        self.health = 0
        def heal(self, heal):
                self.health += heal
                if self.health > self.max_health:
                        self.health = self.max_health
        # Functions to calculate the character's attack damage
        def attack(self, target): # Defualt attack method
                if self.weapon:
                        self.weapon.attack(self, target)
                else:
                        attDamage = self.stats["Strength"] * 10
                        target.damage(attDamage, self, "physical")
        # Functions to use skills
        def useSkill(self, skill, target):
                if skill in self.skills:
                        skill.use(self, target)
        # Functions to modify the character's inventory and skills
        def addToInventory(self, item):
                self.inventory.append(item)
        def removeFromInventory(self, item):
                if item in self.inventory:
                        self.inventory.remove(item)
        def addSkill(self, skill):
                self.skills.append(skill)
        def removeSkill(self, skill):
                if skill in self.skills:
                        self.skills.remove(skill)
        def equipWeapon(self, weapon):
                if self.weapon in self.inventory:
                    self.weapon = weapon
        def unequipWeapon(self):
                self.weapon = None
        def determineInitiative(self):
                return self.speed * random.random() 
        def equipAccessory(self, accessory):
                if accessory in self.inventory and len(self.accessories) < 2: # A character can only equip 2 accessories at a time
                        self.accessories.append(accessory)
                        accessory.apply(self) # Apply the stat bonuses provided by the accessory to the character's stats when equipped
        def unequipAccessory(self, accessory):
                if accessory in self.accessories:
                        self.accessories.remove(accessory)
                        accessory.remove(self) # Remove the stat bonuses provided by the accessory from the character's stats when unequipped
        def useItem(self, item):
                if item in self.inventory and item.isUsable(): # Check if the item is in the inventory and is usable
                        item.use(self)
class player(character):
        def __init__(self, name, age, char_class, race):
                super().__init__(name, age, char_class, 1, race.stats, race.baseHealth, race.speed, race.armor, race.baseHealth, None, char_class.starting_skills, {}, race, 10, [])
                self.experience = 0 # The player's experience points
        def gainExperience(self, experience):
                self.experience += experience
                if self.experience >= self.level * 100: # Level up when experience reaches a certain threshold, which increases with each level
                        self.levelUp()
        # Save/Load
        def serializeWeapon(self):
                if self.weapon:
                        return self.weapon.serialize()
                return None
        def serialize(self):
                return {
                        "name":self.name,
                        "age":self.age,
                        "char_class":self.char_class.serialize(),
                        "level":self.level,
        	        "stats":self.stats,
                        "health":self.health,
                        "inventory":self.serializeInventory(),
                        "skills":self.serializeSkills(),
                        "weapon":self.serializeWeapon(),
                        "max_health":self.max_health,
                        "speed":self.speed,
                        "armor":self.armor,
                        "race":self.race.serialize(),
                        "stat_points":self.stat_points,
	        	"accessories":self.serializeAccessories(),
                        "active_effects":self.serializeActive_effects(),
                        "experience":self.experience
                }
class npc(character):
        def __init__(self, name, char_class, level, stats, health, speed, armor, max_health, weapon, skills, inventory, race, difficulty_modifier):
                super().__init__(name, random.random() * 80 + 20, char_class, level, stats, health, speed, armor, max_health, weapon, skills, inventory, race)
                self.difficulty_modifier = difficulty_modifier # A modifier to the NPC's stats and abilities, which can be used to make the NPC easier or harder to defeat ranges from 0.5 (easier) to 2.0 (harder)
                for stat in self.stats:
                        self.stats[stat] = int(self.stats[stat] * self.difficulty_modifier) # Modify the NPC's stats based on the difficulty modifier
                self.health = int(self.health * self.difficulty_modifier)
                self.max_health = self.health
        # Save/Load
        def serialize(self):
                return {
                        "name":self.name,
                        "age":self.age,
                        "char_class":self.char_class.serialize(),
                        "level":self.level,
        	        "stats":self.stats,
                        "health":self.health,
                        "inventory":self.serializeInventory(),
                        "skills":self.serializeSkills(),
                        "weapon":self.weapon.serialize(),
                        "max_health":self.max_health,
                        "speed":self.speed,
                        "armor":self.armor,
                        "race":self.race.serialize(),
                        "stat_points":self.stat_points,
	        	"accessories":self.serializeAccessories(),
                        "active_effects":self.serializeActive_effects(),
                        "difficulty_modifier":self.difficulty_modifier
                }


# Skill Classes
class skill:
        def __init__(self, name, description):
                self.name = name
                self.description = description
        def use(self, user, target): # abstract method to be overridden by subclasses
                pass
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description
                }
class AttackSkill(skill):
        def __init__(self, name, description, damage, strength_multiplier, damage_type):
                super().__init__(name, description)
                self.damage = damage
                self.strength_multiplier = strength_multiplier
                self.type = damage_type
        def use(self, user, target):
                damage = self.damage + user.getStats()["Strength"] * self.strength_multiplier
                target.damage(damage, user.level, self.damage_type)
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "damage":self.damage,
                        "strength_multiplier":self.strength_multiplier,
                        "damage_type":self.type
                }
class HealSkill(skill):
        def __init__(self, name, description, heal, ability_multiplier, self_only):
                super().__init__(name, description)
                self.heal = heal
                self.ability_multiplier = ability_multiplier
                self.self_only = self_only
        def use(self, user, target): 
                heal = self.heal + user.getStats()["Ability"] * self.ability_multiplier
                if self.self_only:
                        user.heal(heal)
                else:
                        target.heal(heal)
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "heal":self.heal,
                        "ability_multiplier":self.ability_multiplier,
                        "self_only":self.self_only
                }
class BuffSkill(skill): # Can also be used as a debuff skill if stat_changes are negative
        def __init__(self, name, description, stat_changes, duration):
                super().__init__(name, description)
                self.stat_changes = stat_changes # A dictionary of the stat changes provided by the buff skill, which can be applied to the character's stats when the skill is used
                self.duration = duration # The duration of the buff skill's effects in turns
        def use(self, user, target):
                effect = Effect(self.name, self.description, self.stat_changes, self.duration) # Create an effect based on the buff skill's stat changes and duration
                effect.apply(target)
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "stat_changes":self.stat_changes,
                        "duration":self.duration
                }

# Item Classes
class item:
        def __init__(self, name, description, usable):
                self.name = name
                self.description = description
                self.usable = usable
        def isUsable(self):
                return self.usable
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "usable":self.usable
                }
class weapon(item):
        def __init__(self, name, description, damage, effect, damage_type):
                super().__init__(name, description, False)
                self.damage = damage
                self.effect = effect
                self.damage_type = damage_type
        def attack(self, user, target):
                damage = self.damage + user.getStats()["Strength"] * 10
                target.damage(damage, user.level, self.damage_type)
                if self.effect:
                        self.effect.apply(target)
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "usable":self.usable,
                        "damage":self.damage,
                        "effect":self.effect.serialze(),
                        "damage_type":self.damage_type
                }
class accessory(item):
        def __init__(self, name, description, stat_bonus):
                super().__init__(name, description, False)
                self.stat_bonus = stat_bonus # A dictionary of the stat bonuses provided by the accessory, which can be applied to the character's stats when equipped
        def apply(self, character):
                for stat, bonus in self.stat_bonus.items():
                        character.stats[stat] += bonus
                character.statChanged()
        def remove(self, character):
                for stat, bonus in self.stat_bonus.items():
                        character.stats[stat] -= bonus
                character.statChanged()
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "usable":self.usable,
                        "stat_bonus":self.stat_bonus
                }
class healingItem(item):
        def __init__(self, name, description, heal_amount):
                super().__init__(name, description, True)
                self.heal_amount = heal_amount
        def use(self, user):
                user.heal(self.heal_amount)
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "usable":self.usable,
                        "heal_amount":self.heal_amount
                }
class boostItem(item):
        def __init__(self, name, description, stat_bonus, duration, effect):
                super().__init__(name, description, True)
                self.stat_bonus = stat_bonus # A dictionary of the stat bonuses provided by the boost item, which can be applied to the character's stats when used
                self.duration = duration # The duration of the boost item's effects in turns
                self.used = False # A flag indicating whether the boost item has been used
                self.effect = effect # The effect that the boost item applies
        def use(self, user):
                if not self.used:
                        self.effect.apply(user)
                        self.used = True
        def isUsed(self):
                return self.used
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "usable":self.usable,
                        "stat_bonus":self.stat_bonus,
                        "duration":self.duration,
                        "used":self.used,
                        "effect":self.effect.serialize()
                }

# Race Class
class race:
        def __init__(self, name, stats, abilities, possible_classes, baseHealth, speed, armor, healthModifier, speedModifier, armorModifier):
                self.name = name
                self.stats = stats
                self.health = baseHealth
                self.speed = speed
                self.armor = armor
                self.abilities = abilities # Basically passives provided by the race, like flight which gives the character a bonus to dodge agains non-flying enemies
                self.possible_classes = possible_classes
                self.baseHealth = baseHealth
                self.healthModifier = healthModifier
                self.speedModifier = speedModifier
                self.armorModifier = armorModifier 
        def classAllowed(self, char_class):
                return char_class in self.possible_classes
        def serializeAbilities(self):
                serializedAbilities = []
                for ability in self.abilities:
                        serializedAbilities.append(ability.serialize())
                return serializedAbilities
        def serializePClasses(self):
                serialziedPClasses = []
                for pclass in self.possible_classes:
                        #serialziedPClasses.append(pclass.serialize())
                        serialziedPClasses.append(pclass)
                return serialziedPClasses
        def serialize(self):
                return {
                        "name":self.name,
                        "stats":self.stats,
                        "health":self.health,
                        "speed":self.speed,
                        "armor":self.armor,
                        "abilites":self.serializeAbilities(),
                        "possible_classes":self.serializePClasses(),
                        "baseHealth":self.baseHealth,
                        "healthModifier":self.healthModifier,
                        "speedModifier":self.speedModifier,
                        "armorModifier":self.armorModifier
                }

# Class classes    
class char_class:
        def __init__(self, name, skills, starting_skills):
                self.name = name
                self.skills = skills # A dictionary of the skills that the character has when they choose this class keyed by level
                self.starting_skills = starting_skills # A list of the skills that the character starts with when they choose this class
        def levelUp(self, character):
                if character.level in self.skills:
                        character.skills.append(self.skills[character.level]) # Add the skill corresponding to the character's new level to their list of skills when they level up
        def serializeSkills(self,skills):
                serializedSkills = []
                for skill in skills:
                        serializedSkills.append(skill.seralize())                     
                return serializedSkills
        def serialize(self):
                return {
                        "name":self.name,
                        "skills":self.serializeSkills(self.skills),
                        "starting_skills":self.serializeSkills(self.starting_skills)
                }
class HiddenClass(char_class): # a class that will overhaul some aspects of the character's race when they reach level 20
        def __init__(self, fakeName, realName, skills, starting_skills, stat_changes, overhaul_abilities, overhaul_health, overhaul_speedMod, overhaul_armorMod,overhaul_healthMod):
                super().__init__(fakeName, skills, starting_skills)
                self.realName = realName
                self.stat_changes = stat_changes
                self.overhaul_abilities = overhaul_abilities
                self.overhaul_health = overhaul_health
                self.overhaul_speedMod = overhaul_speedMod
                self.overhaul_armorMod = overhaul_armorMod
                self.overhaul_healthMod = overhaul_healthMod
        def levelUp(self, character):
                super().levelUp(character)
                if character.level == 20: # At level 20, the character's overhaul class will take effect changing parts of the character's race
                        for stat, change in self.stat_changes.items():
                                character.stats[stat] += change
                        self.name = self.realName
                        character.statChanged()
                        character.race.abilities.extend(self.overhaul_abilities)        
                        character.race.baseHealth = self.overhaul_health
                        character.race.speedModifier = self.overhaul_speedMod
                        character.race.armorModifier = self.overhaul_armorMod
                        character.race.healthModifier = self.overhaul_healthMod
        def serializeSkills(self,skills):
                serializedSkills = []
                for skill in skills:
                        serializedSkills.append(skill.seralize())                     
                return serializedSkills
        def serialize(self):
                return {
                        "name":self.name,
                        "skills":self.serializeSkills(self.skills),
                        "starting_skills":self.serializeSkills(self.starting_skills),
                        "stat_changes":self.stat_changes,
                        "overhaul_abilities":self.serializeSkills(self.overhaul_abilities),
                        "overhaul_health":self.overhaul_health,
                        "overhaul_speedMod":self.overhaul_speedMod,
                        "overhaul_armorMod":self.overhaul_armorMod,
                        "overhaul_healthMod":self.overhaul_healthMod
                }

# Effect Class
class Effect:
        def __init__(self, name, description, stat_changes, duration):
                self.name = name
                self.description = description
                self.stat_changes = stat_changes # A dictionary of the stat changes provided by the effect, which can be applied to the character's stats when the effect is active
                self.duration = duration # The duration of the effect in turns
        def apply(self, character):
                for stat, change in self.stat_changes.items():
                        character.stats[stat] += change
                character.statChanged()
                character.active_effects.append(self)
        def remove(self, character):
                for stat, change in self.stat_changes.items():
                        character.stats[stat] -= change
                character.statChanged()
                if self in character.active_effects:
                        character.active_effects.remove(self)
        def tick(self, character):
                self.duration -= 1
                if self.duration <= 0:
                        self.remove(character)
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "stat_changes":self.stat_changes,
                        "self.duration":self.duration
                }

# Passive Classes
class Passive:
        def __init__(self, name, description):
                self.name = name
                self.description = description
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description
                }
class StaticPassive(Passive):
        def __init__(self, name, description, stat_changes):
                super().__init__(name, description)
                self.stat_changes = stat_changes
        def apply(self, character):
                for stat, change in self.stat_changes.items():
                        character.stats[stat] += change
                character.statChanged()
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "stat_changes":self.stat_changes
                }
class ResistancePassive(Passive):
        def __init__(self, name, description, damage_type, resistance_amount):
                super().__init__(name, description)
                self.damage_type = damage_type
                self.resistance_amount = resistance_amount # percentage of damage reduced eg 20 for 20% resistance
        def applyResistance(self, damage, damage_type):
                if damage_type == self.damage_type:
                        damage *= (100 - self.resistance_amount) / 100 # Reduce the damage by the resistance amount percentage
                return damage
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "damage_type":self.damage_type,
                        "resistance_amount":self.resistance_amount
                }
class DodgePassive(Passive):
        def __init__(self, name, description, dodge_bonus):
                super().__init__(name, description)
                self.dodge_bonus = dodge_bonus # A bonus to the character's dodge chance provided by the dodge passive
        def applyDodgeBonus(self, character, attacker):
                return self.dodge_bonus # Return the dodge bonus provided by the dodge passive
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "dodge_bonus":self.dodge_bonus
                }
class FlightPassive(DodgePassive):
        def __init__(self):
                super().__init__("Flight", "The ability to fly, providing a bonus to dodge against non-flying enemies.", 0.2)
        def applyDodgeBonus(self, character, attacker):
                for ability in attacker.race.abilities:
                        if isinstance(ability, FlightPassive):
                                return 0 # If the attacker also has flight, the dodge bonus from this passive does not apply
                return self.dodge_bonus # If the attacker does not have flight, apply the dodge bonus from this passive
class RegenerationPassive(Passive):
        def __init__(self, heal_amount):
                super().__init__("Regeneration", "The ability to regenerate health at the end of each turn.")
                self.heal_amount = heal_amount # The amount of health that the character regenerates at the end of each turn
        def tick(self, character):
                character.heal(self.heal_amount) # Heal the character by the heal amount at the end of each turn
        def serialize(self):
                return {
                        "name":self.name,
                        "description":self.description,
                        "heal_amount":self.heal_amount
                }

# Defined Races Below here does not need serialization functions
class Human(race):
        def __init__(self):
                super().__init__(
                        "Human", # The name of the race
                        {"Strength": 5, "Dexterity": 5, "Constitution": 5, "Intelligence": 10, "Ability": 15}, # Base stats
                        [], # A list of the human's abilities, which can be passive abilities
                        ["Super", "Human Soldier", "GDA Agent", "Citizen"], # A list of the classes that the human can choose from
                        100, # Base health
                        30, # Base speed
                        0, # Base armor
                        10, # Health modifier, the amount added to the character's health for each point of Constitution
                        1, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )
class Viltrimite(race):
        def __init__(self):
                super().__init__(
                        "Viltrumite",
                        {"Strength": 50, "Dexterity": 50, "Constitution": 75, "Intelligence": 10, "Ability": 5},
                        [FlightPassive(), RegenerationPassive(10), Passive("Enhanced Senses", "The ability to see in the dark and have enhanced vision."), Passive("Longevity", "The Viltrumite's long lifespan makes them resistant to aging effects."), ResistancePassive("Heat Resistance", "The Viltrumite's physiology provides resistance to extreme heat.", "heat", 30),ResistancePassive("Cold Resistance", "The Viltrumite's physiology provides resistance to extreme cold.", "cold", 30), ResistancePassive("Electricity Resistance", "The Viltrumite's physiology provides resistance to electricity.", "electric", 10), ResistancePassive("Poison Resistance", "The Viltrumite's physiology provides resistance to poison.", "poison", 10), ResistancePassive("Physical Resistance", "The Viltrumite's physiology provides resistance to physical damage.", "physical", 20)],
                        [" Viltrumite Scout", "Viltrumite Warrior", "Viltrumite Brute", "Viltrumite Elite"],
                        600, # Base health
                        50, # Base speed
                        20, # Base armor
                        50, # Health modifier, the amount added to the character's health for each point of Constitution
                        1.5, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1.5 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )
class Martian(race):
        def __init__(self):
                super().__init__(
                        "Martian",
                        {"Strength": 15, "Dexterity": 15, "Constitution": 15, "Intelligence": 5, "Ability": 20},
                        [FlightPassive(), RegenerationPassive(5), ResistancePassive("Electricity Resistance", "The Martian's physiology provides resistance to electricity.", "electric", 20)],
                        ["Martian Noble", "Martian Soldier", "Martian Spy"],
                        150, # Base health
                        30, # Base speed
                        5, # Base armor
                        15, # Health modifier, the amount added to the character's health for each point of Constitution
                        1, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )
class Flaxian(race):
        def __init__(self):
                super().__init__(
                        "Flaxian",
                        {"Strength": 5, "Dexterity": 5, "Constitution": 10, "Intelligence": 20, "Ability": 5},
                        [],
                        ["Flaxian Commonor", "Flaxian Noble", "Flaxian Technician"],
                        100, # Base health
                        30, # Base speed
                        5, # Base armor
                        10, # Health modifier, the amount added to the character's health for each point of Constitution
                        1.2, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )
class Demon(race):
        def __init__(self):
                super().__init__(
                        "Demon",
                        {"Strength": 25, "Dexterity": 10, "Constitution": 20, "Intelligence": 5, "Ability": 10},
                        [ResistancePassive("Fire Resistance", "The Demon's physiology provides resistance to fire.", "fire", 50)],
                        ["Demon Commonor", "Demon Noble", "Demon Brute"],
                        200, # Base health
                        25, # Base speed
                        10, # Base armor
                        20, # Health modifier, the amount added to the character's health for each point of Constitution
                        0.8, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )
class Thraxian(race):
        def __init__(self):
                super().__init__(
                        "Thraxian",
                        {"Strength": 5, "Dexterity": 5, "Constitution": 2, "Intelligence": 10, "Ability": 5},
                        [ResistancePassive("Poison Resistance", "The Thraxian's physiology provides resistance to poison.", "poison", 40)],
                        ["Thraxian Hybrid", "Thraxian Common", "Thraxian Scout"],
                        150, # Base health
                        35, # Base speed
                        10, # Base armor
                        15, # Health modifier, the amount added to the character's health for each point of Constitution
                        1.3, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1.2 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )
class Unopan(race):
        def __init__(self):
                super().__init__(
                        "Unopan",
                        {"Strength": 30, "Dexterity": 10, "Constitution": 30, "Intelligence": 5, "Ability": 5},
                        [ResistancePassive("Physical Resistance", "The Unopan's physiology provides resistance to physical damage.", "physical", 40)],
                        ["Unopan Brute", "Unopan Technician", "Unopan Genetic Abomination"],
                        250, # Base health
                        20, # Base speed
                        15, # Base armor
                        25, # Health modifier, the amount added to the character's health for each point of Constitution
                        0.7, # Speed modifier, the amount multiplied by the character's Dexterity to determine their speed
                        1.5 # Armor modifier, the amount multiplied by the character's Constitution to determine their armor
                )

# Defined Classes
class SuperHumanSuperSoldier(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Citizen",
                        "Super Soldier",
                        {}, #Skills keyed by level
                        [], #Skills as a list to start with
                        {"Strength":25,"Constitution":20,"Dexterity":15},
                        [],
                        150,
                        1.15,
                        1.25,
                        20
                )
# Skills for Super Soldier

class SuperHumanSpeedster(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Speedster",
                        {}, #skills keyed by level
                        [], #Skills as a list to start with
                        {"Dexterity":55,"Constitution":10,"Ability":10},
                        [], # List of abilities
                        120,
                        2,
                        1,
                        10
                )
# Skills for Speedster

class SuperHumanEnergy(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Energy Manipulatior",
                        {}, #Skills keyed by level
                        [], #Starting Skills list
                        {"Constitution":10,"Dexterity":20,"Ability":30},
                        [], # List of abilities
                        135,
                        1.25,
                        1.15,
                        10
                )
# Skills for Energy

class SuperHumanPsychic(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Psychic",
                        {}, #Skills keyed by level
                        [], #Starting skills
                        {"Ability":40},
                        [], # list of abilites
                        110,
                        1,
                        1,
                        10
                )
# Skills for Psychic

class SuperHumanViltrumiteHybrid(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Citizen",
                        "Viltrumite Hybrid",
                        {}, #Skills keyed by level
                        [], #Starting skills
                        {"Strength": 45, "Dexterity": 45, "Constitution": 70, "Ability":-10},
                        [], # Overhaul Abilities
                        600,
                        1.75,
                        1.5,
                        50,
                )
# Skills for Viltrumite Hybrid

class HumanSoldier(char_class):
        def __init__(self):
                super().__init__(
                        "Soldier",
                        {}, #Skills keyed by level
                        [] # Starting Skills
                )
# Skills for Human Soldier

class GDAAgent(char_class):
        def __init__(self):
                super().__init__(
                        "GDA Agent",
                        {}, #Skills keyed by level
                        [] # Starting SKills
                )
# Skills for GDA Agent

class HumanCitizen(char_class):
        def __init__(self):
                super().init(
                        "GDA Agent",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Citizen

class ViltrumiteScout(char_class):
        def __init__(self):
                super().__init__(
                        "Scout",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for V Scout

class ViltrumiteWarrior(char_class):
        def __init__(self):
                super().__init__(
                        "Warrior",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for V Warrior

class ViltrumiteBrute(char_class):
        def __init__(self):
                super().__init__(
                        "Brute",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for V Brute

class ViltrumiteElite(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Warrior",
                        "Elite",
                        {}, #Skills keyed by level
                        [], #Starting Skills
                        {"Strength": 50, "Dexterity": 50, "Constitution": 75, "Intelligence": 10, "Ability": 5},
                        [],
                        1200,
                        2,
                        2,
                        80
                )
# Skills for V Elite

class MartianNoble(char_class):
        def __init__(self):
                super().__init__(
                        "Noble",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Mar Noble

class MartianSoldier(char_class):
        def __init__(self):
                super().__init__(
                        "Soldier",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Mar Soldier

class MartianSpy(char_class):
        def __init__(self):
                super().__init__(
                        "Spy",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Mar Spy

class FlaxianCommon(char_class):
        def __init__(self):
                super().__init__(
                        "Common",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Flax Common

class FlaxianNoble(char_class):
        def __init__(self):
                super().__init__(
                        "Noble",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Flax Noble

class FlaxianTech(char_class):
        def __init__(self):
                super().__init__(
                        "Brute",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Flax Tech

class DemonCommon(char_class):
        def __init__(self):
                super().__init__(
                        "Common",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Demon Common

class DemonNoble(char_class):
        def __init__(self):
                super().__init__(
                        "Noble",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Demon Noble

class DemonBrute(char_class):
        def __init__(self):
                super().__init__(
                        "Brute",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Demon Brute

class ThraxianCommon(char_class):
        def __init__(self):
                super().__init__(
                        "Common",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Thrax Common

class ThraxianScout(char_class):
        def __init__(self):
                super().__init__(
                        "Scout",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Thrax Scout

class ThraxianHybrid(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Common",
                        "Hybrid",
                        {},
                        [],
                        {"Strength": 40, "Dexterity": 45, "Constitution": 63},
                        [],
                        450,
                        1.75,
                        1.25,
                        40
                )
# Skills for Trax Hybrid

class UnopanBrute(char_class):
        def __init__(self):
                super().__init__(
                        "Brute",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Unopan Brute

class UnopanTech(char_class):
        def __init__(self):
                super().__init__(
                        "Technician",
                        {}, #Skills keyed by level
                        [] #Starting Skills
                )
# Skills for Unopan Tech

class GeneticAbomination(HiddenClass):
        def __init__(self):
                super().__init__(
                        "Technician",
                        "Genetic Abomination",
                        {},
                        [],
                        {"Strength": 20, "Dexterity": 40, "Constitution": 40,"Intelligence":10,"Ability":15},
                        [],
                        450,
                        1.65,
                        1.25,
                        40
                )
# Skills for Genetic Abomination


# Defined SKills I need to have at least one skill every 10 levels for each class up to level 100, with 3 strarting skills for each class
print("Invincible Data Loaded!")


# Testing stuff

def upgradeAll(character):
        character.useStat_points("Strength",1)
        character.useStat_points("Dexterity",1)
        character.useStat_points("Constitution",1)
        character.useStat_points("Intelligence",1)
        character.useStat_points("Ability",1)

c = player("Mark",20,ViltrumiteElite(),Viltrimite())
c2 = player("Oliver",5,ThraxianHybrid(),Thraxian())
upgradeAll(c)
upgradeAll(c)
upgradeAll(c2)
upgradeAll(c2)
serializedPlayer = c.serialize()
for i in range(1,100000):
        c.levelUp()
        c2.levelUp()
        upgradeAll(c)
        upgradeAll(c2)
print(c2)
c2.attack(c)
c.attack(c2)
print(c)


