salary = int(input("Enter your monthly salary: "))

if salary < 30000:
    tax = salary * 0.05
elif 30000 <= salary <= 70000:
    tax = salary * 0.15
elif salary > 70000:
    tax = salary * 0.25
else:
    tax = 0

print(f"The calculated tex on your salary is : {tax}")