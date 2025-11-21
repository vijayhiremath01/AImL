# number = input("Enter a number : ")

# for i in number :
#     print(i)
    
# using maths function 
def print_number(number):
    while number > 0 :
        digit = number % 10 
        print(digit)
        number = number // 10 

number = int(input("Enter a number : "))

print_number(number)

# from here i learned how does the // operator works in python 
