class laptop :
        storage_type = "SSD"

        def __init__(self , name , price , storage) :
                self.name = name 
                self.price = price
                self.storage = storage 
        
        def get_laptop_info(self) :
            print(f"The Name of laptop is {self.name} and its price is {self.price} which is having {self.storage} storage and the type of storage is {self.storage_type}")

lap1 = laptop("macBook" , 120000 , "512GB")
lap2 = laptop("Dell" , 80000 , "1TB") # we pass the information while creating the object

lap1.get_laptop_info()
lap2.get_laptop_info() #we take the info here ! 
