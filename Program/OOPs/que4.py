class laptop :
        storage_type = "SSD"

        def __init__(self , RAM , storage):
                self.RAM = RAM 
                self.storage = storage 
        
        def get_laptop_info(self) :
                print(f"The laptop has {self.RAM} RAM and {self.storage} storage and the type of storage is {self.storage_type}") #instance method here we can access instance variables and class variables 
        
        @classmethod
        def get_storage_info(cls):
                print(f"The type of storage is {cls.storage_type}") # we can access class variables using cls only 
        
        @staticmethod
        def cal_discount(price , discount) :
                final_price = price - (discount * price / 100 )
                print(f"{final_price} is discounted price ! ")

l1 = laptop("8GB" , "512GB")

l1.get_laptop_info()
l1.get_storage_info()
l1.cal_discount(12_0000 , 30)
