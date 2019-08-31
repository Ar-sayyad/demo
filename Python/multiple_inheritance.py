class Father():
    def skills(self):
        print("Gardening, programming")

class Mother():
    def skills(self):
        print("arts, cooking")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")


c = Child()
c.skills()