import sys

"""Unit class contains all the details for each unit type. User must specify which type of unit they want to add to their fleet when they instantiate that unit. For example, unit = Unit('Carrier') - this will be handled with the command line args"""

class Unit():
    def __init__(self, type):
        self.type = type
        self.hp = 1
        self.hit = 0.1
        self.mov = 1
        self.capacity = 4

    def __str__(self):
        return f"{self.type} unit has {self.hp} HP and a {self.hit} chance of hit"

def main():
    args = sys.argv[1]
    
    unit = Unit("Carrier")
    print(unit)

if __name__ == "__main__":
    main()