number_1 = eval(input("Enter the first number:"))
number_2 = eval(input("Enter the second number:"))

question= input('Do you want to \n A. + \n B. X \n C. / \n D. - \n [A/B/C/D] ?')
if question == "A" :
    print(number_1 + number_2)
elif question == "B" :
    print(number_1 * number_2)
elif question == "C" :
    print (number_1 / number_2)
elif question == "D" :
    print (number_1 - number_2)
else :
    print("error!")
