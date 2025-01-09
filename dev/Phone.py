#When to use class methods and when to use static methods ?
from Item import Item
class Phone(Item):
    
    phone = []
    def __init__(self, name: str, price: float, quantity=0, brokenphones=0) -> None:
        
        super().__init__(name, price, quantity)
        
        #Run  validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = brokenphones
        
        Phone.phone.append(self)

item1 = Phone("Phone", 100, 5, 1)
print(item1.broken_phones)
#print(item1.calculate_total_price())
print(Item.all)
print(Phone.phone)