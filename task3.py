class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"Mahsulot: {self.name}, Narx:{self.price},miqdor: {self.quantity}"


    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor xolos")
        else:
            self.quantity -= amount

    def restock(self, amount):
            self.quantity += amount


class Food(Product):
    def __init__(self, name, price, quantity, sirok):
         super().__init__(name,price,quantity,)
         self.sirok = sirok

    def info(self):
        data = super().info()
        data += f" || sirok :{self.sirok}"
        return data


class Electronics(Product):
    def __init__(self, name, price, quantity,  warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f"||warranty: {self.warranty}"
        return data

# e = Electronics("A", 100, 12, "1 yil")
# print(e.info())

f = Food("banan",23,67,"1 yil")
print(f.info())