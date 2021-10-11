subtotal = eval(input("Enter the subtotal ($): "))
tip = eval(input("Enter tip amount ( as a %) : "))

format_subtotal = "${:,.2f}".format(subtotal)
tip_result = (tip / 100) * subtotal
format_tip_result = "${:,.2f}".format(tip_result)
total = "${:,.2f}".format(subtotal + tip_result)

print(format_subtotal)
print(format_tip_result)
print(total)