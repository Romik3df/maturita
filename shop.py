class ShopCart:
    def __init__(self):
       
        self.items = []
        self.total_price = 0.0

    def addItem(self, name, price):
        
        self.items.append((name, price))
        self.total_price += price

    def removeItem(self, name):
        
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                self.total_price -= item[1]
                break
        else:
            print(f"Položka '{name}' nebola nájdená v košíku.")

    def printContent(self):
       
        if self.items:
            print("Položky v nákupnom košíku:")
            for item in self.items:
                print(f"- {item[0]}: {item[1]} EUR")
            print(f"Celková cena: {self.total_price} EUR")
        else:
            print("Nákupný košík je prázdny.")


cart = ShopCart()
cart.addItem("Jablko", 1.2)
cart.addItem("Banán", 0.8)
cart.addItem("Maso", 1.5)
cart.printContent()

cart.removeItem("Banán")
cart.printContent()

cart.removeItem("Hrozno") 
