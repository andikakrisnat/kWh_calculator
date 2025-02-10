#input all data
w = float(input("How much power (W)? "))
h = float(input("How many hours/day? "))
print("(A) 1.300 VA")
print("(B) 2.200 VA")
print("(C) 3.500-5.500 VA")
print("(D) 6.600 VA")
d = input("How much voltage (VA)? ")

#rate for every group
A = 1.444
B = 1.444
C = 1.669
D = 1.669

#calculating kWh
daily = w * h / 1000
weekly = daily * 7
monthly = daily * 30

#convert variable
float(daily)
float(weekly)
float(monthly)

#calculating rate
if d.upper() == "A":
    daily_price = daily * A
    weekly_price = weekly * A
    monthly_price = monthly * A
elif d.upper() == "B":
    daily_price = daily * B
    weekly_price = weekly * B
    monthly_price = monthly * B
elif d.upper() == "C":
    daily_price = daily * C
    weekly_price = weekly * C
    monthly_price = monthly * C
elif d.upper() == "D":
    daily_price = daily * D
    weekly_price = weekly * D
    monthly_price = monthly * D

#result
print("In a Day " + str(daily.__round__(2)) + " kWh = Rp " + str(daily_price.__round__(3)))
print("In a Week " + str(weekly.__round__(2)) + " kWh = Rp " + str(weekly_price.__round__(3)))
print("In a Month " + str(monthly.__round__(2)) + " kWh = Rp " + str(monthly_price.__round__(3)))
