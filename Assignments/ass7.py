# function for prime or not retun true or false 

def is_prime(n):
    if n <= 1 :
        return False
    for i in range(2 , int(n**0.5) + 1 ):
        if n % i == 0 :
            return False 
    return True    

number = int(input("Enter a number : "))
print(is_prime(number))