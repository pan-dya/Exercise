import math

mass = eval(input("Enter the mass of the cart(in kg): "))
force = eval(input("Enter the force to push the cart (in N): "))
gravity = 9.8
sin_teta = force / (mass * gravity)

radians = math.asin(sin_teta)

result = round (math.degrees(radians), 1)

print('The angle of the ramp is', result)