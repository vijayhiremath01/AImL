class Product :
        count = 0 
 
        def __init__(self , name , price ):
                self.name = name 
                self.price = price 
                Product.count += 1

        def get_product_info(self) : #instance method here we can access instance variables and class variables 
                print(f"The product name is {self.name} and its price is {self.price}")
        
        @classmethod
        def counter(cls) : 
                print(f"Total number os products created is {cls.count}")
        
        @staticmethod 
        def cal_discount(price , discount) :
                Final_price = price - (discount*price / 100 )
                print(f"{Final_price} is discounted price ! ")


product1 = Product("laptop" , 12_0000)
product2 = Product("Mouse" , 10000)

product1.get_product_info()
product2.get_product_info()

Product.counter()
product1.cal_discount(12_0000 , 17.5) 