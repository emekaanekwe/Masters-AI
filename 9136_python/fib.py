print("enter a number")
goal = int(input())
# recursive method
def get_fib(n):
    if n <= 1:
        return n
    # my way of writing 
    # return get_fib(n - 1) + get_fib(n - 2)
    # other way
    return (get_fib(n - 1) + get_fib(n - 2))
print("recursive", get_fib(goal))
