principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle : "))
    if principle <= 0:
        print(f"Principle cannot be less than or equal to zero") 

while rate <= 0:
    rate = float(input("Enter the Interest rate : "))
    if rate <= 0:
        print(f"Interest rate cannot be less than or equal to zero") 

while time <= 0:
    time = float(input("Enter the time in years : "))
    if time <= 0:
        print(f"Time in years cannot be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: {total:.2f}")