import csv
class Item:
    
    pay_rate = 10
    all = []
    
    def __init__(self, name: str, price: float, quantity=0) -> None:
        #Run  validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"

        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        print("Parent item")
        
                
        @property
        def name(self):
            return self.name
        
        #action to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"  
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('c:/projects/practice/python/python_practice/dev/item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(name=item.get('name'), price=int(item.get('price')), 
                 quantity=int(item.get('quantity'))) 
            
    @staticmethod        
    def is_integer(num):  
        # We will count out the floats that are point zero
        if isinstance(num, float):
            return num.is_integer() 
        elif isinstance(num, int):
            return True
        else:
            return False 
        
    @property
    def read_only_name(self):
        return "AAA"          
        

#item1 = Item("Phone", 100, 5)
#print(item1.calculate_total_price(item1.price, item1.quantity))
#item1.apply_discount()
#print(item1.price)

#item2 = Item("Laptop", 1000, 3)
#print(item2.calculate_total_price(item2.price, item2.quantity))
#print("Class level :",  Item.__dict__)
#print("--------------------------------------")
#print("Instance level :", item1.__dict__)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)
    
#Item.instantiate_from_csv()  
#print(Item.all)  
#print(Item.is_integer(7.0))  

# class Phone1(Item):
#     pass

# item1 = Phone1("Phone", 100, 5)
# print(item1.name)
