import uuid


class Product:
    def __init__(self, name, price, quantity):
        self.__id = uuid.uuid4()
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






class Basket:
    def __init__(self):
        self.__id = uuid.uuid4()
        self.data = []

    def add(self, product, price):
        self.data.append({'product': product, 'price': price})
        print(f"{product} ({price}) qo'shildi.")

    def remove(self, product):
        for item in self.data:
            if item['product'] == product:
                self.data.remove(item)
                print(f"{product} ---1.")
                return
        print(f"{product} yo'q.")

    def show(self):
        if not self.data:
            print("bo'sh.")
        else:
            print("bor mahsulotlari:")
            for item in self.data:
                print(f"- {item['product']}: {item['price']}")

    def calculating(self):
        total = sum(item['price'] for item in self.data)
        print(f"Total price: {total}")


basket = Basket()
# basket.add("qulupnay", 2)
# basket.add("kiwi", 1)
basket.show()
# basket.calculating()
# basket.remove("qulupnay")
# basket.show()







