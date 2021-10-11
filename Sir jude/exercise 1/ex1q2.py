v = eval(input("Enter the plane's take off speed in m/s: "))
a = eval(input("Enter the plane's acceleration in m/s**2: "))

calculation = v**2 / (2*a)
roundcalc = round(calculation, 4)

print('The minimum runway length neede for this airplane is', calculation, 'meters.')