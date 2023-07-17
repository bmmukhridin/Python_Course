# OOP

class PlayerCharacter:
    # Class Object Attrubute
    membership = True
    def __init__(self, name="anonymous", age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")
        return "Done"
    
    @classmethod
    def run(cls, num1,num2):
        return num1 + num2



player1 = PlayerCharacter("Tom", 19)
player2 = PlayerCharacter()
player2.attack = 50

print(player1.run(2,3))


# class Cat:
#     species = "mammal"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         return

    
# cat1 = Cat("Tom", 10)
# cat2 = Cat("Jim", 5)
# cat3 = Cat("Jerry", 15)

# def all_ages(*args):
#     return max(args)

# print(f"oldest cat is {all_ages(cat1.age,cat2.age,cat3.age)}")




        