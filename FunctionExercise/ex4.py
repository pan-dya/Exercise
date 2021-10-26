def calc_new_height():
    width = eval(input("Enter the current width: "))
    height = eval(input("Enter the current height: "))
    width2 = eval(input("Enter the desired width: "))
    divider = width2 / width 
    height2 = divider * height
    print("The corresponding height is", height2)

calc_new_height()