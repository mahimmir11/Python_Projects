unit = input("Is this the tempreature in Celcius or Fahrenheit? (C/F) : ")
temp = float(input("Enter the tempreature : "))

if unit == 'C':
    temp = round((9 * temp)/ 5 + 32, 1)
    print(f"The tempreature in Fahrenhite is: {temp}F")
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The tempreature in Celcius is {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")