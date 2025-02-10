class Person:
    def __init__(self, name,fam):
        self.name = name
        self.fam = fam

    def hi(self):
        print("Hi, I'm", self.name)


class English(Person):
      pass

class Uzbek(Person):
    def hi(self):
        super().hi()
        print("Salom mening ismim", self.name)


u = Uzbek("Shuhrat", "Fayzulloyev")
u.hi()
e = English("Jack", "Bond")
e.hi()
