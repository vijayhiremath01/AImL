# to count the number of digits in a number 
def count_digits(number):
    count = 0
    while number > 0 :
        number = number // 10 
        count += 1 
    return count
    
number = int(input("Enter a number : "))

result = count_digits(number)
print("Number of digits :", result)