def convert_temp():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit:"))
    convert_to_celcius(fahrenheit)

def convert_to_celcius(fahrenheit):
    tc = (5/9) * (fahrenheit - 32)
    print("The temperature in Celcius is", tc)
    convert_to_kelvin(tc)

def convert_to_kelvin (tc):
    tk = tc + 273.15
    print("The temperature in Kelvin is", tk)

convert_temp()