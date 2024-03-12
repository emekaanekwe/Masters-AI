from math import sqrt
# Given A B and C
x_final = float(input("Please enter the final location"))
x_initial =float(input("Please enter the initial location."))
v = float(input("Please enter the velocity."))
a = float(input("Please enter the acceleration."))

A = 0.5*a # Please enter your code for finding the value of A based on Part 2.
B = v# Please enter your code for finding the value of B based on Part 2.
C = x_initial - x_final# Please enter your code for finding the value of C based on Part 2.

discriminant = B**2-4*A*C

# Please enter your code here for importing the required math method (i.e., sqrt).
if discriminant > 0:
    t_1 = (-1.0*B+sqrt(discriminant))/(2*A)
    t_2 = (-1.0*B-sqrt(discriminant))/(2*A)
    print("sentence")
elif discriminant == 0:
    t = -1*B/(2*A)
    print(f"sentence")
else:
    print("sentence")

# Please enter your code here for computing and displaying all movement duration(s) of Robbie based on Part 1.