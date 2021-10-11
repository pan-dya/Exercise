while True:
    try:
        temp1 = eval(input("Enter the temperature in Fahrenheit: ")) 
        if -58 < temp1 <41:
            break;
        else:
            print("The temperature is incorrect")      
    except ValueError:
        print("Invalid")
    continue

while True :
    try:
        windSpeed = eval(input("Enter the wind speed in miled per hour: "))
        if windSpeed >= 2:
            break;
        else:
            print ("Please enter the wind speed greater than or equal to 2 ")
    except ValueError:
        print ("Invalid")
    continue

windChill =  35.74 + 0.6215 * temp1 - 35.75 * windSpeed ** 0.16 + 0.4275 * temp1 * windSpeed ** 0.16

print('The wind chill index is', round(windChill, 3))