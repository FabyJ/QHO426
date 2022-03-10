salary = float(input("Enter salary: "))
years = int(input("Enter number of years: "))

if years > 2:
    if salary < 25000:
        salary = salary * 1.1
        print(f"Your new salary will be £{salary}")
    else:
        salary = salary + 100
        print(f"Small change, you will now earn £{salary}")
elif years >= 1:
    print("No salary increase for you. Sorry!")
else:
    if salary < 15000:
        print("Ooopsie! YOur salary should be £20000")
        salary = 20000
print("Let us work for the good of the company!")