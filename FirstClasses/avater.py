
class Avatar:
    def __init__(self):
        name = "no name"
        experience = 1
        equipment = []
        health = 4

    def status(self):
        print("Info about {}".format(self.name))
        print("Experience of {}".format(self.experience))
        print("Equipment list is {}".format(len(self.equipment)))
        if self.health > 5:
            print("This avatar is healthy!")
        elif 0 < self.health < 5:
            print("This avatar is ill, take some precautions!")
        else:
            print("This avatar is dead, Game Over!")
