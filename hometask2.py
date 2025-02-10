class Clothe:
    def __init__(self, name,colour,size):
        self.name = name
        self.colour = colour
        self.size = size

class Shirt(Clothe):
        super().size()


    def colour(self):
        print("yellow")
    def size(self):
        print(37)

class Jeans(Clothe):
        super().size()
        print("jeans-coloured")



sh = Shirt("shirt", "yellow", 37)
sh.colour()
sh.size()
jeans = Jeans("jeans", "black", 37)
jeans.colour()
jeans.size()