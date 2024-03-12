
'''
while True:
    num_1 = int(input("Please enter the value of number 1:"))
    num_2 = int(input("Please enter the value of number 2:"))
    if num_1 <=0 and num_2 <= 0:
        print("the number cannot be 0 or lower")
    else:
        break
'''     
#for ints x, y the GCD of x and y is gcd(x,y)
#euclid's algo: two positive ints a, b and a > b,the common 
# divisors of a and b are eqal to as common divisors of a-b and b
  
'''
for pos int a, b where a > b, gcd(a,b) = (a-b),b

48
30
12
'''      
#for 2 ints, but intended for getting gcd for a set of ints
# ex 60, 48
def gcd(div_1, div_2):
    if div_2 == 0: 
        return div_2
    else:
        return gcd(div_2, div_1 % div_2)

while True:
    div_1 = int(input("enter a number"))
    div_2 = int(input("enter another number"))
    if div_1 < 0 and div_2 < 0:
        print("neither number can be less than zero")
    else:
        break
result = gcd(60,48)
print(f" The greatest common divisor between {div_1} and {div_2}, via Euler's Method is:", result)


    


    
'''
            euclid_div[0] = s
        
        r -= s
        if r < 0:
            euclid_div[1] = r
            print(euclid_div)
            return euclid_div

'''
# Please enter your code here for computing the greatest common divisor of num_1 and num_2.

# Please enter your code here for displaying the greatest common divisor of num_1 and num_2.

