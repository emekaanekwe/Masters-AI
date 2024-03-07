# improved version without import
mark = int(input("Input the number of marks: "))
n = [0]*mark
total = 0
for i in range(len(n)):
    marks = float(input(f"Input mark {i+1}:"))
    n[i] = marks
    total += n[i]
print("The average mark is", total/len(n))