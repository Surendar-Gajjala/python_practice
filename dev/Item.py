class Item:
    
    pay_rate = 10
    
    def __init__(self, name: str, price: float, quantity=0) -> None:
        #Run  validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self, x, y):
        return x * y
        


item1 = Item("Phone", 100, 5)
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("Laptop", 1000, 3)
print(item2.calculate_total_price(item2.price, item2.quantity))
print("Class level :",  Item.__dict__)
print("--------------------------------------")
print("Instance level :", item1.__dict__)