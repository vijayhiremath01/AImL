list = [1 , 2, 3, 4, 5, 6, 7, "Hello madarchod ! "]
print(list)
print(type(list))

for i in list :
    print(i)



#list methods 
nums = [1 , 2, 3,4,5 ]
print(len(nums))
# append method 
nums.append(6)
print("After appending")
print(nums)

# insert method 
nums.insert(2 , 10)
print("after insertions")
print(nums)

# remove method 
nums.remove(10)
print("after removing")
print(nums)

# pop method 
nums.pop()
print("after popping")
print(nums)

# clear method 
nums.clear()
print("after clearing")
print(nums)

# reverse method 
nums.reverse()
print("after reversing")
print(nums)

# sort method 
nums.sort()
print("after sorting")
print(nums)

# count method 
nums.count(1)
print("after counting")
print(nums)

# copy method 
nums.copy()
print("after copying")
print(nums)                 