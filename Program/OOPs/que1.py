class studentName : 
    def __init__(self , name) : #parameterized constructor
        self.name = name 

    def get_name(self) : #default constructor
        return self.name

for i in range(5) :
    name = input("Enter Your name : ")
    student = studentName(name)
    print(student.name)


print(student.get_name())