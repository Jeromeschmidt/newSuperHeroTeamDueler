from ability import Ability
from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
      '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''
      # start our total out at 0
      total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`

    def defend(self, damage_amt):
      '''Calculate the total block amount from all armor blocks.
         return: total_block:Int
      '''
      # TODO: This method should run the block method on each armor in self.armors

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        pass

    def take_damage(self, damage):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      # TODO: Create a method that updates self.current_health to the current
      # minus the the amount returned from calling self.defend(damage).
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
      '''Return True or False depending on whether the hero is alive or not.
      '''
      # TODO: Check the current_health of the hero.
      # if it is <= 0, then return False. Otherwise, they still have health
      # and are therefore alive, so return True
      pass

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        pass

    def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      # TODO: Fight each hero until a victor emerges.
      # Phases to implement:
      # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
      # 1) else, start the fighting loop until a hero has won
      # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
      # 3) After each attack, check if either the hero (self) or the opponent is alive
      # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
      pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
