# continuosly taking input from user until user enters 'exit' and printing whether number is negative or positive 

while True :
    number = input("Enter a numbers to check positive or negative (or type 'exit' to quit) : ")
    if number == 'exit' or number == 'EXIT' or number == 'Exit' or number == 'ExIt' :
        print("Exiting the program.")
        break 
    # ...exiting code...
    number = int(number)
    if number >= 0:
        print(f"{number} is a positive number ")
    else:
        print(f"{number} is a negative number ")


