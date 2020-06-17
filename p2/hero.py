class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
      '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
      '''
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health


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
      winner = random.choice(self, opponent)
      print(str(winner.name) + " has won!")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
