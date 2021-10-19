rows = eval(input("How many rows?:"))

for i in range(rows):
    print("  "*(rows - i),end="")
    for j in range(0,i + 1):
        print("*",end=" ")
    print()