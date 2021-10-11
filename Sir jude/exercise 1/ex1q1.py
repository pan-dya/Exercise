x1 = eval(input("Enter the first x coordinate point: "))
y1 = eval(input("Enter the first y coordinate point: "))
x2 = eval(input("Enter the second x coordinate point: "))
y2 = eval(input("Enter the second y coordinate point: "))

slope = ((y2-y1)/(x2-x1))
formatSlope = round(slope, 5)
print('the slope for the line that connects two points', (x1, x2), 'and', (y1,y2), 'is', formatSlope)