class Transport:
    def __init__(self, name,speed):
        self.name = name
        self.speed = speed

    def info (self):
        print(f"The name of the vehicle is {self.name} and the speed is {self.speed}")


class Car(Transport):
     def info(self):
         print(f"The name of the car is {self.name} and the speed is {self.speed} tezlikda yurmowda")






class Bicycle(Transport):
      def info(self):
         print(f"bu  {self.name} nomli velosiped and the speed is {self.speed} ")

c = Car("Mers", 180)
c.info()
b = Bicycle("Gonchik", 10)
b.info()


