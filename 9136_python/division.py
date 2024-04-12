#NOTE: Python, by default, rounds down and thus must be coded to 
    #round up if needing to

#test operands
p1 = 1
p5 = 5
p7 = 7
p11 = 11

e2 = 2
e4 = 4
e6 = 6
e8 = 8

f2 = 2.0
f5 = 5.0
f15p = 15.343579
f20p = 20.99988

# store the values of above vars into a list
variable_names = dir()

values_dict = {}

for name in variable_names:
    if not callable(eval(name)) and name.startswith('p'):
        (eval(name))

# Print the list of values
print("List of values:", values_li)



dict_divisors = {}
print("dict", dict_divisors)
if len(dict_divisors) == 0:
    pass
        
    

def get_modulo(x,y):
    return x % y

def get_float_quotient(x,y) -> float:
    return x / y

def get_floor_quotient(x,y) -> int:
    return x // y



#interprete f(int, int)
'''
print(get_modulo(e8, e2))
print(get_modulo(e2, e8))
print(get_float_quotient(e6,e2))
print(get_float_quotient(e2,e6))
print(get_floor_quotient(e8,e4))
print(get_floor_quotient(e4,e8))
#interpret f(int, float)
print(get_modulo(e8, e2))
print(get_modulo(e2, e8))
print(get_float_quotient(e6,e2))
print(get_float_quotient(e2,e6))
print(get_floor_quotient(e8,e4))
print(get_floor_quotient(e4,e8))
'''