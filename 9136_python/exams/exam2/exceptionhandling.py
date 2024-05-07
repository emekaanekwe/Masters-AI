import unittest

'''TYPES OF ERRORS'''
#NameError - when a value is used before being instantiated
#ValueError - when a funct receives correct input, but invalid value (e.g. passing -9 in sqrt())

def add(x,y):
    return x+y

class Testing(unittest.TestCase):
    def sum(self):
        self.assertEqual(add(1,2), 3)
    

age = 100
#the program is killed at the line below
#assert(age > 100), "The age is too high"

import array
x = 5.0

try:
    x / 3
except ZeroDivisionError:
    print("wrong")
else:
    print("ok")
finally:
    print("complete")

a = array.array = [1,2,3, "4"]
print(a)
a.append(1)
print(a)

if __name__ == "__main__":
    unittest.main()