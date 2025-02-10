class Clothe:
    def __init__(self, name, colour, size):
        self.name = name
        self.colour = colour
        self.size = size


class Shirt(Clothe):
    def get_colour(self):
        print(self.colour)
    def get_size(self):
        print(self.size)


class Jeans(Clothe):
    def __init__(self, name, colour, size):
        super().__init__(name, colour, size)
        print("jeans-coloured")


sh = Shirt("shirt", "yellow", 37)
sh.get_colour()
sh.get_size()

jeans = Jeans("jeans", "black", 37)
print(jeans.colour)
print(jeans.size)
