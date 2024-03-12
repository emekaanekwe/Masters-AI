num1 = int(input("Please enter the value of number 1:"))
num2 = int(input("Please enter the value of number 2:"))
def gcd(num1, num2):
    if num1 == num2:
        return num1
    if num1 < num2:
        return gcd(num2, num1)
    else:
        return gcd(num2, num1 - num2)

print("The greatest common divisor is: ", end='')        
print(gcd(num1,num2))
