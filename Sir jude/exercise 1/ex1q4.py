side_length = eval(input("Enter the sided length of the hexagon: "))

math = ((3*(pow(3, 1/2))) / 2 )* (pow(side_length, 2))
format_math = round(math, 3)

print ('The area of a hexagon with the side length', side_length, 'is', format_math)
