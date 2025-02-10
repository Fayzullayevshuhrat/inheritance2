class Ship:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Moving...")
    def diving(self):
        print("Diving...")

class Airship(Ship):
        def fly(self):
            super().diving()
            print("Flying...")

sh = Ship("Titanic")
sh.move()
air = Airship("Beehive")
air.fly()