class Student :
    college_name = "IIT Madras" #class Attribute

    def __init__(self , name , cgpa) : #parameterized constructor
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Vijay" , 9.8)
print(stu1.name) #by object we can access the both type of attributes (instance and class attributes)
print(stu1.cgpa)
print(Student.college_name) #by class we can access the class attributes only (not instance attributes)

# so the priority is given to instance attributes over class attributes

