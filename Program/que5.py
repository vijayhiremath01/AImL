list = [1 , 2, 3, 4, 5, 6, 7, "Hello madarchod ! "]
print(list)
print(type(list))

for i in list :
    print(i)

list[0] = "Hello Benchod !"
print(list)

list.append("Hello Benchod !")
print(list)

list.remove("Hello Benchod !")
print(list)

list.pop()
print(list)

list.clear()