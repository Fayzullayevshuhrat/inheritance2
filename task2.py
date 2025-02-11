class Product:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self. quantity = quantity


    def info(self):
        print(f"mahsulotning nomi {self.name},narxi {self.price},miqdori {self.quantity} ")

    def sell(self,amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("mahsulot qolmadi")


        return self.quantity

    def restock(self,amount):
        self.quantity += amount
        return self.quantity


p = Product("samsung",1000,23)
p.info()
p.sell(23)
p.info()
p.restock(15)
p.info()


