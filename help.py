class Animal :
    def __init__(self,name,):
        self.name = name

    def sound(self):
        print("sound")

class Dog(Animal):
    def sound(self):
        print("Bark")



class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog("qoravoy")
d.sound()
c = Cat("katyusha")
c.sound()