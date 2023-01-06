# create a class
class User:	
    # attributes for each instance of the class (also called an object)
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # methods for each instance of the class
    def greeting(self):
    	print(f"Hello, my name is {self.name}")

# ? -----------------------------------------

# create a class
class Shoe:
    # attributes
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

    def on_sale_by_percent(self, percent_off):
        self.price *= (1 - percent_off)
        return self




# ? TESTING AREA BELOW -----------------------
river = User("River", "river@tardis.com")
river.greeting()

nike_shoe = Shoe("Nike", "Running", 200)
print(nike_shoe.on_sale_by_percent(.2).price)