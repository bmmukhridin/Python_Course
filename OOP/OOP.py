# OOP

class PlayerCharacter:
    # Class Object Attrubute
    membership = True
    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")
        return "Done"
    
    def run(self, hello):
        print("hello")



player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 22)
player2.attack = 50

print(player1.shout())
print(player2.age)
