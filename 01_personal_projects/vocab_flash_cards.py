import random as ran

def mat():
    funct_list = ["linear", "quadratic", "cubic", "exponential", "inverse even", "inverse odd", "absolute value", "radical", "cuberoot", "logn"]
    category_list = ["domain", "range", "equation", "draw"]

    x = ran.choice(funct_list), ran.choice(category_list)
    return x

print(mat())