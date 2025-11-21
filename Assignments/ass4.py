#sum of digits in a number 
def sum_of_digits(number):
    total = 0 
    while number > 0 :
        digit = number % 10
        total += digit 
        number = number // 10 
    return total 

number = int(input("Enter a number : "))
result = sum_of_digits(number)
print(f"Sum of digits in {number} is {result}")