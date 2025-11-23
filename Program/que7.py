#Linear Search 
list = [1 , 2, 3, 4, 5, 6, 7 , "Hello madarchod ! ", 8, 9 , 10  ]
target = int(input("Enter a target number : "))
idx = 0 

for num in list :
    if num == target :
        print(f"target found at index {idx}")
        break 
    idx += 1 
