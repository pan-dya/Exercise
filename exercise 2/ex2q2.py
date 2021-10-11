e1 = eval(input("Enter length of edge 1: "))
e2 = eval(input("Enter length of edge 2: "))
e3 = eval(input("Enter length of edge 3: "))
perimeter = e1 + e2 + e3

if (e1 + e2) < e3 or (e1 + e3) < e2 or (e2+e3) < e1:
    print ("Perimeter cannot be calculated")
else:
    print ('The perimeter is', perimeter)