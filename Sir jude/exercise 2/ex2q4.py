packages = eval(input("Enter the number of packages purchased: "))


if 9 < packages < 20:
    discount = 10/100 * (99 * packages);
    print("Discount amount @ 10%: ", "${:,.2f}".format(discount))
    print ('Total amount: ', "${:,.2f}".format((99 * packages)-discount))
elif 19 < packages < 50:
    discount = 20/100 * (99 * packages);
    print("Discount amount @ 20%: ", "${:,.2f}".format(discount))
    print ('Total amount: ', "${:,.2f}".format((99 * packages)-discount))
elif 49 < packages < 100:
    discount = 30/100 * (99 * packages);
    print("Discount amount @ 30%: ", "${:,.2f}".format(discount))
    print ('Total amount: ', "${:,.2f}".format((99 * packages)-discount))
elif 99 < packages:
    discount = 40/100 * (99 * packages);
    print("Discount amount @ 40%: ", "${:,.2f}".format(discount))
    print ('Total amount: ', "${:,.2f}".format((99 * packages)-discount))
else:
    print("Invalid")
